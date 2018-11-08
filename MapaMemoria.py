# Proyecto Final - Compiladores
# Autores: Carmelo Ramirez (A01175987) y Juan Pablo Galaz (A01251406)
# Mapa de memoria de el compilador

import sys

class MapaMemoria:
    def __init__(self, dirBase, entero, flotante, tmp, ptr, cte):
        gI = dirBase
        gF = gI + entero
        gCI = gF + flotante
        gCF = gCI + cte
        lI = gCF + cte
        lF = lI + entero
        lTI = lF + flotante
        lTF = lTI + entero
        lPI = lTF + flotante
        lPF = lPI + ptr

        #Mapa de Memoria
        self.mapa_memoria = {
            gI : [],
            gf : [],
            gCI : [],
            gcF : [],
            lI : [],
            lF : [],
            lTI : [],
            lTF : [],
            lPI : [],
            lPF : []
        }

    def insertMapaMemoria(self, direccion, ctxt, variable) :
        if ctxt == 'globalInt':
            indice = direccion - self.gI
            self.mapa_memoria[self.gI].append(indice, variable)
        elif ctxt == 'globalFloat':
            indice = direccion - self.gF
            self.mapa_memoria[self.gF].append(indice, variable)
        elif ctxt == 'globalConstInt':
            indice = direccion - self.gCI
            self.mapa_memoria[self.gCI].append(indice, variable)
        elif ctxt == 'globalConstFloat':
            indice = direccion - self.gCF
            self.mapa_memoria[self.gCF].append(indice, variable)
        elif ctxt == 'localInt':
            indice = direccion - self.lI
            self.mapa_memoria[self.lI].append(indice, variable)
        elif ctxt == 'localFloat':
            indice = direccion - self.lF
            self.mapa_memoria[self.lF].append(indice, variable)
        elif ctxt == 'localTempInt':
            indice = direccion - self.lTI
            self.mapa_memoria[self.lTI].append(indice, variable)
        elif ctxt == 'localPtrInt':
            indice = direccion - self.lPI
            self.mapa_memoria[self.lPI].append(indice, variable)
        elif ctxt == 'localPtrFloat':
            indice = direccion - self.lPF
            self.mapa_memoria[self.lPF].append(indice, variable)
