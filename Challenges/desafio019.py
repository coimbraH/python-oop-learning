#Crie uma classe Livro, que vai simular a passagem de paginas de um livro,
#Considerando também se o usuário chegou ao fim da leitura
from rich import print
from time import sleep

total= {'cont':1}
class Livro:

    def __init__(self, livro='', paginas=0):
        self.livro = livro
        self.paginas = paginas
        inicial = 1
        print(f"Você acabou de abrir o livro '{self.livro}' \nque tem {self.paginas} paginas no total.\n"
              f"Você está agora na página {inicial}")
    def avancar_paginas(self,n):
        for x in range(n):
            if total['cont'] == self.paginas:
                n = x
                break
            else:
                total['cont'] += 1
                print(f"Pág{total['cont']} ->", end=' ')
                sleep(0.5)
        sleep(1)
        print(f'Você avançou {n} páginas e agora está na página {total['cont']}')


l1 = Livro('10 Coisas que Aprendi', 20 )
l1.avancar_paginas(10)
l1.avancar_paginas(5)
l1.avancar_paginas(100)