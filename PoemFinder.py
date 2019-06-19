import urllib.request
from bs4 import BeautifulSoup


def spider(topic):
    key_w = str(topic)

    get_name = input("Como deseja nomear o arquivo? ") # how would you like to name the file?
    f_name = get_name + '.txt'
    fx = open(str(f_name), 'w')

    page = 1

    log = 1
    while log == 1:
        url = 'https://www.pensador.com/' + key_w + r'/' + str(page) # this is the page url, you can change this but make sure to check the logic for scanning however many pages you would like
        print('Fonte: {}'.format(url))
        # print(url)
        sourcecode = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(sourcecode, features='html.parser')
        for z in soup.findAll('p'):
            fx.write("\n{} \n\n".format(z.text))
            fx.write("\n\n______________________________________\n")

        more_pages = input(
            '\nOk... Gostaria que mais frases e poemas fossem salvos em {0}? 1 para sim'
            ' ou 0 para nao: \n'.format(get_name)) # asks if the user wants to scan more pages(1) or not(0)
        if more_pages == '1':
            page += 1
            continue
        elif more_pages == '0':
            print('\n:)')
            log = 0
        else:
            print('Nao entendi sua escolha... reinicie o programa')
            break
    fx.close()
    print("\nProntinho, dezenas de frases e outros textos interessantes sobre {} "
          "acabaram de ser salvos...".format(key_w))
    print('\nFoi um prazer poder ajudar!\n')


def get_i():
    subject = input("Deseja frases e poemas sobre qual assunto? Digite apenas uma palavra, sem acentos: ") # asks the topic
    return subject


spider(get_i())

