from abc import ABC
from abc import abstractmethod
from rich.panel import Panel
from rich import print


class Funcionario(ABC):
    def __init__(self,nome='', sal_bruto=0, salario=0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.sal_min = 1612
        self.inss = 7.5

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        painel = Panel(f'''
        O salário de {self.nome} ({type(self).__name__}) é de R${self.salario:.2f}
        e corresponde a {self.salario / self.sal_min:.2f} salários mínimos''', title='Analise de Funcionario', width=80)
        print(painel)


class FuncionarioHorista(Funcionario):
    def __init__(self,nome, valor_hora = 0, qtd_horas = 0):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = qtd_horas

    def calc_sal(self):
        self.salario = (self.valor_hora * self.horas_trab) - ((self.valor_hora * self.horas_trab)/100*self.inss)

        return self.salario


class FuncionarioMensalista(Funcionario):
    def __init__(self,nome, salario_bruto = 0):
        super().__init__(nome, salario_bruto)

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto/100*self.inss)

        return self.salario

