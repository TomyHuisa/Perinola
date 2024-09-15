from perinola import Perinola
from apuesta import Apuesta

p = Perinola()
print(p)
print(p.cara_visible)
resultado= p.tirar()
print(resultado)
print(p)
print(p.cara_visible)
print("Perinola Arriba| Apuesta Abajo|")
a = Apuesta()
print(a)
a.ponerFicha(4)
print(a)
a.tomarFicha(8)
print(a)
a.tomarFicha()
print(a)

