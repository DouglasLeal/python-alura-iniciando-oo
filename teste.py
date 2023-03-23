from conta import Conta

c1 = Conta(123, "Douglas", 100, 1000)
c2 = Conta(123, "Ana", 100, 1000)

c1.transferir(50, c2)

c1.extrato()
c2.extrato()