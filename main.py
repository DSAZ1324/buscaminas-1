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
            print(matr[i[j]].get_val())
        
dim = str(input("Introduzca las dimensiones de tu tablero (x,y): "))
(x, y) = dim.split(",")
matr = Tablero(x, y)
matr = Tablero.crear_tab(matr)
#dibujar_tabl(matr,x,y)
print(matr)

            
    