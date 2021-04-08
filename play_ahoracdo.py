import random
import os

def works():
    with open('./archivos/data.txt','r',encoding='utf-8') as f:
        works = [work.replace('\n','') for work in f]
    random_number = random.randint(1,len(works))
    return works[random_number]


def run():
    os.system('cls')
    input('BIENVENIDO A AHORCADO\nPRESIONA ENTER PARA COMENZAR')
    work = works()
    while True:
        print(list(enumerate(work)))
        break

 
if __name__ == '__main__':
    run()