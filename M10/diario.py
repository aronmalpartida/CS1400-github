import datetime
# Paso 1: Crea una funcion que guarde opciones en tu menu.
def menu():
    print("\n--- Mi Diario ---")
    print("1. Escribir")
    print("2. Leer")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion

# Paso 2: Complete el While True agregando un if/elif/elif/else
while True:
    eleccion = menu()

    if eleccion == '1':
        pensamiento = input("\nEscribe tus pensamientos: ")
        
        # --- PREPARANDO LOS PUNTOS EXTRA ---
        # Obtenemos la fecha y hora actual
        fecha_actual = datetime.datetime.now()
        # Le damos un formato fácil de leer (Año-Mes-Día Hora:Minuto)
        fecha_formateada = fecha_actual.strftime("%Y-%m-%d %H:%M") 
        
        with open('mi_diario.txt', 'a') as archivo:
            # <-- ¡Punto extra 2: Agregamos el guion y la fecha formateada!
            # La "f" antes de las comillas nos permite meter variables entre llaves {}
            archivo.write(f"- {fecha_formateada}: {pensamiento}\n")
            
        print("¡Pensamiento guardado con éxito!")

    elif eleccion == '2':
        print("\n--- Leyendo tu Diario ---")
        try:
            # Abrimos en modo 'r' (read/leer)
            with open('mi_diario.txt', 'r') as archivo:
                print(archivo.read())
        except FileNotFoundError:
            # Esto evita que el programa falle si intentas leer antes de escribir algo
            print("Todavía no has escrito nada en tu diario.")

    elif eleccion == '3':
        print("\nSaliendo del diario...")
        break # Termina el ciclo while

    else:
        # Por si el usuario teclea algo que no es 1, 2 o 3
        print("\nOpción no válida. Por favor, intenta de nuevo.")
