#Autor:Paredes Calderon Baruch Andre
class Menu:
    def __init__(self, mensaje, cuenta):
        self.mensajeBienvenida = mensaje
        self.cuenta = cuenta  

    def Bienvenida(self):
        print(self.mensajeBienvenida)

    def retirar(self):
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        nuevo_saldo = self.cuenta.retirar(cantidad)
        if nuevo_saldo is not None:
            print(f"Retiro exitoso de ${cantidad}. Nuevo saldo: ${self.cuenta.saldo}")
        else:
            print("Error: Fondos insuficientes o monto inválido.")

    def depositar(self):
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        nuevo_saldo = self.cuenta.depositar(cantidad)
        if nuevo_saldo is not None:
            print(f"Depósito exitoso de ${cantidad}. Nuevo saldo: ${self.cuenta.saldo}")
        else:
            print("Error: El monto a depositar debe ser positivo.")

    def salir(self):
        print("Seleccionó salir. Gracias por usar Bancomer.")

    def opciones(self):
        while True:
            print("\nSeleccione una opción:")
            print("1) Retirar")
            print("2) Depositar")
            print("3) Salir")

            opcion = input("¿Qué acción desea realizar? ")
            if opcion == "1":
                self.retirar()
            elif opcion == "2":
                self.depositar()
            elif opcion == "3":
                self.salir()
                break
            else:
                print("Opción inválida. Intente de nuevo.")


            
