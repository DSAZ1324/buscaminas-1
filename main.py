#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 21:49:00 2018
@author: enaut
"""
from casilla import Casilla
from casilla import numero
from casilla import mina
from Tablero import Tablero
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
            if lista[i][j] != 1:
                if numero.get_lev(lista[i][j]):
                    None
dim = str(input("Introduzca las dimensiones de tu tablero (filas,columnas): "))
(x, y) = dim.split(",")
matr = Tablero(x, y)
matr = Tablero.crear_tab(matr)
matr = table(matr, x, y)
matr = crear_minas_numeros(matr, x, y)
print(matr)