# Proyecto Final - Compiladores
# Autores: Carmelo Ramirez (A01175987) y Juan Pablo Galaz (A01251406)
'''
    Clase TablaSemantica
        Implementa una Tabla Semantica.
    Variables:
        operandos, arreglo de operandos del lenguaje.
        operadores, arreglo de operadores del lenguaje.
        tabla_semantica, cubo de resultados de operandos con operadores
    Metodos:
        __init__()
        llenar()
        tipo()
'''
class TablaSemantica:
    '''
        __init__()
            Constructor inicial que define un arreglo vacio para la pila.
        Parametros:
            Sin parametros
        Retorno:
            Nada
    '''
    def __init__(self):
        self.operandos = {'int':0, 'float':1, 'None': 2, 'CTE_STR':3}
        self.operadores = {'||':0, '&&':1, '!=':2, '<':3, '>':4,
                           '==':5, '<=':6, '>=':7, '+':8, '-':9,
                           '*':10, '/':11, '=':12}
        self.tabla_semantica = [([(['' for i in range(len(self.operadores))]) for i in range(len(self.operandos))]) for i in range(len(self.operandos))]
        self.llenar('int', 'int', '||', 'int')
        self.llenar('int', 'int', '&&', 'int')
        self.llenar('int', 'int', '!=', 'int')
        self.llenar('int', 'int', '<', 'int')
        self.llenar('int', 'int', '>', 'int')
        self.llenar('int', 'int', '==', 'int')
        self.llenar('int', 'int', '<=', 'int')
        self.llenar('int', 'int', '>=', 'int')
        self.llenar('int', 'int', '+', 'int')
        self.llenar('int', 'int', '-', 'int')
        self.llenar('int', 'int', '*', 'int')
        self.llenar('int', 'int', '/', 'int')
        self.llenar('int', 'int', '=', 'int')

        self.llenar('int', 'float', '||', 'int')
        self.llenar('int', 'float', '&&', 'int')
        self.llenar('int', 'float', '!=', 'int')
        self.llenar('int', 'float', '<', 'int')
        self.llenar('int', 'float', '>', 'int')
        self.llenar('int', 'float', '==', 'int')
        self.llenar('int', 'float', '<=', 'int')
        self.llenar('int', 'float', '>=', 'int')
        self.llenar('int', 'float', '+', 'float')
        self.llenar('int', 'float', '-', 'float')
        self.llenar('int', 'float', '*', 'float')
        self.llenar('int', 'float', '/', 'float')
        self.llenar('int', 'float', '=', 'float')

        self.llenar('int', 'None', '+', 'int')
        self.llenar('int', 'None', '-', 'int')

        self.llenar('float', 'int', '||', 'int')
        self.llenar('float', 'int', '&&', 'int')
        self.llenar('float', 'int', '!=', 'int')
        self.llenar('float', 'int', '<', 'int')
        self.llenar('float', 'int', '>', 'int')
        self.llenar('float', 'int', '==', 'int')
        self.llenar('float', 'int', '<=', 'int')
        self.llenar('float', 'int', '>=', 'int')
        self.llenar('float', 'int', '+', 'float')
        self.llenar('float', 'int', '-', 'float')
        self.llenar('float', 'int', '*', 'float')
        self.llenar('float', 'int', '/', 'float')
        self.llenar('float', 'int', '=', 'float')

        self.llenar('float', 'float', '||', 'int')
        self.llenar('float', 'float', '&&', 'int')
        self.llenar('float', 'float', '!=', 'int')
        self.llenar('float', 'float', '<', 'int')
        self.llenar('float', 'float', '>', 'int')
        self.llenar('float', 'float', '==', 'int')
        self.llenar('float', 'float', '<=', 'int')
        self.llenar('float', 'float', '>=', 'int')
        self.llenar('float', 'float', '+', 'float')
        self.llenar('float', 'float', '-', 'float')
        self.llenar('float', 'float', '*', 'float')
        self.llenar('float', 'float', '/', 'float')
        self.llenar('float', 'float', '=', 'float')

        self.llenar('float', 'None', '+', 'float')
        self.llenar('float', 'None', '-', 'float')

        self.llenar('None', 'int', '+', 'int')
        self.llenar('None', 'int', '-', 'int')
        self.llenar('None', 'float', '+', 'float')
        self.llenar('None', 'float', '-', 'float')

    def llenar(self, operando1, operando2, operador, tipo):
        opd1 = self.operandos[operando1]
        opd2 = self.operandos[operando2]
        op = self.operadores[operador]
        self.tabla_semantica[opd1][opd2][op] = tipo
    
    def tipo(self, operando1, operando2, operador):
        opd1 = self.operandos[operando1]
        opd2 = self.operandos[operando2]
        op = self.operadores[operador]
        return self.tabla_semantica[opd1][opd2][op]
