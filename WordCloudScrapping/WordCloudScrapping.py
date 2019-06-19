import operator
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np


def start(url):

    word_list = []
    for num in range(0, 13):
        r_url = url + str(num)
        source_code = requests.get(r_url).text
        soup = BeautifulSoup(source_code, features='html.parser')
        print("\nPage: {page_number}".format(page_number=num))
        for soup_text in soup.findAll('h2', {'class': 'title2'}):
            content = soup_text.text
            words = content.lower().split()
            for each_word in words:
                word_list.append(each_word)
            # print(each_word)
    # print(word_list)
    clean_word_list(word_list)


def clean_word_list(word_list): # this is where we clean the text we got from the website, it's usually very polluted

    symbols = r'~!@#$%^&*()[]{}_-+`-\=,.<>/?;:"' # symbols that we don't want to show up on our cloud
    clean_list = [] 
    # here we define all the words we want to take out of our text and make a new array with the clean text
    not_wanted = ['no', 'na', 'em', 'do', 'da', 'de', 'o', 'a', 'e', 'é', 'ao', 'um', 'pelo', 'para', 'que', 'à', 'após'
                  'por', 'mas', 'por', 'com', ' se', 'ser', 'nos', 'os', 'as', 'nas', 'diz', 'dos', 'tem', 'se', 'sobre'
                  'pela', 'mais', 'alta', 'setor', 'está', 'vez', 'sobre', 'vai', 'r$', 'não', '1º', 'trimestre', 'primeiro'
                  'segundo', 'terceiro', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'º', 'janeiro', 'fevereiro', 'março',
                  'abril', 'maio', 'junho', 'julho', 'agosto', 'outubro', 'setembro', 'novembro', 'dezembro', 'tri', 'ª', 'dá'
                  'até', 'quer', 'pós', 'será', 'deverão', 'subir', 'das', 'dos', 'às', 'são', 'pode', 'dar', 'até', 'bi']

    for word in word_list:
        for i in word:
            if i in symbols:
                word.replace(i, '')
        if len(word) > 0 and (word not in not_wanted):
            clean_list.append(word)



    create_dic(clean_list)

    # defining and creating the word cloud here

    zz = ' '.join(clean_list) # for the wordcloud we don't pass a dictionary, I simply put everything together separated by spaces and the library does the counting for us
    mask = np.array(Image.open('brazil.png'))
    cloud = WordCloud(background_color="white", width=1920, height=1080, mask = mask, max_words=1000).generate(zz)
    plt.figure(figsize=(16,9),facecolor = 'white', edgecolor='blue')
    plt.imshow(cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()


def create_dic(clean_list):
    
    word_count = {} # I'm using this dictionary to count the number of times each word appears

    for word in clean_list:
        if word in word_count.keys():       
            word_count[word] = word_count[word] + 1
        elif word not in word_count.keys():  # if the word appears for the first time, adds it to the dic with the value 1
            word_count[word] = 1
        else:
            print('Something went wrong.')

    most_words = ['first']
    most_count = [0]

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)
        if len(most_words) < 11: # adds the words to the top 10 until we have at least 10 itens
            most_count.append(value)
            most_words.append(key)
        elif value > most_count[0]: # after getting 10 itens we check if the value is greater than some other value and add it if it is
            most_count.pop(0)
            most_words.pop(0)
            most_count.append(value)
            most_words.append(key)
        else:
            continue

    dic_plot(most_words, most_count)


def dic_plot(word_list, count_list): # this function is making a bar line and a bar graph

    tit = 'Palavras Mais Usadas nas Manchetes'
    x_label = 'Palavras'
    y_label = 'Contagem'

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(tit)

    plt.plot(word_list, count_list, color='r', linestyle='--')
    plt.bar(word_list, count_list) 

    plt.tick_params(labelsize=10)
    plt.show()


start('https://www.valor.com.br/ultimas-noticias?page=')
