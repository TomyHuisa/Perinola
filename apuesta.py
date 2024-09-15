class Apuesta:
    def __init__(self): #init: iniciar todo el equipo que definiste#
        self.fichas = 0 #self: representa el objeto, como fichas en este caso# 

    def __repr__(self):
        return f"Apuesta: {self.fichas} fichas"
    
    def ponerFicha(self, cuantas=1):
        self.fichas = self.fichas + cuantas

    def tomarFicha(self, cuantas=1):
        if self.fichas < cuantas:
            raise ValueError("No hay suficientes fichas para retirar") #raise: Reclamo del error, estas reclamando ese error#
        self.fichas = self.fichas - cuantas

    def tomarTodas(self):
        cantidad = self.fichas
        self.fichas = 0
        return cantidad

    def tieneFicha(self, cuantas=1):
        return self.fichas == self.fichas > cuantas

    def estaVacia(self):
        return self.fichas == 0
