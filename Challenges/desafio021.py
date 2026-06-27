#Crie a classe caneta, que simule o funcionamento de uma caneta colorida
#podendo escrever frases na cor relativa

from rich import print

class Caneta():

    def __init__(self, cor='azul'):
        self.cor = cor
        self.tampa = True
    def cores(self):
        if self.cor == 'vermelho' or self.cor == 'vermelha':
            return '[red]'
        elif self.cor == 'azul':
            return '[blue]'
        elif self.cor == 'verde':
            return '[green]'
        else:
            return 'Não temos essa cor de caneta. \n'

    def destampar(self):
        self.tampa = False
    def tampar(self):
        self.tampa = True

    def escrever(self, texto =''):
        if self.tampa == False:
            print(f'{self.cores()} {texto}', end='')
        else:
            print(f' :prohibited: A {self.cores()}caneta[/] está tampada !', end='')

    def quebrar_linha(self, n=1):
        print('\n'*n)


c1 = Caneta('azul')
c2 = Caneta('vermelho')
c3 = Caneta('verde')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Hi ! =)')
c1.quebrar_linha(2)
c2.escrever('Eae !')
c3.escrever('Tudo bonitinho!')
c1.quebrar_linha()
c3.tampar()
c3.escrever('Teste de tampa')

