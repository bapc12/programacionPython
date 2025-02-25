#Autor: Paredes Calderon Baruch Andre
class Cuenta:
    def __init__(self,valor,tipo,propietario):
        self.saldo= valor
        self.tipo= tipo
        self.propietario= propietario
    
    def imprimirDetalles(self):
        print("Desde el metodo")
        print("saldo:",self.saldo)
        print("tipo:",self.tipo)
        print("nombre:",self.propietario)
        
    def depositar(self,deposito):
        if deposito>0:
            print("Depósito exitoso. Su nuevo saldo es de :",self.saldo+deposito)
        else:
            print("Depósito inválido") 
        
    def retirar(self,cantidad):
        if cantidad > self.saldo:
            print("No se puede realizar el retiro.")
        elif self.saldo >= cantidad:
            print("Retiro exitoso. Nuevo saldo:",self.saldo-cantidad)