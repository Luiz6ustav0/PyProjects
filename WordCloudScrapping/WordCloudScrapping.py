import operator
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np


def get_words(url, number_of_pages):
    word_list = []
    for num in range(0, number_of_pages): # this the range of pages we are going through in the website
        r_url = url + str(num) # completing the url iteration after iteration so we get new pages
        source_code = requests.get(r_url).text
        soup = BeautifulSoup(source_code, features='html.parser') # here we are getting the html
        print("\nPage: {page_number}".format(page_number=num)) 
        for soup_text in soup.findAll('span', {'class':'lx-stream-post__header-text gs-u-align-middle'}): # finding all text inside a <span> and belonging to that class
            content = soup_text.text # parsing to text
            words = content.lower().split() # separating all words and making them lower case so we don't count a word differently if it's uppercase
            for each_word in words:
                word_list.append(each_word)
    # print(word_list)
    return word_list

def clean_word_list(word_list): # this is where we clean the text we got from the website, it's usually very polluted
    # here we define all the words and symbols we want to take out of our text and make a new array with the clean text
    symbols = r'~!@#$%^&*()[]{}_-+`-\=,.<>/?;:"' # symbols that we don't want to show up on our cloud
    not_wanted = ['no', 'na', 'em', 'do', 'da', 'de', 'o', 'a', 'e', 'é', 'ao', 'um', 'pelo', 'para', 'que', 'à', 'após'
                  'por', 'mas', 'por', 'com', ' se', 'ser', 'nos', 'os', 'as', 'nas', 'diz', 'dos', 'tem', 'se', 'sobre'
                  'pela', 'mais', 'alta', 'setor', 'está', 'vez', 'sobre', 'vai', 'r$', 'não', '1º', 'trimestre', 'primeiro'
                  'segundo', 'terceiro', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'º', 'janeiro', 'fevereiro', 'março',
                  'abril', 'maio', 'junho', 'julho', 'agosto', 'outubro', 'setembro', 'novembro', 'dezembro', 'tri', 'ª', 'dá'
                  'até', 'quer', 'pós', 'será', 'deverão', 'subir', 'das', 'dos', 'às', 'são', 'pode', 'dar', 'até', 'bi', 'quem',
                  'entre', 'meio', 'há', 'como', 'após', 'foi']
    clean_list = [] 
    for word in word_list:
        for i in word:
            if i in symbols:
                word.replace(i, '')
        if len(word) > 0 and (word not in not_wanted): # taking out empty spaces and unwanted words
            clean_list.append(word)
    return clean_list

def create_wordcloud(clean_list):
    # defining and creating the word cloud here
    all_words = ' '.join(clean_list) # for the wordcloud we don't pass a dictionary, I simply put everything together separated by spaces and the library does the counting for us
    mask = np.array(Image.open('brazil.png'))
    cloud = WordCloud(background_color="white", mask=mask, width=1920, height=1080, max_words=1000).generate(all_words) 
    plt.figure(figsize=(16,9),facecolor = 'white', edgecolor='blue')
    plt.imshow(cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()

def get_top_words_and_count(clean_list):
    word_count = {} # I'm using this dictionary to count the number of times each word appears
    for word in clean_list:
        if word in word_count.keys():       
            word_count[word] = word_count[word] + 1
        elif word not in word_count.keys():  # if the word appears for the first time, adds it to the dic with the value 1
            word_count[word] = 1
        else:
            print('Something went wrong.')

    top_words = ['first']
    top_words_count = [0]

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)
        if len(top_words) < 11: # adds the words to the top 10 until we have at least 10 itens
            top_words_count.append(value)
            top_words.append(key)
        elif value > top_words_count[0]: # after getting 10 itens we check if the value is greater than some other value and add it if it is
            top_words_count.pop(0)
            top_words.pop(0)
            top_words_count.append(value)
            top_words.append(key)
        else:
            continue 
    return top_words, top_words_count

def plot_words_and_count(word_list, count_list): # this function is making a bar line and a bar graph
    tit = 'Most used words in the Headlines'
    x_label = 'Words'
    y_label = 'Count'

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(tit)

    plt.plot(word_list, count_list, color='r', linestyle='--')
    plt.bar(word_list, count_list) 

    plt.tick_params(labelsize=10)
    plt.show()


words = get_words(r'https://www.bbc.com/portuguese/topics/cz74k717pw5t/page/', 30)
clean_list = clean_word_list(words)
create_wordcloud(clean_list)
user_choice = input('Would you like to get a graph of the the top words versus how many times they appeared? (Y/n)')
if user_choice != 'n' and user_choice != 'N':
    top_w, top_w_c = get_top_words_and_count(clean_list)
    plot_words_and_count(top_w, top_w_c)