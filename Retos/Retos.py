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
        #For por si se dijita la x en minuscula
        for f in range(filas):
                for c in range(colum):
                        matriz[f][c]=matriz[f][c].upper()
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

es_tiro_al_blanco()

#INICIO DE RETO 2, DECLARACION DE FUNCION
def sumar_diagonales():
        print("\n********** RETO 2 (SUMA DIAGONALES) **********\n")
        print("\nNOTA: Por favor ingresar una matriz cuadrada\n")
        filas=int(input("Digite la cantidad de filas de la matriz: "))
        colum=int(input("Digite la cantidad de columnas de la matriz: "))
        
        #CREACION DE MATRIZ DE MANERA RAPIDA
        matriz=np.empty((filas,colum),dtype=int)
        for f in range(filas):
                for c in range(colum):
                        matriz[f][c]=int(input(f"Ingrese el valor de la ubicacion {f},{c}: ".format(f+1,c+1)))
        #IMPRESION DE LA MATRIZ GENERANDO LA REPRESENTACION GRAFICA
        print("\n***** REPRESENTACION GRAFICA *****\n",matriz,"\n")
        d1=0
        d2=0
        #FOR PARA REALIZAR SUMA DE LA PRIMERA DIAGONAL
        for f in range(filas):
                for c in range(colum):
                        if c==f:
                                numD1=matriz[f][c]
                                d1=d1+numD1
        print("Suma de la diagonal 1: ",d1)
        #FOR PARA REALIZAR SUMA DE LA SEGUNDA DIAGONAL (DIAGONAL INVERTIDA)
        for f in range(filas):
                numD2=(matriz[f][(colum-1)-f])
                d2=d2+numD2

        print("Suma de la diagonal 2: ",d2)
        s=d1+d2
        #SUMA TOTAL
        print("\nLa suma de ambas diagonales es: ",s)

sumar_diagonales()#LLAMADO DE FUNCION

print("\n********** RETO 3 (ESFERA Y SUS CALCULOS) **********\n")
class Esfera: #DECLARARION DE CLASE
        #ATRIBUTOS
        radio=0
        masa=0
        def __init__(self, radio=0, masa=0): #METOODO CONSTRUCTOR PRINCIPAL MAIN
                self.radio=radio
                self.masa=masa
                self.volumen = 0
                self.superficie =0
                self.densidad=0
        def get_radio(self): #METODO DE PARA OBTENER RADIO
               # return "El radio de la esfera es: ",self.radio
                return "El radio de la esfera es: {}".format(self.radio)
                
        def get_masa(self): #METODO PARA OBTENER MASA
                return "La masa de la esfera es: {}".format(self.masa)

        def get_volumen(self): #METODO PARA OBTENER VOLUMEN
                self.volumen=(4/3)*math.pi*(self.radio**3)
                return "El volumen de la esfera es: {}".format(round(self.volumen,2))

        def get_area_superficie(self): #METODO PARA OBTENER SUPERFICIE
                self.superficie=4*math.pi*(self.radio**2)
                return "La superficie de la esfera es: {}".format(round(self.superficie,2))

        def get_densidad(self): #METODO PARA OBTENER DENSIDAD
                self.densidad = self.masa/self.volumen
                return "La densidad de la esfera es: {}".format(round(self.densidad,2))
#FUNCION DE CREACION DE ESFERA QUE SE CONECTA CON LA CLASE 
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

crearEsfera() #LLAMADO DE FUNCION

print("\n********** RETO 4 (CREACION E INTERACCIÓN QUARKS) **********\n")
class Quark: #DECLARACION DE CLASE
        #ATRIBUTOS
        color=""
        sabor=""
        numero_baryon=1/3
        #METODO CONSTRUCTOR PRICIPAL MAIN
        def __init__(self,color,sabor):
                self.color = color
                self.sabor=sabor
        #METODO DE INTERACCION Y CAMBIO DE COLOR DE LOS QUARK´S
        def interactuar(self,quark):
                colAux = quark.color
                quark.color= self.color
                self.color = colAux

#CREACION DE FUNCION PARA CREACION DE QUARKS 
def crear_interatuar_quark():
        print("+++++ CREACION DE QUARKS +++++\n")
        print("Tipos de colores: 'rojo', 'azul' y 'verde'")
        print("Tipos de sabores: 'up', 'down', 'strange', 'charm', 'top' y 'bottom'\n")
        #LEECTURA DE COLOR Y SABOR PARA CREAR QUARKS
        col1=str(input("¿Qué color tendra el quark #1 (q1): "))
        sab1 = str(input("¿Qué color tendra el quar #1 (q1): "))
        #SI ESCRIBEN UN DATO EN MAYUSCULA O MEZCLA DE MAYUSCULA, SE PASA A MINUSCULA (MEJOR PROCESAMIENTO)
        col1=col1.lower()
        sab1=sab1.lower()
        col2=str(input("¿Qué color tendra el quark #2 (q2): "))
        sab2 = str(input("¿Qué color tendra el quar #2 (q2): "))
        col2=col2.lower()
        sab2=sab2.lower()
        #CREACION DE QUARKS CON LOS DATOS ANTERIORMENTE LEIDO
        q1=Quark(col1,sab1)
        q2=Quark(col2,sab2)
        #IMPRESION DE INFORMACION DE LOS QUARKS
        print("\n/// INFORMACION DE LOS QUARKS ///")
        print("q1:\nSu color es {} \nSu sabor es: {}\nSu numero baryon es: {}\n".format(q1.color,q1.sabor,q1.numero_baryon))
        print("q2:\nSu color es {} \nSu sabor es: {}\nSu numero baryon es: {}".format(q2.color,q2.sabor,q2.numero_baryon))
        #PREGUNTA POR SI SE DESEA QUE INTERACTUEN LOS QUARKS O NO
        preg=str(input("¿Desea que los quarks interactuen? (si/no): "))
        preg=preg.lower()
        if preg == "si":
                q1.interactuar(q2)
                print("\nHAN CAMBIADO DE COLOR!!")
                print("q1:\nSu color es: {}".format(q1.color))
                print("q2:\nSu color es: {}".format(q2.color))
        else:
                print("FIN...")
        
crear_interatuar_quark() #LLAMADO DE FUNCION.

        
