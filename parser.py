# Constantes

Variables = []
Orientaciones = ["left", "right", "around"]
Cardinalidades = ["north", "south", "east", "west"]
Objetos = ["Balloons", "Chips"]
Direcciones = ["front", "right", "left", "back"]

# Estructuras

Condicionales = { "facing-p" : [Direcciones], "can-put-p" : [Objetos, "int"], "can-pick-p" : [Objetos, "int"], "can-move-p" : [Cardinalidades], "not": "CasoEspecial"}

Metodos = {}

MetodosCreados = {}

# Contadores

contParentesis = 0
error = False

# Funciones

def añadirParentesis(texto):

    if texto == "(":
        contParentesis += 1
    elif texto == ")":
        contParentesis -= 1

    if contParentesis < 0:
        error = True

# =========================================== Ciclo principal ===========================================

nomArchivo = input("Cual archivo quieres revisar")
archivo = open(nomArchivo, "r", encoding="utf-8")

linea = archivo.readline()

# Leer el archivo

while linea != "" and not error:

    # Contar Parentesis
    for x in linea:
        if x == "(" or x == ")":
            añadirParentesis(x)

    # Arreglar String

    linea = linea.replace("(", "")
    linea = linea.replace(")", "")
    linea = linea.replace(":", "")

    linea = linea.split()

    # Analisis por elemento

    linea = archivo.readline()
    
archivo.close()

# =========================================== Ciclo principal ===========================================

if error:
    print("Se encontro un error")
else:
    print("No se encontraron errores")