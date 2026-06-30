from abc import ABC
from datetime import datetime

class Pessoa(ABC):
    def __init__(self, nome='', nascimento=0):
        self._nome = nome
        self._nascimento = nascimento


    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano):
        anoatual = datetime.now().year
        if ano > anoatual or ano > anoatual-15:
            raise ValueError('Digite um ano válido')
        elif ano < anoatual -70:
            raise ValueError('Digite um ano valido')
        else:
            self._nascimento = ano

    @property
    def idade(self):
        anoatual = datetime.now().year
        return anoatual - self._nascimento
    @idade.setter
    def idade(self, ano):
        raise PermissionError('Você não pode alterar a idade. Mude o ano de nascimento')


class Aluno(Pessoa):
    def __init__(self, nome='', nascimento=0, curso = ''):
        super().__init__(nome, nascimento)
        self.cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']
        self._curso = curso

    @property
    def curso(self):
        return self.curso

    @curso.setter
    def curso(self, curso):
        raise ValueError(f'O curso {curso} não está na lista de cursos oficiais')

    def add_curso(self,curso):
        if 3 <= len(curso) <= 5:
            self.cursos_oficiais.append(curso)
        else:
            raise ValueError('O nome do curso deve conter entre três e cinco letras.')
