# Proyecto Final - Compiladores
# Autores: Carmelo Ramirez (A01175987) y Juan Pablo Galaz (A01251406)
'''
    Clase MapaMemoria
        Implementa el mapa de memoria que guarde el estad de direcciones virtuales.
    Variables:
        
    Metodos:
        __init__()
        llamadaFun()
        finFunc()
        creaVarGlobal()
        creaVarLocal()
'''
class MapaMemoria:
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
        # Tamaño = 8000 + dirBase
        self.init_local = {'int': lI, 'float': lF,
                           'tmpi': lTI, 'tmpf': lTF,
                           'ptri': lPI, 'ptrf': lPF,}
        self.globales = {'int': gI, 'float': gF,
                         'ctei': gCI, 'ctef': gCF}
        self.locales = {'int': lI, 'float': lF,
                        'tmpi': lTI, 'tmpf': lTF,
                        'ptri': lPI, 'ptrf': lPF,}
        self.estado_locales = []

    def defFunc(self):
        self.estado_locales.append(self.locales.copy())
        self.locales = self.init_local.copy()

    def finFunc(self):
        self.locales = self.estado_locales.pop()

    def creaVarGlobal(self, tipo, n=1):
        self.globales[tipo] += n
        return self.globales[tipo] - n

    def creaVarLocal(self, tipo, n=1):
        self.locales[tipo] += n
        return self.locales[tipo] - n
    


    