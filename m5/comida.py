print("bienvenida al programa de comidas de latinoamerica")
print("opciones : tacos , arepas, ceviche, pupusas, empanadas")
comida1= input("que comida quieres comer ?")
comida= comida1.lower()


if comida == "tacos": 
    print('los tacos son tipicos de mexico')
elif comida == "arepas" :
    print('las arepas son tipicos de venezuela')
elif comida == "ceviche" :
    print('el ceviche es tipico de Peru')
elif comida == "pupusas" : 
    print('las pupusas son tipicos de el guatemala ')
elif comida == "empanada" : 
    print('las empanadas son tipicos de colombia')
