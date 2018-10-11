# Proyecto Final - Compiladores
# Autores: Carmelo Ramirez (A01175987) y Juan Pablo Galaz (A01251406)
'''
    Clase Quad
        Implementa un quad que guarda el codigo generado para una maquina virtual.
    Variables:
        contador, contador que apunta al siguiente quad a generar.
        quads, arreglo de instrucciones generadas.
    Metodos:
        __init__()
        genera()
'''
class Quad:
    '''
        __init__()
            Constructor inicial que define un arreglo vacio para la pila.
        Parametros:
            Sin parametros
        Retorno:
            Nada
    '''
    def __init__(self):
        self.contador = 1
        self.quads = []
    def genera(self, operador, op_izq, op_der, res):
        self.quads.append([operador, op_izq, op_der, res])
        self.contador += 1
    def rellena(self, val):
        self.quads[val - 1][3] = self.contador
