#Proyecto Final - Compiladores
#Autores: Carmelo Ramirez (A01175987) y Juan Pablo Galaz (A01251406)

import ply.yacc as yacc
import ProyectoFinal_Lex as scanner
import sys

#------------- SINTAXIS DEL LENGUAJE ---------

precedence = (
    ('left','SUMA','RESTA'),
    ('left','MULT','DIV'),
)

# DEFINICION DE LAS REGLAS DE LA GRAMATICA
def p_programa(p):
    '''programa : MODULE ID PUNTCOM ajustes var_func MAIN bloque_func'''

def p_ajustes(p):
    '''ajustes : CANVAS BRAIZQ WIDTH CTE_I PUNTCOM HEIGHT CTE_I PUNTCOM BACKGROUND CTE_F COMA CTE_F COMA CTE_F PUNTCOM BRADER
               | IMPORT CTE_STR'''

def p_var_func(p):
    '''var_func : tipo ID var_o_func
                | VOID ID PARIZQ pars PARDER bloque_func funcs
                | '''

def p_var_o_func(p):
    '''var_o_func : lista vars_lista PUNTCOM var_func
                  | PARIZQ pars PARDER bloque_func funcs'''

def p_bloque_func(p):
    '''bloque_func : BRAIZQ vars_estatutos returns BRADER'''

def p_vars_estatutos(p):
    '''vars_estatutos : vars estatutos
                      | estatutos'''

def p_estatutos(p):
    '''estatutos : estatuto estatutos
                 | '''

def p_returns(p):
    '''returns : RETURN expresion PUNTCOM
               | '''
def p_vars(p):
    ''' vars : tipo ID lista vars_lista PUNTCOM mas_vars'''

def p_vars_lista(p):
    '''vars_lista : COMA ID lista vars_lista
                  | '''
def p_mas_vars(p):
    '''mas_vars : vars
                | '''
def p_funcs(p):
    '''funcs : func funcs
             | '''

def p_func(p):
    '''func : tipo ID PARIZQ pars PARDER bloque_func
            | VOID ID PARIZQ pars PARDER bloque_func'''

def p_expresion(p):
    '''expresion : exp mas_exp'''

def p_mas_exp(p):
    '''mas_exp : MENOR exp
               | MAYOR exp
               | MENIGUAL exp
               | MAYIGUAL exp
               | IGUAL exp
               | DIF exp
               | AND exp
               | OR exp
               | '''

def p_exp(p):
    '''exp : termino suma_resta'''

def p_suma_resta(p):
    '''suma_resta : SUMA termino
                  | RESTA termino
                  | '''
def p_termino(p):
    '''termino : factor mult_div'''

def p_mult_div(p):
    '''mult_div : MULT factor
                | DIV factor
                | '''

def p_factor(p):
    '''factor : PARIZQ expresion PARDER
              | var_func_call
              | SUMA var_func_call
              | RESTA var_func_call'''

def p_var_func_call(p):
    '''var_func_call : var
                     | func_call'''

def p_estatuto(p):
    '''estatuto : asignacion
                | condicion
                | escritura
                | ciclo
                | instruccion
                | func_call PUNTCOM'''

def p_asignacion(p):
    '''asignacion : ID lista ASIG exp_input PUNTCOM'''

def p_exp_input(p):
    '''exp_input : expresion
                 | INPUT PARIZQ PARDER'''

def p_condicion(p):
    '''condicion : IF PARIZQ expresion PARDER bloque else_bloque'''

def p_else_bloque(p):
    '''else_bloque : ELSE bloque
                   | '''
def p_escritura(p):
    '''escritura : PRINT PARIZQ arg_escritura PARDER PUNTCOM'''

def p_arg_escritura(p):
    '''arg_escritura : expresion args_escritura
                     | CTE_STR args_escritura'''

def p_args_escritura(p):
    '''args_escritura : COMA arg_escritura
                      | '''

def p_ciclo(p):
    '''ciclo : REPEAT PARIZQ expresion PARDER bloque'''

def p_tipo(p):
    '''tipo : INT
            | FLOAT '''

def p_lista(p):
    '''lista : CORIZQ expresion CORDER matriz
             | '''

def p_matriz(p):
    '''matriz : CORIZQ expresion CORDER
              | '''

def p_var(p):
    '''var : ID lista
           | CTE_I
           | CTE_F'''

def p_func_call(p):
    '''func_call : ID PARIZQ args PARDER'''

def p_args(p):
    '''args : expresion arg
            | '''

def p_arg(p):
    '''arg : COMA expresion arg
           | '''

def p_bloque(p):
    ''' bloque : BRAIZQ estatutos BRADER '''

def p_pars(p):
    '''pars : tipo ID par
            | '''
def p_par(p):
    '''par : COMA tipo ID par
           | '''

def p_instruccion(p):
    '''instruccion : FORWARD PARIZQ expresion PARDER PUNTCOM
                   | BACKWARD PARIZQ expresion PARDER PUNTCOM
                   | LEFT PARIZQ expresion PARDER PUNTCOM
                   | RIGHT PARIZQ expresion PARDER PUNTCOM
                   | TURN PARIZQ expresion PARDER PUNTCOM
                   | SIZE PARIZQ expresion PARDER PUNTCOM
                   | CIRCLE PARIZQ expresion PARDER transform PUNTCOM
                   | TRIANGLE PARIZQ expresion PARDER transform PUNTCOM
                   | SQUARE PARIZQ expresion PARDER transform PUNTCOM
                   | NGON PARIZQ expresion COMA expresion PARDER transform PUNTCOM
                   | ARC PARIZQ expresion COMA expresion PARDER transform PUNTCOM
                   | UP PARIZQ PARDER PUNTCOM
                   | DOWN PARIZQ PARDER PUNTCOM
                   | COLOR PARIZQ expresion COMA expresion COMA expresion PARDER PUNTCOM'''

def p_transform(p):
    '''transform : PUNTO altera transform
                 | '''

def p_altera(p):
    '''altera : ROTATE PARIZQ expresion PARDER
              | STRETCH PARIZQ expresion PARDER
              | FILL PARIZQ PARDER'''

def p_error(p):
    print("Syntax error at token " + str(p.type) + " lineno " + str(p.lineno))


# FUNCION PRINCIPAL PARA EVELUAR UN ARCHIVO DE TEXTO - python3 ProyectoFinal_Yacc.py archivo
def main():
    lexer = scanner.lexer
    tokens = scanner.tokens
    parser = yacc.yacc()
    with open(str(sys.argv[1]), 'r') as file:
        data=file.read().replace('\n', '')
        file.close()
        parser.parse(data)

if __name__ == '__main__':
    main()