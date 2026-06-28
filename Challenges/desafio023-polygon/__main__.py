from rich import print, inspect
from class_desafio023 import *

def main():
    p1 = Quadrado(20)

    print(f'Perimetro = {p1.perimetro():.1f}cm')
    print(f'Area = {p1.area():.1f}cm²')

    p2 = Circulo(12)
    print(f'Perimetro = {p2.perimetro():.1f}cm')
    print(f'Area = {p2.area():.1f}cm²')


if __name__ == '__main__':
    main()