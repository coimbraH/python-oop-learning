class Avaliacao:
    def __init__(self, nome, disciplina, nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # atributo protected (#)

    #Criando atributo validável
    #@property pra quem mexe no programa principal faz com que se pareça um atributo normal
    @property
    def nota(self): #getter
        return self._nota

    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print('Nota inválida')

    @nota.deleter #só pra mostrar que existe
    def nota(self):
        pass

    @nota.getter #só pra mostrar que existe
    def nota(self):
        pass