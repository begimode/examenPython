from functions import *

def test():
    filename = "winequality.csv"
    atributo = "alcohol"
    try:
        diccionario = read_data(filename)
        diccionarios = split(read_data(filename))
        print(diccionarios)
        # print(reduce(diccionarios[1], atributo))

    except ValueError as err:
        print("Ha ocurrido la excepcion " + err)

test()