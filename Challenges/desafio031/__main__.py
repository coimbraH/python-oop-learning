from classes import Retangulo
from rich import print, inspect

def main():
    c = Retangulo(-2, 5)

#    c.altura = 23
#    c.base = 12
#    c.medidas = (9, 3)

    inspect(c, private=True, methods=True)




if __name__ == '__main__':
    main()