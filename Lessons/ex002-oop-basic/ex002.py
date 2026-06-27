#Esse exercicio demonstra como usar os métodos de classe
#E também como não atribuir diretamente fora da classe
#Explicando utilização de dunder attributes e dunder methods
#declaração de classe
#ESTADO == conjunto de valores atribuídos a um objeto
class Gafanhoto:
    #DOCUMENTAÇÃO DE CLASSE:
    """
Essa classe criar um gafanhoto, que é uma pessoa que tem nome e idade.

Para criar uma nova pessoa, use
variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "", idade = 0): #metodo construtor
        #atributos de instancia
        self.nome = nome
        self.idade = idade

    #metodo de instancia
    def aniversario(self):
        self.idade += 1

#    def mensagem(self): #Dunder Method - substituido por metodo str
#        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"

    def __str__(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"

#declaração de objeto
g1 = Gafanhoto("Maria", 17)
g1.aniversario()
print(g1)
print(g1.__dict__) #Attribute - para colocar em dicionario
print(g1.__getstate__()) #Method - para mostrar o estado
#print(g1.mensagem())
#print(g1.__doc__) # Dunder Attribute
print(g1.__class__) #Attribute - Para ver o nome da classe