# TODO: Paso 1. Importa el módulo 'random'.
print("Importando el módulo random...")
import random  

def lanzar_dado():

    """""
    Simula el lanzamiento de un dado de seis caras.

    No recibe parámetros.

    Returns:
      int: Un número entero aleatorio entre 1 y 6.
    """
    # TODO: Paso 2. Genera un número aleatorio entre 1 y 6.
    #Guardalo en una variable llamada 'resultado'.

    resultado = random.randint(1, 6)

    # TODO: Paso 3. Devuelve el resultado.
    return resultado


# --- Bloque para probar tu función ---
# Este código es para que pruebes tu función.
if _name_ == "_main_":
    print("Lanzando el dado 5 veces:")

    # Usamos un bucle para llamar a la función varias veces
    for i in range(5):
        resultado_lanzamiento = lanzar_dado()
        print(f"Lanzamiento {i + 1}: {resultado_lanzamiento}")