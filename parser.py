# Constantes

Variables = []
Orientaciones = ["left", "right", "around"]
Cardinalidades = ["north", "south", "east", "west"]
Objetos = ["Balloons", "Chips"]
Direcciones = ["front", "right", "left", "back"]


# Estructuras

Condicionales = { "facing-p" : [Direcciones], "can-put-p" : [Objetos, "int"], "can-pick-p" : [Objetos, "int"], "can-move-p" : [Cardinalidades], "not": "CasoEspecialCond"}

Metodos = {"defvar" : ["str", "int"], "=": ["str", "int"], "move" : ["int"], "turn" : [Orientaciones], "face" : [Cardinalidades], "put" : [Objetos, "int"], "pick" : [Objetos, "int"],
                "move-dir" : ["int" , Direcciones], "run-dirs" : ["listaDirec"], "move-face" : ["int", Cardinalidades], "Skip" : [], "if" : [Condicionales, "CasoEspecial", "CasoEspecial"],
                "loop" : [Condicionales, "CasoEspecial"], "repeat" : ["int", "CasoEspecial"], "defun" : ["str", "listaStr", "CasoEspecial"]
                }

MetodosCreados = {}

# Casos especiales
# int - numero o variable, CasoEspecialCond - Revisar otra vez condicion, str - Texto, listaDirec una lista de Direcciones, CasoEspecial - Revisar otra vez como metodo, listaStr - Lista de str


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


def revisarLinea(linea):

    buscando = None # Tipo de var que deberia ser 
    comandos = None # lista de los parametros
    contador = 0

    for x in linea:
        
        if buscando == None: # Revisar que el metodo existe
            
            if Metodos.key(x) != None or MetodosCreados.key(x) != None:
                
                comandos = metodos[x]
                buscando = comandos[contador]
        
        if buscando != None:# Revisar los argumentos
            
            if type(buscando) != "str": # si no es un caso especial
                if x not in buscando:
                    error = True
            else:
                a
                # explicar cada caso especial

            contador += 1
            buscando = comandos[contador] # out of range
            

    return None

# funcion de revision general, caso especial - iniciar otra vez el analisis


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

    revisarLinea(linea)

    linea = archivo.readline()
    
archivo.close()

# =========================================== Ciclo principal ===========================================

if error:
    print("Se encontro un error")
else:
    print("No se encontraron errores")