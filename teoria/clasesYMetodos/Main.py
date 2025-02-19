from MenuBanco import MenuBanco
from Cuenta import Cuenta
from Cliente import Cliente

class Main:
    pass

menu = MenuBanco("¡Bienvenido a Bancomer¡")
menu.bienvenida()  
cuenta1 = Cuenta(4500, "credito", "Baruch P")
cuenta1.imprimirDetalles()
cliente1 = Cliente("Baruch Andre Paredes Calderon", "Av. Reforma 145", 18)
cliente1.imprimirDetalles()