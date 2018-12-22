#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 21:49:00 2018

@author: enaut
"""
from casilla import Casilla
from Tablero import Tablero

matr = []
def dibujar_tabl(matr, x, y):
    for i in range(int(x)):
        for j in range(int(y)):
            return Casilla.get_val(matr[i][j])
        
dim = str(input("Introduzca las dimensiones de tu tablero (filas, columnas): "))
(x, y) = dim.split(",")
matr = Tablero(x, y)
matr = Tablero.crear_tab(matr)
print(dibujar_tabl(matr,x,y))


            
    