from ex010 import Avaliacao
from rich import print, inspect


def main():
    av1 = Avaliacao('Pedro', 'Matemática')
    av1.nota = 7 #Diferente de getter and setter, ele se parece com atributo normal, mas dispara o setter
    inspect(av1, private=True)
    print(f'{av1.nome} tirou {av1.nota} em {av1.disciplina}')


if __name__ == '__main__':
    main()