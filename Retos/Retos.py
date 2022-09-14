'''
Cree una función que reciba una matriz(i.e., lista de listas) de tamaño nxm que contiene una
"x"(objetivo) y ">" como una flecha hacia esa dirección. La función debe retornar True si la
flecha va dirigida hacia el blanco. Retorna False si la flecha no va en dirección al blanco.
'''
import numpy as np

m=[" ",">"," ","x"]
tiro=[[" "," "," "," "],
        [" ",">"," ","x"],
        [" "," "," "," "]]

def es_tiro_al_blanco(matrix):
    index=np.where(matrix == "x")
    print(index)
    for elem in matrix:
        print(elem)




es_tiro_al_blanco(m)