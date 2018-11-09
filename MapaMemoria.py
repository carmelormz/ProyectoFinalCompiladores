# Proyecto Final - Compiladores
# Autores: Carmelo Ramirez (A01175987) y Juan Pablo Galaz (A01251406)
# Mapa de memoria de el compilador

import sys

class MapaMemoria:
    def __init__(self, dirBase, entero, flotante, tmp, ptr, cte, stack):
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
        self.init_pos = stack
        self.stack_pos = stack
        self.call_stack = []

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
    
    def era(self, num_pars):
        tam = (len(self.mapa_memoria[self.lI])
               + len(self.mapa_memoria[self.lF])
               + len(self.mapa_memoria[self.lTI])
               + len(self.mapa_memoria[self.lTF])
               + len(self.mapa_memoria[self.lPI])
               + len(self.mapa_memoria[self.lPF])
               + 1 + num_pars)
        if self.stack_pos - tam > self.lim:
            contexto = {
                        self.lI : self.mapa_memoria[self.lI].copy(),
                        self.lF : self.mapa_memoria[self.lF].copy(),
                        self.lTI : self.mapa_memoria[self.lTI].copy(),
                        self.lTF : self.mapa_memoria[self.lTF].copy(),
                        self.lPI : self.mapa_memoria[self.lPI].copy(),
                        self.lPF : self.mapa_memoria[self.lPF].copy(),
                        'tam' : tam,
                        'ip' : 0,
                        'pars' : {}
                        }
            self.stack_pos -= tam
            self.call_stack.append(contexto)
        else:
            print("Stack Overflow")
            sys.exit()

    def param(self, val, mem):
        self.call_stack[-1]['pars'][mem] = val
        # print(self.call_stack[-1])

    def gosub(self, instuction_pointer):
        self.call_stack[-1]['ip'] = instuction_pointer + 1
        self.mapa_memoria[self.lI] = []
        self.mapa_memoria[self.lF] = []
        self.mapa_memoria[self.lTI] = []
        self.mapa_memoria[self.lTF] = []
        self.mapa_memoria[self.lPI] = []
        self.mapa_memoria[self.lPF] = []
        for direccion in self.call_stack[-1]['pars']:
            self.insert(direccion, self.call_stack[-1]['pars'][direccion])
    
    def endproc(self):
        contexto = self.call_stack.pop()
        self.mapa_memoria[self.lI] = contexto[self.lI].copy()
        self.mapa_memoria[self.lF] = contexto[self.lF].copy()
        self.mapa_memoria[self.lTI] = contexto[self.lTI].copy()
        self.mapa_memoria[self.lTF] = contexto[self.lTF].copy()
        self.mapa_memoria[self.lPI] = contexto[self.lPI].copy()
        self.mapa_memoria[self.lPF] = contexto[self.lPF].copy()
        self.stack_pos +=  contexto['tam']
        return contexto['ip']

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
