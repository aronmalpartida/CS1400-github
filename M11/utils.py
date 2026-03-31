# utils.py

def limpiar_y_tokenizar(texto):
    
    limpio = texto.lower()
    limpio = limpio.replace(".", "").replace(",", "")
    palabras = limpio.split()
    
    return palabras