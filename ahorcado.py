from os import replace, system
import random
import re

def clean():
    system('clear')

def read():
    with open ("./files/data.txt", "r", encoding="UTF-8") as file:
        words = [i.replace("\n", '')
        .replace('á', 'a')
        .replace("é", "e")
        .replace("í", "i")
        .replace('ó', 'o')
        .replace('ú', 'u') for i in file]
        return words

def run():
    finished = False
    hidden_word = ""
    words = read()
    word = random.choice(words)
    for letter in word:
        hidden_word += "_"
    while finished == False:
        clean()
        print('Veamos si esto es de tu talla.')
        print(hidden_word)
        selected_letter = input('Ingresa una letra: ')
        assert selected_letter != '', 'Debes introducir una letra'
        match = re.compile(selected_letter)
        for letter in match.finditer(word):
            hidden_word = hidden_word[:letter.start()] + letter.group().upper() + hidden_word[letter.start() + 1:]
            if hidden_word.__contains__('_') == False:
                finished = True
    clean()
    print(hidden_word)
    print('¡Lo lograste! La palabra es: ' + hidden_word)
if __name__ == '__main__':  
    run()
    