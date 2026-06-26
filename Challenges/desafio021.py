#Crie a classe caneta, que simule o funcionamento de uma caneta colorida
#podendo escrever frases na cor relativa

from rich import print

class Caneta():

    def __init__(self, cor=''):
        self.cor = cor
        self.tampa = ''
    def cores(self):
        if self.cor == 'vermelho':
            return '[red]'
        elif self.cor == 'azul':
            return '[blue]'
        elif self.cor == 'verde':
            return '[green]'
        else:
            return 'Não temos essa cor de caneta. \n'

    def destampar(self):
        self.tampa = 'ok'

    def escrever(self, texto =''):
        if self.tampa == 'ok':
            print(f'{self.cores()} {texto}', end='')
        else:
            print(' :prohibited: A caneta está tampada !', end='')

    def quebrar_linha(self, n):
        print('\n'*n)


c1 = Caneta('azul')
c2 = Caneta('vermelho')
c3 = Caneta('verde')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá, Mundo!')
c1.quebrar_linha(2)
c2.escrever('Olá, Gafanhoto!')
c3.escrever('Vamos exercitar!')

