import random
import string

# Función para generar contraseñas seguras


def generar_contraseña(tamaño=12, mayusculas=True, numeros=True, especiales=True, excluir_ambiguos=False):
    caracteres = string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if especiales:
        caracteres += string.punctuation

    # Excluir caracteres ambiguos si se solicita
    if excluir_ambiguos:
        caracteres = caracteres.translate(str.maketrans('', '', 'Il1O0'))

    contraseña_generada = ''.join(random.choice(caracteres)
                                  for _ in range(tamaño))
    return contraseña_generada


# Cálculo del área y perímetro de un rectángulo
def calcular_rectangulo():
    try:
        base = int(input("Proporciona la base del rectángulo: "))
        altura = int(input("Proporciona la altura del rectángulo: "))

        area = base * altura
        perimetro = 2 * (base + altura)

        print(f"\nÁrea del rectángulo: {area}")
        print(f"Perímetro del rectángulo: {perimetro}")

    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")


if __name__ == "__main__":
    # Solicitar datos para la contraseña
    while True:
        try:
            longitud = int(input("\nLongitud de la contraseña (mínimo 4): "))
            if longitud < 4:
                print("La longitud debe ser al menos 4.")
                continue
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    incluir_mayus = input(
        "¿Incluir mayúsculas? (s/n): ").strip().lower() == 's'
    incluir_numeros = input("¿Incluir números? (s/n): ").strip().lower() == 's'
    incluir_especiales = input(
        "¿Incluir caracteres especiales? (s/n): ").strip().lower() == 's'
    excluir_ambiguos = input(
        "¿Excluir caracteres ambiguos? (s/n): ").strip().lower() == 's'

    contraseña_final = generar_contraseña(
        longitud, incluir_mayus, incluir_numeros, incluir_especiales, excluir_ambiguos)
    print(f"\nContraseña generada: {contraseña_final}")

    # Cálculo del rectángulo
    calcular_rectangulo()
