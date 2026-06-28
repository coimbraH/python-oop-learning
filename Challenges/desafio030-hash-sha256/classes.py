import hashlib


class Credencial:
    def __init__(self):
        self.__hash = ''

    @property
    def senha(self):
        return self.__hash
    @senha.setter
    def senha(self, senha):
        self.__hash = hashlib.sha256(str(senha).encode()).hexdigest()

    def validar(self,chave):
        chave_hash = hashlib.sha256(str(chave).encode()).hexdigest()
        if chave_hash == self.__hash:
            print('Senha Correta')
        else:
            print('Senha errada.')



