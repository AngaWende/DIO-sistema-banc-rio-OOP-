from conta import *

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    @property
    def contas(self):
        return self._contas

    @property
    def list_contas(self):
        if len(self._contas) > 0:
            lista = ''
            for i in self._contas:
                lista += i.resumo
            return lista
        else:
            return 'Sem contas cadastradas'

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, cliente,  num):
        conta = CC.new_account(cliente, num)
        self._contas.append(conta)
        return conta

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, dn, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._dn = dn

    @property
    def nome(self):
        return self._nome

