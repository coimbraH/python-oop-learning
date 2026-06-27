from rich import inspect
from classesex005 import Aluno, Professor, Funcionario

def main():
    a1 = Aluno('José', 17, 'Informática', 'T01')
    a1.fazer_aniversario()
    #inspect(a1, methods=True)
    a1.fazer_matricula()

    p1 = Professor('Samuel', 37, 'Biologia', 'Mestrado')
    #inspect(p1, methods=True)
    p1.dar_aula()

    f1 = Funcionario('Claudia', 27, 'Secretária', 'Secretaria')
    f1.fazer_aniversario()
    #inspect(f1, methods=True)
    f1.bater_ponto()

if __name__ == '__main__':
    main()