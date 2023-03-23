from conta import Conta

c1 = Conta(123, "Douglas", 100, 1000)
c2 = Conta(123, "Ana", 100, 1000)

print(c1.limite)
c1.limite = 1500
print(c1.limite)