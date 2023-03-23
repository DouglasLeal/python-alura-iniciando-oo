class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo {self.__saldo} do titular {self.__titular}")

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destinho):
        self.sacar(valor)
        destinho.depositar(valor)

    @property   
    def titular(self):
        return self.__titular.title()
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter   
    def limite(self, valor):
        self.__limite = valor