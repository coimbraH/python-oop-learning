from rich import print, inspect
from classes import Credencial

def main():
    c = Credencial()
    c.senha = 'Henrique'
    inspect(c, methods=True, private=True)
    c.validar('Henrique')

if __name__ == '__main__':
    main()