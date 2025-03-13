class Menu:
    def __init__(self,mensaje):
        self.mensajeBienvenida= mensaje
        
    def Bienvenida(self):
        print(self.mensajeBienvenida)
        
    def Retirar(self):
        print("Seleccionó retirar dinero")
        
    def Depositar(self):
        print("Seleccionó depositar dinero")
        
    def Salir(self):
        print("Seleccionó salir")
        
    def Opciones(self):
        while True:
            print("\nSeleccione una opción")
            print("1)Retirar")
            print("2)Depositar")
            print("3)Salir")
            
            opcion= input("¿Qué acción desea realizar? ")
            if opcion== "1":
                self.Retirar()
            elif opcion== "2":
                self.Depositar()
            elif opcion== "3":
                self.Salir()
                break
            else:
                print("Opción inválida.")
            