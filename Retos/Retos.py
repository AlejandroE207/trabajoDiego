#IMPORTACION DE LIBRERIAS AUXILIARES
import numpy as np
import math
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

        print("\n***** REPRESENTACION GRAFICA *****\n",matriz,"\n")
        d1=0
        d2=0
        for f in range(filas):
                for c in range(colum):
                        if c==f:
                                numD1=matriz[f][c]
                                d1=d1+numD1
        print("Suma de la diagonal 1: ",d1)

        for f in range(filas):
                numD2=(matriz[f][(colum-1)-f])
                d2=d2+numD2

        print("Suma de la diagonal 2: ",d2)
        s=d1+d2
        print("\nLa suma de ambas diagonales es: ",s)


#sumar_diagonales()

class Esfera:
        radio=0
        masa=0
        def __init__(self, radio=0, masa=0):
                self.radio=radio
                self.masa=masa
                self.volumen = 0
                self.superficie =0
                self.densidad=0
        def get_radio(self):
               # return "El radio de la esfera es: ",self.radio
                return "El radio de la esfera es: {}".format(self.radio)
                
        def get_masa(self):
                return "La masa de la esfera es: {}".format(self.masa)

        def get_volumen(self):
                self.volumen=(4/3)*math.pi*(self.radio**3)
                return "El volumen de la esfera es: {}".format(round(self.volumen,2))

        def get_area_superficie(self):
                self.superficie=4*math.pi*(self.radio**2)
                return "La superficie de la esfera es: {}".format(round(self.superficie,2))

        def get_densidad(self):
                self.densidad = self.masa/self.volumen
                return "La densidad de la esfera es: {}".format(round(self.densidad,2))

def crearEsfera():
        print("***** CREACION DE ESFERA*****")
        v=float(input("Digite el volumen de la esfera: "))
        m=float(input("Digite la masa de la esfera: "))
        e1=Esfera(v,m)
        print("\n+++ INFORMACION DE LA ESFERA +++")
        print(e1.get_radio())
        print(e1.get_masa())
        print(e1.get_volumen())
        print(e1.get_area_superficie())
        print(e1.get_densidad())

crearEsfera()



