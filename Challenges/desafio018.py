#Crie uma classe chamada Churrasco, onde seja possível informar
#Quantas pessoas vão participar e mostre quanto de carne deve ser comprado,
#O custo total do churrasco e o preço por pessoa
#Considerar custo por pessoa 400g, e o preço 82,40/kg

from rich.panel import Panel
from rich import print

class Churrasco():
    def __init__(self, titulo = '', quant = 0):
        self.evento = titulo
        self.pessoas = quant


    def analisar(self):
        quant = self.pessoas * 0.4
        custototal = quant*82.4
        x = Panel(f'''
        Analisando {self.evento} com {self.pessoas} convidados
        Cada participante comerá 0.4Kg e cada Kg custa R$82,40
        Recomendo comprar {quant:.3f}Kg de carne
        O custo total será de R${custototal:.2f}
        Cada pessoa pagará R${custototal/self.pessoas:.2f} para participar
        ''',
        title=self.evento,
        width=70,
        )
        print(x)


c1 = Churrasco('Churras dos Amigos', 100)
c1.analisar()