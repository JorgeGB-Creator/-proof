import random
import string

# Función para generar contraseñas aleatorias con diferentes opciones de caracteres


def generar_contraseña(tamaño=12, mayusculas=True, numeros=True, especiales=True):
    caracteres = string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if especiales:
        caracteres += string.punctuation

    contraseña_generada = ''.join(random.choice(caracteres)
                                  for _ in range(tamaño))
    return contraseña_generada


if __name__ == "__main__":
    longitud = int(input("Longitud de la contraseña: "))
    incluir_mayus = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    incluir_especiales = input("¿Incluir especíales? (s/n): ").lower() == 's'

    contraseña_final = generar_contraseña(
        longitud, incluir_mayus, incluir_numeros, incluir_especiales)
    print(f"Contraseña generada: {contraseña_final}")
