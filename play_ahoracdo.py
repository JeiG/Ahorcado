import random
import os

def works():
    with open('./archivos/data.txt','r',encoding='utf-8') as f:
        works = [work.replace('\n','') for work in f]

    random_number = random.randint(1,len(works))
    return works[random_number]


def verification(letters,work):
    clave = ''
    for i in work:
        if i in letters:
            clave += i
        else:
            clave += '-' 
    return clave 


def run():
    os.system('cls')
    input('BIENVENIDO A AHORCADO\nPRESIONA ENTER PARA COMENZAR ')
    work = works()
    letters = []

    while True:
        letter = input('Enter a letter: ')
        letters.append(letter)
        clave = verification(letters,work)
        print(clave)
        if clave == work:
            print('Has adivinado la palabra')
            break

 
if __name__ == '__main__':
    run()