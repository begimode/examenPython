def read_data(filename):
    """ Devuelve un diccionario con el formato que aparece a continuacion (un objeto).
    A modo de ejemplo, se muestra como debera devolver la onformacion de la primera muestra del fichero (primera fila),
    siendo dato1 una clave que se ira incrementando. Si hay alguna muestra vacia, no debera aparecer en el fichero devuelto.
    Si el fichero tiene menos de 10 lineas con valor en todos los atributos se emitira un error de tipo ValueError. """

    f=open(filename, mode="csv", encoding = "utf-8")
    linea = f.readline()
    vino = []
    while linea != "" :
        

