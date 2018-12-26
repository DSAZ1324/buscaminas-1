# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 21:38:55 2018
@author: enaut.genua
"""
import time
from casilla import Casilla
from casilla import numero
from casilla import mina
from Tablero import Tablero
matr = []
def levantar(matr, posx, posy):
        for i in range(max(posx-1, 0), min(posx+2, len(matr))):
            for j in range(max(posy-1, 0), min(posy+2, len(matr[0]))):
                if Casilla.get_val(matr[i][j]) == 0:
                    matr[i][j] = Casilla.set_lev(True)
        return matr
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
    print((int(x) + 1) * "-+-")
    print("  |",end="")
    for i in range(int(x)):
        print(f" {i + 1}|", end="")
    print("\n" + (int(x) + 1) * "-+-")
    for i in range(int(x)):
        print(f" {i + 1}|", end="")
        for j in range(int(y)):
            if Casilla.get_lev(lista[i][j]) == True:
                if Casilla.get_val(lista[i][j]) == 0:
                    lista[i][j] = numero(i, j)
                    cant_de_minas = numero(i, j).analizar_minas(lista)
                    if cant_de_minas == 0:
                        print("  |", end="")
                    else:
                        print(f" {cant_de_minas}|", end="")
                else:
                    print(" X|", end = "")
                    se_ha_acabado_el_juego = True   
            else:
                print("  |", end="")
        print()        
    return se_ha_acabado_el_juego
dim = str(input("Introduzca las dimensiones de tu tablero (filas,columnas): "))
(x, y) = dim.split(",")
matr = Tablero(x, y)
matr = Tablero.crear_tab(matr)
matr = table(matr, x, y)
matr = crear_minas_numeros(matr, x, y)
actualizar_y_dibujar_tablero(matr, x, y)