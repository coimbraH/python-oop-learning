#implemente um termostato orientado a objetos
#quando liga o termostato ele inicia em 24 graus.
#o minimo dele é 16 graus e o maximo é 30
#ele mexe a temperatura de 0.5 grau em 0.5 grau

from rich import print, inspect
from classes import Termostato

def main():
    t = Termostato()
    try:
        t.temperatura = 25.2
    except Exception as e:
        print(f'Houve um problema {e}:')


    inspect(t, private=True, methods=True)
    print(f'A temperatura atual é {t.ftemperatura}')


if __name__ == '__main__':
    main()