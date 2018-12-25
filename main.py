# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 21:38:55 2018

@author: caper
"""
from casilla import Casilla
from casilla import numero
from casilla import mina
from tablero import Tablero
matr = []
def crear_minas_numeros(matr, x, y):
    for i in range(int(x)):
        for j in range(int(y)):
            if matr[i][j] == 1:
                matr[i][j] = mina(i, j)
            else:
                matr[i][j] = numero(i, j)
    return matr
def table(matr, x, y):
    lista = []
    listaux = []
    for i in range(int(x)):
        for j in range(int(y)):
            if len(listaux) < int(y):
                listaux.append(Casilla(i, j).get_val())
        lista.append(listaux)
        listaux = []
    return lista
def actualizar_y_dibujar_tablero(lista, x, y):
    
    for i in range(int(x)):
        for j in range(int(y)):
            if Casilla.get_val(lista[i][j]) == 0:
                lista[i][j] = numero(i, j)
                cant_de_minas = numero(i, j).analizar_minas(lista)
            
    matr_dib=""
    for i in range(int(x)):
        for j in range(int(y)):
            matr_dib+=str(matr[i][j])+'\t'
        print (matr_dib)
        matr_dib=""
            
    


    
dim = str(input("Introduzca las dimensiones de tu tablero (filas,columnas): "))
(x, y) = dim.split(",")
matr = Tablero(x, y)
matr = Tablero.crear_tab(matr)
matr = table(matr, x, y)
matr = crear_minas_numeros(matr, x, y)
actualizar_y_dibujar_tablero(matr, x, y)

a=""
for i in range (int(x)):
    for j in range (int(y)):
        a+=str(matr[i][j])+'\t'
    print (a)
    a=""
        
