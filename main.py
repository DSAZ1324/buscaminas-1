#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 21:49:00 2018

@author: enaut
"""
from casilla import Casilla
from casilla import numero
from Tablero import Tablero
matr = []
def tablero(matr, x, y):
    lista = []
    listaux = []
    for i in range(int(x)):
        for j in range(int(y)):
            if len(listaux) < int(y):
                listaux.append(Casilla(i, j).get_val())
        lista.append(listaux)
        listaux = []
    return lista

def actualizar_y_dibujar_tablero(matrusable):
    None
    
dim = str(input("Introduzca las dimensiones de tu tablero (filas,columnas): "))
(x, y) = dim.split(",")
matr = Tablero(x, y)
matr = Tablero.crear_tab(matr)
a = tablero(matr, x, y)
print(a)
print(tablero(matr, x, y))




            
    