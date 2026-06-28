from rich import print, inspect
from classes import Diario


def main():
    d = Diario('vuvuzela')
    d.escrever('Primeira mensagem')
    d.escrever('Você é lindo.')
    d.escrever('Teste concluído com sucesso.')
    inspect(d, methods=True, private=True)
    d.ler('vuvuzela')



if __name__ == '__main__':
    main()