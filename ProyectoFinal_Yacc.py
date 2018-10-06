# Proyecto Final - Compiladores
# Autores: Carmelo Ramirez (A01175987) y Juan Pablo Galaz (A01251406)

import ply.yacc as yacc
import ProyectoFinal_Lex as scanner
import TablaSemantica as tb
import sys
import json

#------------- SINTAXIS DEL LENGUAJE ---------

precedence = (
    ('left','SUMA','RESTA'),
    ('left','MULT','DIV'),
)
# dir_func = {nombre, tipo, num_pars, tabla_vars}
# tabla_vars = {nombre, tipo, tam1, tam2}
dir_func = {}
id_programa = ""
funcion_actual = ""
tipo_actual = ""
id_actual = ""
num_args = 0
tabla_semantica = tb.TablaSemantica()

# DEFINICION DE LAS REGLAS DE LA GRAMATICA
def p_programa(p):
    '''programa : MODULE ID creaDirFunc PUNTCOM ajustes var_func tipo_main MAIN actualiza_id crea_func bloque_func'''

def p_creaDirFunc(p):
    '''creaDirFunc : '''
    global dir_func
    global id_programa
    global funcion_actual
    funcion_actual = 'global'
    id_programa = p[-1]
    dir_func['global'] = {'nombre': id_programa, 'tipo':'void', 'num_pars': 0,'tabla_vars': {}}

def p_ajustes(p):
    '''ajustes : CANVAS BRAIZQ WIDTH CTE_I PUNTCOM HEIGHT CTE_I PUNTCOM BACKGROUND CTE_F COMA CTE_F COMA CTE_F PUNTCOM BRADER
               | IMPORT CTE_STR'''

def p_var_func(p):
    '''var_func : tipo ID actualiza_id var_o_func
                | VOID tipo_void ID actualiza_id crea_func PARIZQ pars PARDER bloque_func funcs
                | '''

def p_actualiza_id(p):
    '''actualiza_id : '''
    global id_actual
    id_actual = p[-1]

def p_var_o_func(p):
    '''var_o_func : PARIZQ crea_func pars PARDER bloque_func funcs
                  | crea_var lista vars_lista PUNTCOM var_func'''

def p_crea_var(p):
    '''crea_var : '''
    global dir_func
    if dir_func[funcion_actual]['tabla_vars'].get(id_actual) == None:
        dir_func[funcion_actual]['tabla_vars'][id_actual] = {'nombre': id_actual, 'tipo':tipo_actual, 'tam1': 1, 'tam2': 0}
    else:
        print("Variable %s ya declarada" %(id_actual))
        # TODO generar error

def p_bloque_func(p):
    '''bloque_func : BRAIZQ vars_estatutos RETURN returns BRADER'''
    global funcion_actual
    funcion_actual = 'global'

def p_vars_estatutos(p):
    '''vars_estatutos : vars estatutos
                      | estatutos'''

def p_estatutos(p):
    '''estatutos : estatuto estatutos
                 | '''

def p_returns(p):
    '''returns : expresion PUNTCOM
               | PUNTCOM'''

def p_vars(p):
    ''' vars : tipo ID actualiza_id crea_var lista vars_lista PUNTCOM mas_vars'''

def p_vars_lista(p):
    '''vars_lista : COMA ID actualiza_id crea_var lista vars_lista
                  | '''
def p_mas_vars(p):
    '''mas_vars : vars
                | '''
def p_funcs(p):
    '''funcs : func funcs
             | '''

def p_func(p):
    '''func : tipo ID actualiza_id crea_func PARIZQ pars PARDER bloque_func
            | VOID tipo_void ID actualiza_id crea_func PARIZQ pars PARDER bloque_func'''

def p_tipo_void(p):
    '''tipo_void : '''
    global tipo_actual
    tipo_actual = p[-1]

def p_tipo_main(p):
    '''tipo_main : '''
    global tipo_actual
    tipo_actual = 'void'

def p_crea_func(p):
    '''crea_func : '''
    global dir_func
    global funcion_actual
    funcion_actual = id_actual
    if dir_func.get(funcion_actual) == None:
        dir_func[funcion_actual] = {'nombre': funcion_actual, 'tipo': tipo_actual, 'num_pars': 0, 'tabla_vars': {}}
    else:
        print("Funcion %s ya declarada" %(funcion_actual))
        # TODO generar error

def verificar_tipo(p1, p2):
    if type(p2) is str:
        return p1
    else:
        tipo = tabla_semantica.tipo(p1, p2[1], p2[0])
        if tipo == '':
            print("Type Mismatch %s , %s" %(p1, p2[1]))
            # TODO generar error
        else:
            return tipo

def p_expresion(p):
    '''expresion : expr or_expr'''
    p[0] = verificar_tipo(p[1], p[2])

def p_or_expr(p):
    '''or_expr : OR expresion
               | '''
    if len(p) > 1:
        p[0] = [p[1], p[2]]
    else:
        p[0] = 'None'

def p_expr(p):
    '''expr : exp and_exp'''
    p[0] = verificar_tipo(p[1], p[2])

def p_and_exp(p):
    '''and_exp : AND expr
               | '''
    if len(p) > 1:
        p[0] = [p[1], p[2]]
    else:
        p[0] = 'None'

def p_exp(p):
    '''exp : e rel_e'''
    p[0] = verificar_tipo(p[1], p[2])

def p_rel_e(p):
    '''rel_e : DIF exp
             | MENOR exp
             | MAYOR exp
             | MENIGUAL exp
             | MAYIGUAL exp
             | IGUAL exp
             |'''
    if len(p) > 1:
        p[0] = [p[1], p[2]]
    else:
        p[0] = 'None'

