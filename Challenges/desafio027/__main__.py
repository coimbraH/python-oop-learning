#simule o sistema de batalha entre personagens de um RPG
#cura de 100 pontos no maximo
from classes import *

def main():
    p1 = Guerreiro('Kratos', 2000)
    p2 = Mago('Merlin', 3000)

    p1.atacar(p2, 1000)
    p2.curar()
    p2.atacar(p1, 500)

if __name__ == '__main__':
    main()