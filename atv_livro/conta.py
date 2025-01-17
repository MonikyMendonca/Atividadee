class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print(f"CC N° {self.numero} Saldo: {self.saldo:10.2f}")
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome}\nTelefone: {cliente.telefone}\n")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print("O saldo é insuficiente!")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPOSITO", valor])

    def extrato(self):
        print(f"Extrato CC N° {self.numero}\n")
        for o in self.operacoes:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print(f"\nSaldo: {self.saldo:10.2f}\n")

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print("Saldo insuficiente, mesmo com o limite!")

# Criação de instâncias da classe Cliente
fernando = Cliente("Fernando da Silva", "8883 - 4321")
fatima = Cliente("Fatima da Silva", "3333 - 1234")

# Criação da conta
conta = Conta([fernando, fatima], 1234, 5000)
conta.resumo()
