#Criar classes capazes de calcular fretes de veiculos diferentes
from classes import *
from rich import print, inspect
from rich.table import Table
from rich.console import Console

def main():
    dist = 50
    viagens = [Caminhao(dist), Moto(dist), Drone(dist)]
    entrega = Caminhao(dist)
    print(f'Frete de {type(entrega).__name__} em {dist}Km custará {entrega.calc_frete()}')

    table = Table(title='Fretes')
    table.add_column('Distância', justify='center', style='blue')
    table.add_column('Transporte', justify='center', style='blue')
    table.add_column('Frete', justify='center',style='blue')
    for viagem in viagens:
        table.add_row(str(viagem.distancia), str(type(viagem).__name__), str(viagem.calc_frete()))
    console = Console()
    console.print(table)






if __name__ == '__main__':
    main()