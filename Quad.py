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
        rellena()
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
        self.codigos_operacion = {'canvas' : 0, 'background' : 1, 'import' : 2,
                                  'endproc' : 3, 'return' : 4, 'ver' : 5,
                                  'goto' : 6, 'era' : 7, 'gosub' : 8,
                                  'param' : 9, 'end' : 10, 'gotof' : 11,
                                  'print' : 12, 'color' : 13, 'forward' : 14,
                                  'backward' : 15, 'left' : 16, 'right' : 17,
                                  'turn' : 18, 'size' : 19, 'circle' : 20,
                                  'triangle' : 21, 'square' : 22, 'ngon' : 23,
                                  'arc' : 24, 'up' : 25, 'down' : 26,
                                  'rotate' : 27, 'stretch' : 28, 'fill' : 29,
                                  '|' : 30, '&' : 31, '!=' : 32,
                                  '<' : 33, '>' : 34, '==' : 35,
                                  '<=' : 36, '>=' : 37, '+' : 38,
                                  '-' : 39, '*' : 40, '/' : 41,
                                  '=' : 42, '%' : 43, 'input' : 44,
                                  'module': 45, 'draw' : 46}
    '''
        genera()
            Metodo para generar un cuadruplo.
        Parametros:
            operador, el operador
            opd1, el primer operando
            opd2, el segundo operando
            res, el resultado
        Retorno:
            Nada
    '''
    def genera(self, operador, op_izq, op_der, res):
        operacion = self.codigos_operacion[operador]
        # operacion = operador
        self.quads.append([operacion, op_izq, op_der, res])
        self.contador += 1
    '''
        rellena()
            Metodo para rellenar el ultimo valor de un cuadruplo, con el contador.
        Parametros:
            val, direccion del cuadruplo
        Retorno:
            Nada
    '''
    def rellena(self, val):
        self.quads[val - 1][3] = self.contador
