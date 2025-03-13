#Autor:Paredes Calderon Baruch Andre
from Cuenta import Cuenta
from Cliente import Cliente
from Menu import Menu

class Main:
    pass

cuenta1 = Cuenta(4500, "débito", "Baruch P")

detalles = cuenta1.obtenerDetalles()
print("\nDetalles de la Cuenta:")
print("Propietario:", detalles["Propietario"])
print("Tipo de cuenta:", detalles["Tipo de cuenta"])
print("Saldo actual: $", detalles["Saldo actual"])

menu1 = Menu("¡Bienvenido a Bancomer!", cuenta1)
menu1.Bienvenida()
menu1.opciones()  

detalles = cuenta1.obtenerDetalles()
print("\nDetalles de la Cuenta:")
print("Propietario:", detalles["Propietario"])
print("Tipo de cuenta:", detalles["Tipo de cuenta"])
print("Saldo actual: $", detalles["Saldo actual"])
    
cliente1 = Cliente("Baruch Andre Paredes Calderon", "Av. Reforma 145", 18)
cliente1.imprimirDetalles()






