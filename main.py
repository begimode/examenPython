from functions import *

def test(self, filename):
    filename = "winequality.csv"
    atributo = "alcohol"
    try:
        diccionario = read_data(filename)
        diccionarios = split(read_data(filename))
        reduce(diccionarios[1], atributo)

    except ValueError as err:
        print("Ha ocurrido la excepcion " + err)