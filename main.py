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
def contar_levantadas(matr):
    cant_levantables = 0
    levantados = 0
    for i in range(len(matr)):
        for j in range(len(matr[0])):
            if Casilla.get_val(matr[i][j]) == 0:
                cant_levantables += 1
    for i in range(len(matr)):
        for j in range(len(matr[0])):
            if Casilla.get_val(matr[i][j]) == 0 and Casilla.get_lev(matr[i][j]) == True:
                levantados += 1
    if cant_levantables == levantados:
        return True
    else:
        return False
def levantar_auto(matr):
        for i in range(len(matr)):
            for j in range(len(matr[0])):
                if Casilla.get_lev(matr[i][j]) == True:
                    if Casilla.get_val(matr[i][j]) == 0:
                        if numero(i, j).analizar_minas(matr) == 0:
                            for x in range(max(i-1, 0), min(i+2, len(matr))):
                                for y in range(max(j-1, 0), min(j+2, len(matr))):
                                    Casilla.set_lev(matr[x][y], True)
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
    print((int(y) + 1) * "-+-")
    print("  |",end="")
    for i in range(int(y)):
        if i >=10:
            print(f"{i}|", end="")
        else:
            print(f" {i}|", end="")
    print("\n" + (int(y) + 1) * "-+-")
    for i in range(int(x)):
        if i >=10:
            print(f"{i}|", end="")
        else:
            print(f" {i}|", end="")
        for j in range(int(y)):
            if Casilla.get_lev(lista[i][j]) == True:
                if Casilla.get_val(lista[i][j]) == 0:
                    cant_de_minas = numero(i, j).analizar_minas(lista)
                    if cant_de_minas == 0:
                        print("  |", end="")
                    else:
                        print(f" {cant_de_minas}|", end="")
                else:
                    print(" X|", end = "")
            else:
                print(" x|", end="")
        print()        
dim = str(input("Introduzca las dimensiones de tu tablero (filas,columnas): "))
(x, y) = dim.split(",")
matr = Tablero(x, y)
matr = Tablero.crear_tab(matr)
matr = table(matr, x, y)
matr = crear_minas_numeros(matr, x, y)
has_ganado = False
antes = int(round(time.time(), 0))
print("0h 0' 00\"")
actualizar_y_dibujar_tablero(matr, x, y)
try:
    while True:
        jugada = input("Tu jugada(fila,columna): ")
        (jx,jy) = jugada.split(",")
        if Casilla.get_lev(matr[int(jx)][int(jy)]) == False:
            if Casilla.get_val(matr[int(jx)][int(jy)]) == 1:
                break
            else:
                Casilla.set_lev(matr[int(jx)][int(jy)], True)
        else:
            print("Ya levantado... -.-")
        matr = levantar_auto(matr)
        has_ganado = contar_levantadas(matr)
        if has_ganado == True:
            break
        despues = int(round(time.time())) - antes
        m, s = divmod(despues, 60)
        h, m = divmod(m, 60)
        print ("%d:%02d:%02d" % (h, m, s))
        actualizar_y_dibujar_tablero(matr, x, y)
    if has_ganado == False:
        for i in range(len(matr)):
            for j in range(len(matr[0])):
                        if Casilla.get_lev(matr[i][j]) == False:
                            Casilla.set_lev(matr[i][j], True)
        actualizar_y_dibujar_tablero(matr, x, y)
        print("HAS PERDIDO")
    else:
        for i in range(len(matr)):
            for j in range(len(matr[0])):
                        if Casilla.get_lev(matr[i][j]) == False:
                            Casilla.set_lev(matr[i][j], True)
        actualizar_y_dibujar_tablero(matr, x, y)
        print("HAS GANADO")
except:
    print("Uups, creo que acabas de romperlo...")