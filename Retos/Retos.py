#IMPORTACION DE LIBRERIAS AUXILIARES
import numpy as np
def es_tiro_al_blanco():
        #INICIO E INGRESO DEL TAMAÑO DE MATRIZ
        print("********** RETO 1 (TIRO AL BLANCO) **********\n")
        filas=int(input("Digite la cantidad de filas de la matriz: "))
        colum=int(input("Digite la cantidad de columnas de la matriz: "))
        #CREACION DE MATRIZ DE MANERA RAPIDA
        print("\nNOTA: Por favor ingresar la 'x' del objetivo en mayuscula\n")
        matriz=np.empty((filas,colum),dtype=str)
        for f in range(filas):
                for c in range(colum):
                        matriz[f][c]=str(input(f"Ingrese el valor de la ubicacion {f},{c}: ".format(f+1,c+1)))
        print("\n***** REPRESENTACIÓN GRAFICA *****\n",matriz)
        #ANALISIS DE UBICACION DE LA FLECHA Y DEL OBJETIVO
        for f in range(filas):
                for c in range(colum):
                        if matriz[f][c]==">":
                                filaFlecha = f
                                colFlecha = c
                        if matriz[f][c]=="X":
                                filaObj = f
                                colObj = c
        #TOMA DE DECISION DEPENDIENDO DE LA UBICACION DE LA FLECHA Y OBJETIVO
        if((filaFlecha == filaObj)and(colObj>colFlecha)):
                print("\n¡¡¡¡¡ RESULTADO !!!!!\n",True)
        else:
                print("\n¡¡¡¡¡ RESULTADO !!!!!\n",False)

#es_tiro_al_blanco()

def sumar_diagonales():
        print("\nNOTA: Por favor ingresar una matriz cuadrada\n")
        filas=int(input("Digite la cantidad de filas de la matriz: "))
        colum=int(input("Digite la cantidad de columnas de la matriz: "))
        #CREACION DE MATRIZ DE MANERA RAPIDA

        matriz=np.empty((filas,colum),dtype=int)
        for f in range(filas):
                for c in range(colum):
                        matriz[f][c]=int(input(f"Ingrese el valor de la ubicacion {f},{c}: ".format(f+1,c+1)))
        d1=0
        for f in range(filas):
                for c in range(colum):
                        if c==f:
                                num=matriz[f][c]
                                d1=d1+num
        print("Suma diagonal 1: ",d1)

        for f in range(filas):
                for c in range(colum):
                        print(matriz[f][(colum-1)-f])


sumar_diagonales()