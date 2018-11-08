# Proyecto Final - Compiladores
# Autores: Carmelo Ramirez (A01175987) y Juan Pablo Galaz (A01251406)
import sys
'''
    Clase GeneradorDireccion
        Implementa el mapa de memoria que guarde el estad de direcciones virtuales.
    Variables:
        
    Metodos:
        __init__()
        defFunc()
        finFunc()
        creaVarGlobal()
        creaVarLocal()
'''
class GeneradorDireccion:
    '''
        __init__()
            Constructor inicial que define un arreglo vacio para la pila.
        Parametros:
            Sin parametros
        Retorno:
            Nada
    '''
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
        self.vals = [dirBase, entero, flotante, tmp, ptr, cte]
        self.limite_locales = {'int': lF, 'float': lTI,
                               'tmpi': lTF, 'tmpf': lPI,
                               'ptri': lPF, 'ptrf': lPF}
        self.limite_globales = {'int': gF, 'float': gCI,
                                'ctei': gCF, 'ctef': lI}
        self.init_local = {'int': lI, 'float': lF,
                           'tmpi': lTI, 'tmpf': lTF,
                           'ptri': lPI, 'ptrf': lPF,}
        self.globales = {'int': gI, 'float': gF,
                         'ctei': gCI, 'ctef': gCF}
        self.locales = {'int': lI, 'float': lF,
                        'tmpi': lTI, 'tmpf': lTF,
                        'ptri': lPI, 'ptrf': lPF}
        self.estado_locales = []

    def defFunc(self):
        self.estado_locales.append(self.locales.copy())
        self.locales = self.init_local.copy()

    def finFunc(self):
        self.locales = self.estado_locales.pop()

    def creaVarGlobal(self, tipo, n=1):
        if self.globales[tipo] + n <= self.limite_globales[tipo]:
            self.globales[tipo] += n
            return self.globales[tipo] - n
        else:
            print('Too many variables of type %s declared' %(tipo))
            sys.exit()

    def creaVarLocal(self, tipo, n=1):
        if self.locales[tipo] + n <= self.limite_locales[tipo]:
            self.locales[tipo] += n
            return self.locales[tipo] - n
        else:
            print('Too many variables of type %s declared' %(tipo))
            sys.exit()
    


    