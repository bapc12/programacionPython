#Autor:Paredes Calderon Baruch Andre
from MenuBanco import MenuBanco
from Cuenta import Cuenta
from Cliente import Cliente

class Main:
    pass

menu = MenuBanco("¡Bienvenido a Bancomer¡")
menu.bienvenida()  

cuenta1 = Cuenta(4500, "débito", "Baruch P")
cuenta1.imprimirDetalles()
cuenta1.depositar(500)  
cuenta1.retirar(5000)   

cliente1 = Cliente("Baruch Andre Paredes Calderon", "Av. Reforma 145", 18)
cliente1.imprimirDetalles()