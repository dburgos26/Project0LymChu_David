# Constantes

Variables = []
Orientaciones = ["left", "right", "around"]
Cardinalidades = ["north", "south", "east", "west"]
Objetos = ["balloons", "chips"]
Direcciones = ["up", "right", "left", "down","front","back"]


# Estructuras

Condicionales = { "facing-p" : [Cardinalidades], "can-put-p" : [Objetos, "int"], "can-pick-p" : [Objetos, "int"], "can-move-p" : [Cardinalidades], "not": "CasoEspecialCond"}

Metodos = {"defvar" : ["str", "int"], "=": ["int", "int"], "move" : ["int"], "turn" : [Orientaciones], "face" : [Cardinalidades], "put" : [Objetos, "int"], "pick" : [Objetos, "int"],
                "move-dir" : ["int" , Direcciones], "run-dirs" : ["listaDirec"], "move-face" : ["int", Cardinalidades], "Skip" : [], "if" : [Condicionales, "CasoEspecial", "CasoEspecial"],
                "loop" : [Condicionales, "CasoEspecial"], "repeat" : ["int", "CasoEspecial"], "defun" : ["str", "listaStr", "CasoEspecial"]
                }

MetodosCreados = {}

# Casos especiales
# int - numero o variable, CasoEspecialCond - Revisar otra vez condicion, str - Texto, listaDirec una lista de Direcciones, CasoEspecial - Revisar otra vez como metodo, listaStr - Lista de str,


# Contadoressss

contParentesis = 0
error = False

# Funciones

def añadirParentesis(texto):
    global contParentesis
    global error

    

    if texto == "(":
        contParentesis += 1
    elif texto == ")":
        contParentesis -= 1

    if contParentesis < 0:
        error = True
        print("error parentesis")



def revisarLinea(linea):

    global error

    buscando = None # Tipo de var que deberia ser 
    comandos = None # lista de los parametros
    contador = 0
    creandoVar = False

    for elemento in linea: 

        print("elemento : "+str(elemento))

        
        
        if buscando != None:# Revisar los argumentos
            
            if type(buscando) != str : # si no es un caso especial
                if elemento not in buscando:
                    error = True
                    print("error en type(buscando) != str")
                    print("no se encontro el metodo")
                    print("buscando :" + str(buscando))
                    print("comandos :" + str(comandos))
                    print("tipo del elemento = "+str(type(elemento)))
                    print("tipo delbuscando  = "+str(type(buscando)))


            else: # casos especiales

                if buscando == "str":

                    if type(elemento) != str:
                        error = True
                        print("error en type(elemento) != str")
                    if creandoVar:
                        Variables.append(elemento)
                        creandoVar = False

                if buscando == "int": 
                    
                    try:
                        int(elemento)
                        
                    except:
                        if buscando not in Variables:
                            error = True
                            print("error en buscando not in Variables")


                    

                if buscando == "listaDirec": 
                    for x in range(len(linea) - 1):
                        comandos.append(Direcciones)
                
                if buscando == "listaStr": 
                    for x in range(len(linea) - 2):
                        comandos.insert( 1,"str")

                if buscando == "CasoEspecialCond":
                    comandos.append(Condicionales)

                if buscando == "CasoEspecial":
                    print("elemento 112"+str(elemento))
                    if elemento in Metodos.keys() or elemento in MetodosCreados.keys():
                        listaMom = Metodos[elemento]
                        for x in range(len(listaMom)):
                            comandos.insert(x+contador, listaMom[x])
                    else:
                        error = True
                        print("error en CasoEspecial")
                        



        if buscando == None: # Revisar que el metodo existe
            
            if elemento in Metodos.keys() or elemento in MetodosCreados.keys():
                
                comandos = Metodos[elemento]
                

                if elemento == "defvar":
                    creandoVar = True
                    


        contador += 1
        try:
            print("contador = "+str(contador))
            print((comandos))
            if comandos != None:
                if contador <= len(comandos):
                    buscando = comandos[contador-1]

        except:
            error = True # Exceso de parametros
            print("error en Exceso de parametross")

        print("se realizo un ciclo")    
            

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
    print("============================================================================")
    print("se leyo una liena ")
    print("============================================================================")
    
archivo.close()

# =========================================== Ciclo principal ===========================================

if contParentesis != 0: # Contador de parentesis
    print("error en parentesis")
    error = True


if error: # Print final
    print("Se encontro un error")
else:
    print("No se encontraron errores")