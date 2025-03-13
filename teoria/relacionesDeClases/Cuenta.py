#Autor: Paredes Calderon Baruch Andre
class Cuenta:
    def __init__(self, valor, tipo, propietario):
        self.saldo = valor  
        self.tipo = tipo  
        self.propietario = propietario 
    
    def obtenerDetalles(self):
        return {
            "Propietario": self.propietario,
            "Tipo de cuenta": self.tipo,
            "Saldo actual": self.saldo
        }
        
    def depositar(self, deposito):
        if deposito > 0:
            self.saldo += deposito
            return self.saldo
        else:
            return None  
        
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            return None  
        elif cantidad <= 0:
            return None  
        else:
            self.saldo -= cantidad
            return self.saldo


       