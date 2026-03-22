import datetime

def menu():
    print("\n--- Mi Diario ---")
    print("1. Escribir")
    print("2. Leer")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion

while True:
    eleccion = menu()

    if eleccion == '1':
        pensamiento = input("\nEscribe tus pensamientos: ")

        fecha_actual = datetime.datetime.now()
        fecha_formateada = fecha_actual.strftime("%Y-%m-%d %H:%M") 
        
        with open('mi_diario.txt', 'a') as archivo:
            archivo.write(f"- {fecha_formateada}: {pensamiento}\n")
            
        print("¡Pensamiento guardado con éxito!")

    elif eleccion == '2':
        print("\n--- Leyendo tu Diario ---")
        try:
            with open('mi_diario.txt', 'r') as archivo:
                print(archivo.read())
        except FileNotFoundError:
            print("Todavía no has escrito nada en tu diario.")

    elif eleccion == '3':
        print("\nSaliendo del diario...")
        break 
    else:
        print("\nOpción no válida. Por favor, intenta de nuevo.")
