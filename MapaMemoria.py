# Proyecto Final - Compiladores
# Autores: Carmelo Ramirez (A01175987) y Juan Pablo Galaz (A01251406)
# Mapa de memoria de el compilador

import sys

class MapaMemoria:
    def __init__(self, dirBase, entero, flotante, tmp, ptr, cte):
        self.gI = dirBase
        self.gF = self.gI + entero
        self.gCI = self.gF + flotante
        self.gCF = self.gCI + cte
        self.lI = self.gCF + cte
        self.lF = self.lI + entero
        self.lTI = self.lF + flotante
        self.lTF = self.lTI + entero
        self.lPI = self.lTF + flotante
        self.lPF = self.lPI + ptr
        self.lim = self.lPF + ptr

        #Mapa de Memoria
        self.mapa_memoria = {
            self.gI : [],
            self.gF : [],
            self.gCI : [],
            self.gCF : [],
            self.lI : [],
            self.lF : [],
            self.lTI : [],
            self.lTF : [],
            self.lPI : [],
            self.lPF : []
        }

    def expand(self, context, index):
        length = len(self.mapa_memoria[context])
        n = index - length + 1
        if n > 0:
            self.mapa_memoria[context].extend([0] * n)
    
    def find(self, direccion):
        val = None
        if type(direccion) is str:
            # deref de apuntador
            direccion = self.find(int(direccion[1:]))
        if direccion < self.gF:
            # globalInt
            self.expand(self.gI, direccion - self.gI)
            val = self.mapa_memoria[self.gI][direccion - self.gI]
        elif direccion < self.gCI:
            # globalFloat
            self.expand(self.gF, direccion - self.gF)
            val = self.mapa_memoria[self.gF][direccion - self.gF]
        elif direccion < self.gCF:
            # globalConstInt
            self.expand(self.gCI, direccion - self.gCI)
            val = self.mapa_memoria[self.gCI][direccion - self.gCI]
        elif direccion < self.lI:
            # globalConstFloat
            self.expand(self.gCF, direccion - self.gCF)
            val = self.mapa_memoria[self.gCF][direccion - self.gCF]
        elif direccion < self.lF:
            # localInt
            self.expand(self.lI, direccion - self.lI)
            val = self.mapa_memoria[self.lI][direccion - self.lI]
        elif direccion < self.lTI:
            # localFloat
            self.expand(self.lF, direccion - self.lF)
            val = self.mapa_memoria[self.lF][direccion - self.lF]
        elif direccion < self.lTF:
            # localTempInt
            self.expand(self.lTI, direccion - self.lTI)
            val = self.mapa_memoria[self.lTI][direccion - self.lTI]
        elif direccion < self.lPI:
            # localTempFloat
            self.expand(self.lTF, direccion - self.lTF)
            val = self.mapa_memoria[self.lTF][direccion - self.lTF]
        elif direccion < self.lPF:
            # localPtrInt
            self.expand(self.lPI, direccion - self.lPI)
            val = self.mapa_memoria[self.lPI][direccion - self.lPI]
        elif direccion < self.lim:
            # localPtrFloat
            self.expand(self.lPF, direccion - self.lPF)
            val = self.mapa_memoria[self.lPF][direccion - self.lPF]
        else:
            # error
            print("Memory Error")
            sys.exit()
        return val

    def insert(self, direccion, variable):
        if direccion < self.gF:
            # globalInt
            self.expand(self.gI, direccion - self.gI)
            self.mapa_memoria[self.gI][direccion - self.gI] = variable
        elif direccion < self.gCI:
            # globalFloat
            self.expand(self.gF, direccion - self.gF)
            self.mapa_memoria[self.gF][direccion - self.gF] = variable
        elif direccion < self.gCF:
            # globalConstInt
            self.expand(self.gCI, direccion - self.gCI)
            self.mapa_memoria[self.gCI][direccion - self.gCI] = variable
        elif direccion < self.lI:
            # globalConstFloat
            self.expand(self.gCF, direccion - self.gCF)
            self.mapa_memoria[self.gCF][direccion - self.gCF] = variable
        elif direccion < self.lF:
            # localInt
            self.expand(self.lI, direccion - self.lI)
            self.mapa_memoria[self.lI][direccion - self.lI] = variable
        elif direccion < self.lTI:
            # localFloat
            self.expand(self.lF, direccion - self.lF)
            self.mapa_memoria[self.lF][direccion - self.lF] = variable
        elif direccion < self.lTF:
            # localTempInt
            self.expand(self.lTI, direccion - self.lTI)
            self.mapa_memoria[self.lTI][direccion - self.lTI] = variable
        elif direccion < self.lPI:
            # localTempFloat
            self.expand(self.lTF, direccion - self.lTF)
            self.mapa_memoria[self.lTF][direccion - self.lTF] = variable
        elif direccion < self.lPF:
            # localPtrInt
            self.expand(self.lPI, direccion - self.lPI)
            self.mapa_memoria[self.lPI][direccion - self.lPI] = variable
        elif direccion < self.lim:
            # localPtrFloat
            self.expand(self.lPF, direccion - self.lPF)
            self.mapa_memoria[self.lPF][direccion - self.lPF] = variable
        else:
            # error
            print("Memory Error")
            sys.exit()
