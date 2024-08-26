from random import choice

class Perinola:
    caras = [0,1,2,3,4,5,6]
    def __init__(self):
        self.cara_visible = Perinola.caras[0]
    def __repr__(self):
        return f"Salio: {self.cara_visible}"
    def tirar(self):
        caras = ("Pon 1" , "Toma 2", "Todos Ponen",
                  "Toma 1", "Pon2", "Toma Todo")
        self.cara_visible = choice(caras)
        return self.cara_visible