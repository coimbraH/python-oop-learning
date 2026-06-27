#Crie a classe PRODUTO, onde podemos cadastrar NOME e PREÇO.
#Crie também um method que mostre uma etiqueta de preço do produto
from rich.panel import Panel
from rich import print


class Produto:
    def __init__(self, produto='', preco=0):
          self.produto = produto
          self.preco = preco

    def etiqueta(self):
        x =  Panel(f"{self.produto:^35} \n {'-'*33}\n {self.preco:.^33,.2f}",
                   title='Produto',
                   style='blue',
                   width=40,
                   subtitle='okoko',
                   subtitle_align="right"
                   )
        print(x)

p1 = Produto('Mouse', 120)
p1.etiqueta()

p2 = Produto('Notebook', 3000)
p2.etiqueta()