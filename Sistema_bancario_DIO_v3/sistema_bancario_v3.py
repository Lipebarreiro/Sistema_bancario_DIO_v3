import textwrap
from abc import ABC, abstractmethod

# =================== CLASSES ===================

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def __str__(self):
        if not self.transacoes:
            return "Não foram realizadas movimentações."
        extrato = ""
        for t in self.transacoes:
            extrato += f"{t.__class__.__name__}: R$ {t.valor:.2f}\n"
        return extrato


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n[ERRO] Operação falhou! Valor inválido!")


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n[ERRO] Operação de saque não permitida!")


class Conta:
    def __init__(self, cliente, numero, agencia="0001"):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo_atual(self):
        return self.saldo

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    def sacar(self, valor):
        if valor <= 0 or valor > self.saldo:
            return False
        self.saldo -= valor
        return True

    def depositar(self, valor):
        if valor <= 0:
            return False
        self.saldo += valor
        return True


class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saques=3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([t for t in self.historico.transacoes if isinstance(t, Saque)])
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n[ERRO] Valor do saque excede o limite!")
            return False
        if excedeu_saques:
            print("\n[ERRO] Número máximo de saques excedido!")
            return False
        return super().sacar(valor)


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

# =================== FUNÇÕES DO MENU ===================

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n[ERRO] Já existe um usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuario = PessoaFisica(nome, cpf, data_nascimento, endereco)
    usuarios.append(usuario)

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None


def criar_conta(numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        conta = ContaCorrente.nova_conta(usuario, numero_conta)
        usuario.adicionar_conta(conta)
        contas.append(conta)
        print("\n=== Conta criada com sucesso! ===")
        return conta

    print("\n[ERRO] Usuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    if not contas:
        print("\n[ERRO] Nenhuma conta cadastrada!")
        return

    for conta in contas:
        linha = f"""\n
            Agência:\t{conta.agencia}
            C/C:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def exibir_extrato(conta):
    print("\n================ EXTRATO ================")
    print(conta.historico)
    print(f"\nSaldo:\t\tR$ {conta.saldo_atual():.2f}")
    print("==========================================")

# =================== PROGRAMA PRINCIPAL ===================

def main():
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            cpf = input("Informe o CPF do usuário: ")
            usuario = filtrar_usuario(cpf, usuarios)
            if not usuario:
                print("\n[ERRO] Usuário não encontrado!")
                continue
            if not usuario.contas:
                print("\n[ERRO] Usuário não possui conta cadastrada!")
                continue

            valor = float(input("Informe o valor do depósito: "))
            conta = usuario.contas[0]
            transacao = Deposito(valor)
            usuario.realizar_transacao(conta, transacao)

        elif opcao == "s":
            cpf = input("Informe o CPF do usuário: ")
            usuario = filtrar_usuario(cpf, usuarios)
            if not usuario:
                print("\n[ERRO] Usuário não encontrado!")
                continue
            if not usuario.contas:
                print("\n[ERRO] Usuário não possui conta cadastrada!")
                continue

            valor = float(input("Informe o valor do saque: "))
            conta = usuario.contas[0]
            transacao = Saque(valor)
            usuario.realizar_transacao(conta, transacao)

        elif opcao == "e":
            cpf = input("Informe o CPF do usuário: ")
            usuario = filtrar_usuario(cpf, usuarios)
            if not usuario:
                print("\n[ERRO] Usuário não encontrado!")
                continue
            if not usuario.contas:
                print("\n[ERRO] Usuário não possui conta cadastrada!")
                continue

            conta = usuario.contas[0]
            exibir_extrato(conta)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, usuarios, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("\nEncerrando o sistema... Volte sempre!\n")
            break

        else:
            print("[ERRO] Operação inválida, por favor selecione novamente a operação desejada.")

main()