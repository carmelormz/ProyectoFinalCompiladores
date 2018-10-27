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
    def __init__(self, gInt, gFloat, gCte, lInt, lFloat, lCte):
        init_local = {'int': lInt, 'float': lFloat, 'cte': lCte}
        self.globales = {'int': gInt, 'float': gFloat, 'cte': gCte}
        self.locales = init_local
        self.estado_locales = []


    def llamadaFun(self):
        sel.estado_locales.append(self.locales)
        self.locales = init_local


    def finFunc(self):
        self.locales =  self.estado_locales.pop()


    def creaVarGlobal(tipo):
        self.globales[tipo] += 1
        return self.globales[tipo] - 1


    def creaVarLocal(tipo):
        self.locales[tipo] += 1
        return self.locales[tipo] - 1
    


    