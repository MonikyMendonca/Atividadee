from conta import Cliente, Conta

fernando = Cliente("Fernando da Silva", "888 - 4321")
fatima = Cliente("Fatima da Silva", "333 - 1234")
conta1 = Conta([fernando], 1, 1000)
conta2 = Conta([fatima, fernando], 2, 500)
conta1.saque(20)
conta2.deposito(4000)
conta1.saque(999)

conta2.deposito(95.15)
conta2.saque(250)

conta1.extrato()
conta2.extrato()