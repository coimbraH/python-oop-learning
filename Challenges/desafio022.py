#Crie a classe ControleRemoto, onde vamos simular o funcionamento
#De um controle simples (canal, volume e liga/desliga)

from rich.panel import Panel
from rich import print

class ControleRemoto:
    def __init__(self):
        self.ligada = False
        self.volume = 1
        self.canal = 1
    def ligar(self):
        barra = ''
        for i in range(5):
            if i < self.volume:
                barra += "[on blue] [/] "
            else:
                barra += "[on white] [/] "
        canal = [' 1 ',' 2 ',' 3 ',' 4 ',' 5 ']
        for i in range(5):
            if i+1 == self.canal:
                canal[i] = f'[on blue] {i+1} [/]'
            else:
                canal[i] = f'[on white] {i+1} [/]'

        print(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        x = Panel(f'CANAL = {"".join(canal)} \nVOLUME = {barra}', title='[  TV  ]', width=30)
        print(x)
        print(f'< CH >   - VOL{self.volume} + ', end='')

    def desligar(self):
        print(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        x = Panel(f'A TV está desligada', title='[  TV  ]', width=30)
        print(x)
        print('< CH >   - VOL + ', end='')

    def aumentar_volume(self, botao=''):
        if self.volume < 5:
            self.volume += 1


    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def proximo_canal(self):
        if self.canal < 5:
            self.canal += 1
        else:
            self.canal = 1

    def canal_anterior(self):
        if self.canal > 1:
            self.canal -= 1
        else:
            self.canal = 5


controle = ControleRemoto()
while True:
    controle.desligar()
    botao = input('')
    if botao == '@':
        while True:
            controle.ligar()
            botao = input('')

            if botao == '@':
                break
            if botao == '+':
                controle.aumentar_volume()
            if botao == '-':
                controle.diminuir_volume()
            if botao == '>':
                controle.proximo_canal()
            if botao == '<':
                controle.canal_anterior()

        continue





