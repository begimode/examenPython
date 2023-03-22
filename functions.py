import csv
    

def read_data(filename):
    """ Lee el fichero csv y devuelve un diccionario con el formato que aparece a continuacion (un objeto).
    A modo de ejemplo, se muestra como debera devolver la onformacion de la primera muestra del fichero (primera fila),
    siendo dato1 una clave que se ira incrementando. Si hay alguna muestra vacia, no debera aparecer en el fichero devuelto.
    Si el fichero tiene menos de 10 lineas con valor en todos los atributos se emitira un error de tipo ValueError. """

    lector_csv = csv.reader(filename, delimiter=',')

    for fila in lector_csv:
        # Si hay valores vacíos en la fila, saltarla
        if not all(fila):
            continue

    atributo = 2    
    
    # Si la lista de objetos tiene menos de 10 elementos, lanzar una excepción
    if len(atributo) < 10:
        raise ValueError('El archivo no tiene suficientes filas')



def split (diccionario):
    diccionariowhite =[]
    diccionariored = []
    pos1, pos2, pos3 = 0
    if diccionario[pos1].type == "white":
        diccionariowhite[pos2] = diccionario[pos1]
        pos1 = pos1 + 1
        pos2 = pos2 + 1
    elif diccionario[pos1].type == "red":
        diccionariored[pos3] = diccionario[pos1]
        pos1 = pos1 + 1
        pos3 = pos3 + 1
    else :
        pos1 = pos1 + 1

    return diccionariored, diccionariowhite


