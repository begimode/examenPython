import csv

def read_data(filename):
    """ Lee el fichero csv y devuelve un diccionario con el formato que aparece a continuacion (un objeto).
    A modo de ejemplo, se muestra como debera devolver la onformacion de la primera muestra del fichero (primera fila),
    siendo dato1 una clave que se ira incrementando. Si hay alguna muestra vacia, no debera aparecer en el fichero devuelto.
    Si el fichero tiene menos de 10 lineas con valor en todos los atributos se emitira un error de tipo ValueError. """

    with open(filename, newline='') as archivo:
    # reader = csv.reader(csvfile)
        lector_csv = csv.reader(archivo)
        objetos = {}
        i = 0

        for linea in lector_csv:
            #     # Si la línea está vacía, la saltamos
            if not any(linea):
                continue
            
            # Creamos un diccionario con los datos de la línea
            objeto = {
                'type': linea[0],
                'fixed acidity': linea[1],
                'volatile acidity': linea[2],
                'citric acid': linea[3],
                'residual sugar': linea[4],
                'chlorides': linea[5],
                'free sulfur dioxide': linea[6],
                'total sulfur dioxide': linea[7],
                'density': linea[8],
                'PH': linea[9],
                'sulphates': linea[10],
                'alcohol': linea[11],
                'quality': linea[12]
            }
            objetos[f'dato{i}'] = objeto
            i += 1

        # Si la lista de objetos tiene menos de 10 elementos, lanzar una excepción
        if len(objetos) < 10:
            raise ValueError('El atributo tiene menos de 10 filas')
        
        return objetos



def split (diccionario):
    """ Una funcion 'split' que recibe un diccionario como el que devuelve el ejercicio anterior
      y devuelve dos diccionarios. El primero es un diccionario con las muestras 
      que tengan el valor "white" en el atributo "type" y el segundo es un diccionario con 
      los datos que tengan el valor "red" en este atributo. El atributo "type" se eliminara 
      de cada dato en estos diccionarios devueltos.  """
    
    diccionariowhite ={}
    diccionariored = {}
    i=0
    # Ahora recorremos un for para poner los datos en los diccionarios
    for atributo in  diccionario.items():
        tipo = atributo.pop('type', None)
        if tipo == "white":
            diccionariowhite[i] == atributo
        elif tipo == "red":
            diccionariored[i] == atributo
        i += 1
    return diccionariored, diccionariowhite



def reduce(diccionario, atributo):
    """ Crea una funcion 'reduce' que reciba un diccionario con el dormato de los que devuelve 
    el ejercicio anterior y u string que corresponde al nombre de un atributo. Esta funcion 
    devuelve una lista con los valores de ese atributo. Si el atributo que se le pasa no existe en el diccionario,
    se emitira un error de tipo ValueError. A modo de ejemplo, si le pasamos un diccionario
    con los datos que son de tipo '"white" y con el atributo "alcohol", la lista devuelta 
    tendra los numeros de este atributo"""

    valores = []
    for objeto in diccionario.values():
        if atributo in objeto:
            valores.append(objeto[atributo])
        else:
            raise ValueError(f"El atributo '{atributo}' no existe en el diccionario")
    return valores


