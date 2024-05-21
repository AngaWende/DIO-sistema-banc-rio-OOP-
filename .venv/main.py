from classes import *
from conta import *

if __name__ == '__main__':

    menu = """
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Cadastrar novo cliente
    [l] Listar clientes
    [cc] Criar nova conta
    [lc] Listar contas por cliente
    [lt] Listar todas as contas
    [q] Sair

=> """
    lista_clientes = {}
    lista_contas = []


    def validar_cliente(cpf):
        return True if cpf in lista_clientes.keys() else False


    def cadastrar_cliente():
        cpf = input('Digite o CPF: ')
        if cpf in lista_clientes.keys():
            print('Cliente já cadastrado.')
        else:
            nome = input('Digite o nome:')
            dn = input('Digite a data de nascimento:')
            end = input('Digite o o endereço:')
            lista_clientes[cpf] = PessoaFisica(cpf, nome, dn, end)
            print(' --- Cliente cadastrado com sucesso ---')


    def nova_conta(num_conta):
        cpf = input('digite o cpf:')
        if cpf not in lista_clientes.keys():
            print('cliente não cadastrado')
        else:
            nova_conta = lista_clientes[cpf].adicionar_conta(lista_clientes[cpf], num_conta)
            print(' --- Conta adicionada com sucesso ---')
            return nova_conta

    def listar_todas_as_contas():
        if len(lista_contas) > 0:
            lista = ''
            for i in lista_contas:
                lista += i.resumo
                # print(i)
            print(lista)
        else:
            return 'Sem contas cadastradas'

    def sacar():
        cpf = input('Digite o CPF: ')
        if validar_cliente(cpf):
            if len(lista_clientes[cpf].contas) > 0:
                valor = float(input('Digite o valor: '))
                lista_clientes[cpf].realizar_transacao(lista_clientes[cpf].contas[0], Saque(valor))
            else:
                print('Sem conta cadastrada.')

        else:
            print('CPF não encontrado.')


    def depositar():
        cpf = input('Digite o CPF: ')
        if validar_cliente(cpf):
            if len(lista_clientes[cpf].contas) > 0:
                valor = float(input('Digite o valor: '))
                lista_clientes[cpf].realizar_transacao(lista_clientes[cpf].contas[0], Deposito(valor))
            else:
                print('Sem conta cadastrada.')

        else:
            print('CPF não encontrado.')


    def mostrar_extrato():
        cpf = input('Digite o cpf:')
        if validar_cliente(cpf):
            lista_clientes[cpf].contas[0].extrato()
        else:
            print('CPF não encontrado.')

    def listar_contas():
        cpf = input('Digite o CPF: ')
        if validar_cliente(cpf):
            print(lista_clientes[cpf].list_contas)

    while True:
        choice = input(menu)

        match choice:
            case 'd':
                depositar()
            case 's':
                sacar()

            case 'e':
                mostrar_extrato()
            case 'c':
                cadastrar_cliente()
            case 'l':
                for i, j in lista_clientes.items():
                    print(i, j.nome)
            case 'cc':
                num_conta = len(lista_contas)+1
                lista_contas.append(nova_conta(num_conta))
            case 'lc':
                listar_contas()
            case 'lt':
                listar_todas_as_contas()
            case 'q':
                break
            case _:
                print('Opção inválida.\n')
