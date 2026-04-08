#ELEGI LA OPCION B 
class DigiPet:
    def __init__(self, nombre):
        self.nombre = nombre
        self.felicidad = 100
        self.hambre = 100
        self.salud = 100
        self.vivo = True

    def pasartiempo(self):
        self.felicidad -= 10
        self.hambre -= 15
        self.salud -= 5
        self.verificar_estado()

    def alimentar(self):
        print(f"Has alimentado a {self.nombre}.")
        self.hambre += 20
        if self.hambre > 100: self.hambre = 100
        self.pasartiempo()

    def jugar(self):
        print(f"Jugaste con {self.nombre}!")
        self.felicidad += 20
        self.hambre -= 10
        self.verificar_estado()

 # MINITAREA CON IA crear el método pasear(), el cual reutiliza la lógica de 
 #modificar los atributos de salud y felicidad de la mascota.  

    def pasear(self):
        print(f"Sacaste a pasear a {self.nombre}. ¡Le encanta el aire libre!")
        self.salud += 15
        self.felicidad += 10
        self.hambre -= 20 
        if self.salud > 100: self.salud = 100
        self.verificar_estado()

    def verificar_estado(self):
        if self.felicidad <= 0 or self.hambre <= 0 or self.salud <= 0:
            self.vivo = False
            print(f"Oh no... {self.nombre} ha fallecido.")

mi_mascota = DigiPet("Dino")
# IA corregir errores  en el ciclo while y para implementar la
#funcionalidad de la mini-tarea: 
while mi_mascota.vivo:
    print(f"\nEstado de {mi_mascota.nombre}:")
    print(f"Felicidad: {mi_mascota.felicidad} | Comida: {mi_mascota.hambre} | Salud: {mi_mascota.salud}")
    print("1. Jugar | 2. Alimentar | 3. Pasear | 4. Salir")
    
    opcion = input("¿Qué te gustaría hacer hoy? ")
    
    if opcion == "1":
        mi_mascota.jugar()
    elif opcion == "2":
        mi_mascota.alimentar()
    elif opcion == "3":
        mi_mascota.pasear()
    elif opcion == "4":
        break