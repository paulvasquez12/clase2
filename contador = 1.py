#contador = 10 
#while contador >= 1:
  #  print(contador)
 #   contador = contador -1 
#print("despegue ¡¡¡¡" )

##suma = 0
#numero = 1 
#while numero <= 15:
  #  suma = suma + numero
 #   numero = numero + 1 
#print("suma es", suma )
import random

#def lanzar_dado():
   # return random.randint(1,6)
#def presentacion():
 #   print("Bienvenido al juego!!")
def lanzar_dos_dados():
    print(lanzar_dado())
    print(lanzar_dado())
presentacion()
lanzar_dado()
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
print("inicio")
print(fahrenheit_a_celsius (55))


def lanzar_dado():
    return random.randint (1,6)
print("lanzar dado")
lanzar_dado




  