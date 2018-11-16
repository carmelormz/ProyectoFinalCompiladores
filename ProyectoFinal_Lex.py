#Proyecto Final - Compiladores
#Autores: Carmelo Ramirez (A01175987) y Juan Pablo Galaz (A01251406)

import ply.lex as lex
import sys

#------------- LEXICO DEL LENGUAJE ----------
#TOKENS VALIDOS EN EL LENGUAJE.
tokens = [
    'ID',
    'CTE_I',
    'CTE_F',
    'CTE_STR',
    'BRADER',
    'BRAIZQ',
    'CORDER',
    'CORIZQ',
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
    'MOD',
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
    'height': 'HEIGHT',
    'width': 'WIDTH',
    'canvas' : 'CANVAS',
    'print' : 'PRINT',
    'input' : 'INPUT',
    'forward' : 'FORWARD',
    'background': 'BACKGROUND',
    'backward' : 'BACKWARD',
    'left' : 'LEFT',
    'main' : 'MAIN',
    'right' : 'RIGHT',
    'turn' : 'TURN',
    'up' : 'UP',
    'down' : 'DOWN',
    'return' : 'RETURN',
    'circle' : 'CIRCLE',
    'triangle' : 'TRIANGLE',
    'square' : 'SQUARE',
    'ngon' : 'NGON',
    'arc' : 'ARC',
    'fill' : 'FILL',
    'color' : 'COLOR',
    'rotate' : 'ROTATE',
    'stretch' : 'STRETCH',
    'size' : 'SIZE',
    'int' : 'INT',
    'float' : 'FLOAT',
    'void' : 'VOID'
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
    r'\"[^\"\~]*\"'
    return t

def t_COMMENT(t):
    r'\#[^\#]*\#'
    pass

#REGLAS PARA DETECTAR CARACTERES ESPECIALES.
t_BRADER = r'\}'
t_BRAIZQ = r'\{'
t_CORDER = r'\]'
t_CORIZQ = r'\['
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
t_MOD = r'\%'
t_MULT = r'\*'
t_ASIG = r'\='
t_COMA = r'\,'
t_PUNTO = r'\.'
t_ignore = ' \t\n'


#MENSAJE DE ERROR.
def t_error(t):
    print("Invalid character")
    t.lexer.skip(1)
    sys.exit()


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