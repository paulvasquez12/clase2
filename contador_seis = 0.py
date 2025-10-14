
import random  # Asegúrate de importar random

contador_seis = 0 
for i in range(10):
    dado = random.randint(1,6)
    print(f"Lanzamiento {i+1}: {dado}")
    if dado == 6:
        contador_seis += 1

print(f"El número 6 salió {contador_seis} veces")
