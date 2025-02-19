class Cuenta:
    def __init__(self,valor,tipo,nombre):
        self.saldo= valor
        self.tipo= tipo
        self.nombre= nombre
    def imprimirDetalles(self):
        print("Desde el metodo")
        print("saldo:",self.saldo)
        print("tipo:",self.tipo)
        print("nombre:",self.nombre)
    