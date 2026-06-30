from rich import print, inspect

from classes import ContaBancaria


def main():
    print('Criando a conta...')
    cc = ContaBancaria(123, 'Henrique', 1000, 'vuvuzela')

    print('Realizando depósito')
    cc.depositar(500)

    print('Realizando saque')
    cc.sacar(300)
    inspect(cc, methods=True, private=True)




if __name__ == '__main__':
    main()