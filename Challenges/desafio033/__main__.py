from rich import print, inspect
from classes import Aluno, Pessoa


def main():
    a1 = Aluno('Maria', 2000, 'ADM')
    a1.add_curso('MED')
    a1.curso = 'MED'
    inspect(a1, methods=True, private=True)


if __name__ == '__main__':
    main()