#declaração de classe
class Gafanhoto:
        def __init__(self): #método construtor
            #atributos de instancia
            self.nome = ("")
            self.idade = 0

        #metodo de instancia
        def aniversario(self):
            self.idade += 1

        def mensagem(self):
            return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"

#declaração de objeto
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Mauro"
g2.idade = 53
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())

g4 = Gafanhoto()
g4.nome = "Henrique"
g4.idade = 30
g4.aniversario()
print(g4.mensagem())