from abc import ABC, abstractmethod
from datetime import datetime


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        return f'|{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}| '


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.add_transacao(super().registrar(conta) + f'Depósito: +R${self.valor}')


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.add_transacao(super().registrar(conta) + f'Saque: -R${self.valor}')


class Historico:
    def __init__(self):
        self._hist = ['\nExtrato detalhado:\n']

    def mostrar_historico(self, saldo):
        txt = ''
        for i in self._hist:
            txt += i
        txt += f'\n\nSaldo atual: R${saldo}'
        print(txt)

    def add_transacao(self, transacao):
        self._hist.append(f'\n{transacao}')


class Conta:

    def __init__(self, cliente, numero):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0213'
        self._cliente = cliente
        self._numero_de_saques = 3
        self._historico = Historico()

    @property
    def historico(self):
        return self._historico

    def extrato(self):
        return self._historico.mostrar_historico(self._saldo)

    @property
    def saldo(self):
        return self._saldo


    @property
    def resumo(self):
        return f'''Cliente: {self._cliente.nome}\nNúmero:{self._numero}\nAgência: {self._agencia}\n\n'''

    @classmethod
    def new_account(cls, numero, cliente):
        return cls(numero, cliente)

    @staticmethod
    def _validar_valor(valor):
        if (isinstance(valor, float) or isinstance(valor, int)) and valor > 0:
            return True
        else:
            return False

    def sacar(self, valor):
        if not self._validar_valor(valor):
            print('Valor inválido')
            return False
        elif valor > self._saldo:
            print("Saldo indisponível")
            return False
        elif self._numero_de_saques < 1:
            print('Qtde de saques ultrapassada')
            return False
        elif valor > 500:
            print('O limite máximo por saque é de R$500,00')
            return False
        else:
            self._saldo -= valor
            self._numero_de_saques -= 1
            return True

    def depositar(self, valor):

        if self._validar_valor(valor):
            self._saldo += valor
            return True
        else:
            print('Valor de depósito inválido')
            return False


class CC(Conta):
    def __init__(self, cliente, numero):
        super().__init__(cliente, numero)
        self._limite_saque = 3
