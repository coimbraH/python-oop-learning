from pwinput import pwinput
from rich import print, inspect
import hashlib
from time import sleep

class ContaBancaria:
    def __init__(self, numconta, nome: str, saldo: float, chave: str):
        self._id = numconta
        self._titular = nome
        self.__saldo = saldo
        self.__hash = hashlib.sha256(str(chave).encode()).hexdigest()


    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, nome = ''):
        senha = self.pede_senha()
        if self.validar_senha(senha) == True:
            print(f'Nome alterado com sucesso para {nome}')
            self._titular = nome
        else:
            print('Senha incorreta. Nome não alterado.')


    def validar_senha(self, chave):
        if hashlib.sha256(str(chave).encode()).hexdigest() == self.__hash:
            return True
        else:
            return False

    def pede_senha(self) -> str:
        return pwinput('Digite sua senha: ', mask='*')

    def sacar(self, valor: float, chave = None):
        print(f'Solicitando saque no valor de {valor}')
        if chave == None:
            senha = self.pede_senha()
        else:
            senha = chave
        if self.validar_senha(senha) == True:
            self.__saldo -= valor
            print(f'Saque de R${valor:.2f} autorizado na conta {self._id}')
        else:

            print('Senha incorreta. Saque não autorizado.')


    def depositar(self, valor):
        print('Depositando saldo...')
        sleep(0.5)
        self.__saldo += valor
        print(f'Depósito autorizado na conta {self._id}')