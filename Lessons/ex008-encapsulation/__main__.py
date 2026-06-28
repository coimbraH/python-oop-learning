from ex008 import ContaBancaria

def main():
    c1 = ContaBancaria(111, "Henrique", 5000)
    c1.depositar(1000)

    c1._titular = "Maria" # Python deixa, porém não mexa "Adults Consenting"...
#    c1.__saldo = 0 # Dessa forma cria um novo atributo '__saldo': 0 e não mexe no principal, proque:
    c1._ContaBancaria__saldo = 0 #Dessa forma mexeria no saldo principal, porém , "Adults Consenting"
    #O que aprendemos aqui, python não protege dados e deixa tudo exposto,
    #apenas temos uma convenção sobre não mexer nos atributos e métodos que estão
    #privados ou protegidos. É uma regra que pode ser quebrada, mas não se deve.
    #É mais uma filosofia ou acordo do que uma regra.


    print(c1)


if __name__ == '__main__':
    main()