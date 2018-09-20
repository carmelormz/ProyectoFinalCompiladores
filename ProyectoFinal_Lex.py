#Proyecto Final - Compiladores
#Autores: Carmelo Ramirez (A01175987) y Juan Pablo Galaz (A01251406)

import ply.lex as lex


#------------- LEXICO DEL LENGUAJE ----------
#TOKENS VALIDOS EN EL LENGUAJE.
tokens = [
    'ID',
    'CTE_I',
    'CTE_F',
    'CTE_STR',
    'BRADER',
    'BRAIZQ',
    'PARDER',
    'PARIZQ',
    'PUNTCOM',
    'DIF',
    'MENOR',
    'MAYOR',
    'MENIGUAL',
    'MAYIGUAL',
    'IGUAL',
    'AND',
    'OR',
    'SUMA',
    'RESTA',
    'DIV',
    'MULT',
    'ASIG',
    'COMA',
    'PUNTO'
]


#PALABRAS RESERVADAS PARA EL LENGUAJE.
palabrasReservadas = {
    'if' : 'IF',
    'else' : 'ELSE',
    'repeat' : 'REPEAT',
    'module' : 'MODULE',
    'import': 'IMPORT',
    'canvas' : 'CANVAS',
    'print' : 'PRINT',
    'input' : 'INPUT',
    'forward' : 'FORWARD',
    'backward' : 'BACKWARD',
    'left' : 'LEFT',
    'main' : 'MAIN',
    'right' : 'RIGHT',
    'turn' : 'TURN',
    'up' : 'UP',
    'down' : 'DOWN',
    'return' : 'RETURN',
    'circle' : 'CIRCLE',
    'triange' : 'TRIANGLE',
    'square' : 'SQUARE',
    'ngon' : 'NGON',
    'fill' : 'FILL',
    'color' : 'COLOR',
    'rotate' : 'ROTATE',
    'stretch' : 'STRETCH'
}


#AGREGAMOS LAS PALABRAS RESERVADAS A LA LISTA DE TOKENS.
tokens += palabrasReservadas.values()


#REGLA PARA DETECTAR TIPO DE CONSTANTE NUMERICA DECIMAL.
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in palabrasReservadas:
        t.type = palabrasReservadas[t.value]
    return t


#REGLA PARA DETECTAR CONSTANTES NUMERICAS DECIMALES.
def t_CTE_F(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


#REGLA PARA DETECTAR CONSTATNES NUMERICAS ENTERAS.
def t_CTE_I(t):
    r'\d+'
    t.value = int(t.value)
    return t


#REGLA PARA DETECTAR CONSTANTES DE TEXTO.
def t_CTE_STR(t):
    r'\"[a-zA-Z0-9_\.\(\)-\[\]]*\"'
    return t


#REGLAS PARA DETECTAR CARACTERES ESPECIALES.
t_BRADER = r'\}'
t_BRAIZQ = r'\{'
t_PARDER = r'\)'
t_PARIZQ = r'\('
t_PUNTCOM = r'\;'
t_DIF = r'\!\='
t_MENOR = r'\<'
t_MAYOR = r'\>'
t_MENIGUAL = r'\<\='
t_MAYIGUAL = r'\>\='
t_IGUAL = r'\=\='
t_AND = r'\&'
t_OR = r'\|'
t_SUMA = r'\+'
t_RESTA = r'\-'
t_DIV = r'\/'
t_MULT = r'\*'
t_ASIG = r'\='
t_COMA = r'\,'
t_PUNTO = r'\.'
t_ignore = ' \t\n'


#MENSAJE DE ERROR.
def t_error(t):
    print("Caracter Invalido")
    t.lexer.skip(1)


#CREACION DE INSTANCIA DE LEXER.
lexer = lex.lex()


# FUNCION ADICIONAL PARA VER LOS TOKENS DENTRO DE UNA CADENA.
def verTokens(entrada):
    lexer.input(entrada)
    # entrada = ' "str[()w2ASSDAF]ng" hheooi 78923 930 l 990.32 * 27 if else repeat !=  <= == >=  & | = { } () "" '
    token = lexer.token()
    while (token is not None):
        print(token)
        token = lexer.token()

