#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:52:17 2018

@author: carlos.perez.cabot
"""
from casilla import Casilla
class numero(Casilla):
    def __init__(self):
        Casilla().__init__(self, posx, posy)
        self.contador=int(0)
    def analizar_minas(self, matr):
        for dimx in range(self.x-1, self.x+1):
                for dimy in range(self.y-1, self.y+1):
                    if Casilla.get_val == 1:
                        self.contador+=1
    def get_valor(self):
        return self.contador       