def p_e(p):
    '''e : termino suma_resta'''
    p[0] = verificar_tipo(p[1], p[2])

def p_suma_resta(p):
    '''suma_resta : SUMA e
                  | RESTA e
                  | '''
    if len(p) > 1:
        p[0] = [p[1], p[2]]
    else:
        p[0] = 'None'

def p_termino(p):
    '''termino : factor mult_div'''
    p[0] = verificar_tipo(p[1], p[2])

def p_mult(p):
    '''mult_div : MULT termino
                | DIV termino
                | '''
    if len(p) > 1:
        p[0] = [p[1], p[2]]
    else:
        p[0] = 'None'

def p_factor(p):
    '''factor : PARIZQ e PARDER
              | var
              | SUMA var
              | RESTA var'''
    if len(p) > 2:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_estatuto(p):
    '''estatuto : asignacion
                | condicion
                | escritura
                | ciclo
                | instruccion
                | func_call PUNTCOM'''

def p_func_call(p):
    '''func_call : ID PARIZQ args PARDER'''
    verifica_funcion(p[1])

def p_asignacion(p):
    '''asignacion : ID actualiza_id lista ASIG exp_input PUNTCOM'''
    if dir_func[funcion_actual]['tabla_vars'].get(p[1]) == None:
        if dir_func['global']['tabla_vars'].get(p[1]) == None:
            raise SyntaxError
        else:
            if (dir_func['global']['tabla_vars'][p[1]]['tipo'] != p[5]):
                print("Type Mismatch %s , %s." %(p[1], p[5]))
                # o Hacer typecasting
    else:
        if (dir_func[funcion_actual]['tabla_vars'][p[1]]['tipo'] != p[5]):
            print("Type Mismatch %s , %s." %(p[1], p[5]))
            # o Hacer typecasting

def p_asignacion_error(p):
    '''asignacion : error'''
    print("Variable %s not declared." %(id_actual))

def p_exp_input(p):
    '''exp_input : expresion
                 | INPUT PARIZQ PARDER'''
    if len(p) > 2:
        print("Input")
    else:
        p[0] = p[1]

def p_condicion(p):
    '''condicion : IF PARIZQ expresion PARDER bloque else_bloque'''
    if p[3] != 'int':
        print("Type Mismatch Expected int recieved %s." %(p[3]))

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
    if p[3] != 'int':
        print("Type Mismatch Expected int recieved %s." %(p[3]))

def p_tipo(p):
    '''tipo : INT actualiza_tipo
            | FLOAT actualiza_tipo'''

def p_actualiza_tipo(p):
    '''actualiza_tipo : '''
    global tipo_actual
    tipo_actual = p[-1]

def p_lista(p):
    '''lista : CORIZQ expresion CORDER matriz
             | '''
    # agrega p[2] como dimension #1 a id_actual
    # TODO verificar Buffer Overflow
    if (len(p) > 2):
        global dir_func
        dir_func[funcion_actual]['tabla_vars'][id_actual]['tam1'] = p[2]

def p_matriz(p):
    '''matriz : CORIZQ expresion CORDER
              | '''
    # agrega p[2] como dimension #2 a id_actual
    # TODO verificar Buffer Overflow
    if (len(p) > 2):
        global dir_func
        dir_func[funcion_actual]['tabla_vars'][id_actual]['tam2'] = p[2]

def p_var(p):
    '''var : ID actualiza_id var_func_call'''
    p[0] = p[3]

def p_var_int(p):
    '''var : CTE_I'''
    p[0] = 'int'

def p_var_float(p):
    '''var : CTE_F'''
    p[0] = 'float'

def p_var_func_call(p):
    '''var_func_call : PARIZQ args PARDER
                     | lista'''
    if len(p) > 2:
        p[0] = verifica_funcion(id_actual)
    else:            
        if dir_func[funcion_actual]['tabla_vars'].get(id_actual) == None:
            if dir_func['global']['tabla_vars'].get(id_actual) == None:
                print("Variable %s no declarada." %(id_actual))
                p[0] = 'None'
                # TODO generar error.
            else:
                p[0] = dir_func['global']['tabla_vars'][id_actual]['tipo']
        else:
            p[0] = dir_func[funcion_actual]['tabla_vars'][id_actual]['tipo']


def verifica_funcion(p):
    global num_args
    tipo = ''
    if dir_func.get(p) == None:
        print("Funcion %s no declarada." %(p))
        tipo = 'None'
        # TODO llamar error
    elif num_args != dir_func[p]['num_pars']:
        print('Funcion %s requiere %d parametros %d dados.' %(p, dir_func[p]['num_pars'], num_args))
        tipo = dir_func[p]['tipo']
        # TODO llamar error
    else:
        tipo = dir_func[p]['tipo']
        # llamar funcion
    num_args = 0
    return tipo

def p_args(p):
    '''args : expresion arg
            | '''
    if len(p) > 1:
        global num_args
        num_args += 1

def p_arg(p):
    '''arg : COMA expresion arg
           | '''
    if len(p) > 1:
        global num_args
        num_args += 1

def p_bloque(p):
    ''' bloque : BRAIZQ estatutos BRADER '''

def p_pars(p):
    '''pars : tipo ID actualiza_id crea_var lista par
            | '''
    if len(p) > 1:
        dir_func[funcion_actual]['num_pars'] = dir_func[funcion_actual]['num_pars'] + 1

def p_par(p):
    '''par : COMA tipo ID actualiza_id crea_var lista par
           | '''
    if len(p) > 1:
        dir_func[funcion_actual]['num_pars'] = dir_func[funcion_actual]['num_pars'] + 1

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
        data=file.read()
        file.close()
        parser.parse(data)
    print(json.dumps(dir_func, indent=4))

if __name__ == '__main__':
    main()