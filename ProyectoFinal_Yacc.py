# Proyecto Final - Compiladores
# Autores: Carmelo Ramirez (A01175987) y Juan Pablo Galaz (A01251406)

import ply.yacc as yacc
import ProyectoFinal_Lex as scanner
import TablaSemantica as tb
import GeneraDireccion as gd
import Quad as q
import sys
import json

#------------- SINTAXIS DEL LENGUAJE ---------
# dir_func = {nombre, tipo, tamano, secuencia_par, tabla_vars, dir_inicio}
# tabla_vars = {nombre, tipo, dim, dir_virual}
dir_func = {}
# Nombre del programa que se describe en module.
id_programa = ""
# La funcion acutal, se actualiza al tiempo de definir una funcion.
funcion_actual = ""
# Pila de llamada de funciones para el control de parametros.
func_call = []
# Tipo actual, se actualiza al tiempo de definir una nueva variable.
tipo_actual = ""
# Id actual, se actualiza al tiempo de definir una nueva variable.
id_actual = ""
# Instruccion actual, se actualiza al declarar una figura a dibujar.
instr_actual =""
# Num args, el numero de argumentos en la llamada de funcion
num_args = 0
# Asignacion es expresion o input
asig_input = False
# Operador uanrio menos
negativo = False
# Tabla Semantica para Resolver el tipo de una operacion
tabla_semantica = tb.TablaSemantica()
# Pila de operadores.
pila_operadores = []
# Pila de operandos.
pila_operandos = []
# Pila de Saltos
pila_saltos = []
# Estructura para genera quadruplos
quads = q.Quad()
# Pila de variables dimensionadas para tener casos A[B[C[1]]]
var_dim = []
# Cantidad de direcciones para cada tipo dirBase, entero, flotante, tmp, ptr, cte.
mapa = gd.GeneradorDireccion(5000, 1000, 1000, 1000, 500, 500)
# Tabla de constantes
tabla_constantes = {}
# DEFINICION DE LAS REGLAS DE LA GRAMATICA
def p_programa(p):
    '''programa : MODULE CTE_STR creaDirFunc PUNTCOM ajustes var_func tipo_main MAIN actualiza_id crea_func bloque_func'''

# Funcion para rellenar el goto del modulo main.
def p_tipo_main(p):
    '''tipo_main : '''
    global tipo_actual
    global quads
    global pila_operandos
    global pila_saltos
    tipo_actual = 'void'
    quads.rellena(pila_saltos.pop())

# Funcion para crear el directorio de funciones, genera el quadruplo module.
def p_creaDirFunc(p):
    '''creaDirFunc : '''
    global dir_func
    global id_programa
    global funcion_actual
    funcion_actual = 'global'
    id_programa = p[-1]
    dir_func['global'] = {'nombre': id_programa, 'tipo':'void', 'secuencia_par': [],'tabla_vars': {}, 'dir_inicio': 0, 'tamano': 0}
    quads.genera('module', None, None, p[-1])

# Funcion para agregar una constante en la tabla de constantes y regresar su dirección virtual.
def dir_constant(val, tipo):
    global tabla_constantes
    if tabla_constantes.get(val) == None:
        dir_virtual = mapa.creaVarGlobal(tipo)
        tabla_constantes[val] = dir_virtual
    else:
        dir_virtual = tabla_constantes[val]
    return dir_virtual

# Crea los modulos necesarios para los ajustes de pantalla.
def p_ajustes(p):
    '''ajustes : CANVAS BRAIZQ WIDTH CTE_I PUNTCOM HEIGHT CTE_I PUNTCOM BACKGROUND CTE_I COMA CTE_I COMA CTE_I PUNTCOM BRADER
               | IMPORT CTE_STR PUNTCOM'''
    global quads
    global pila_saltos
    if len(p) > 4:
        quads.genera('canvas', None, dir_constant(p[4], 'ctei'),
                                     dir_constant(p[7], 'ctei'))
        quads.genera('background', dir_constant(p[10], 'ctef'),
                                   dir_constant(p[12], 'ctef'),
                                   dir_constant(p[14], 'ctef'))
    else:
        quads.genera('import', None, None, p[2])
    pila_saltos.append(quads.contador)
    quads.genera('goto',None, None, None)

# Reglas Sintactica para eliminar Shift/Reduce
def p_var_func(p):
    '''var_func : tipo ID actualiza_id var_o_func
                | 
       var_o_func : PARIZQ crea_func pars PARDER bloque_func funcs
                  | crea_var lista_dec vars_lista PUNTCOM var_func'''

# Actualizar el Id actual
def p_actualiza_id(p):
    '''actualiza_id : '''
    global id_actual
    id_actual = p[-1]
    p[0] = p[-1]

# Regla sintactica para el tipo posible de variables
def p_tipo(p):
    '''tipo : INT actualiza_tipo
            | FLOAT actualiza_tipo'''
    p[0] = p[1]

# Actualizar el Tipo actual
def p_actualiza_tipo(p):
    '''actualiza_tipo : '''
    global tipo_actual
    tipo_actual = p[-1]

# Funcion para agregar a la tabla de variables
def p_crea_var(p):
    '''crea_var : '''
    global dir_func
    if dir_func[funcion_actual]['tabla_vars'].get(id_actual) == None:
        dir_func[funcion_actual]['tabla_vars'][id_actual] = {'nombre': id_actual, 'tipo':tipo_actual, 'dim': [], 'dir_virtual': 0}
    else:
        print("Variable %s ya declarada" %(id_actual))
        sys.exit()

# Funcion para declar una variable dimensionada 
def p_lista_dec(p):
    '''lista_dec : CORIZQ CTE_I CORDER matriz_dec
                 | '''
    global dir_func
    global mapa
    tipo = dir_func[funcion_actual]['tabla_vars'][id_actual]['tipo']
    if len(p) > 2:
        # Si sí es dimensionada
        if p[2] < 1:
            print("Dimension must be greater than 1, var %s" %(id_actual))
            sys.exit()
        tam = 0
        dir_virtual = 0
        dir_func[funcion_actual]['tabla_vars'][id_actual]['dim'].insert(0,p[2])
        if len(dir_func[funcion_actual]['tabla_vars'][id_actual]['dim']) > 1:
            tam = dir_func[funcion_actual]['tabla_vars'][id_actual]['dim'][0]*dir_func[funcion_actual]['tabla_vars'][id_actual]['dim'][1]
            dir_func[funcion_actual]['tamano'] += tam
        else:
            tam = dir_func[funcion_actual]['tabla_vars'][id_actual]['dim'][0]
            dir_func[funcion_actual]['tamano'] += tam
        
        if funcion_actual == 'global':
            dir_virtual = mapa.creaVarGlobal(tipo, tam)
        else:
            dir_virtual = mapa.creaVarLocal(tipo, tam)
        dir_func[funcion_actual]['tabla_vars'][id_actual]['dir_virtual'] = dir_virtual
    else:
        # Es variable simple
        dir_func[funcion_actual]['tamano'] += 1
        dir_virtual = 0
        if funcion_actual == 'global':
            dir_virtual = mapa.creaVarGlobal(tipo)
        else:
            dir_virtual = mapa.creaVarLocal(tipo)
        dir_func[funcion_actual]['tabla_vars'][id_actual]['dir_virtual'] = dir_virtual

# Funcion para declar una variable dimensionada de dos dimensiones.
def p_matriz_dec(p):
    '''matriz_dec : CORIZQ CTE_I CORDER
                  | '''
    global dir_func
    if len(p) > 2:
        dir_func[funcion_actual]['tabla_vars'][id_actual]['dim'].insert(0,p[2])
        if p[2] < 1:
            print("Second dimension must be greater than 1 for variable %s" %(id_actual))
            sys.exit()

# Define un bloque de funcion.
def p_bloque_func(p):
    '''bloque_func : BRAIZQ vars_estatutos RETURN returns BRADER end_sub'''
    global funcion_actual
    funcion_actual = 'global'

# Genera quadruplo fin de funcion o fin de program en caso de modulo main
def p_end_sub(p):
    '''end_sub : '''
    global quads
    global mapa
    mapa.finFunc()
    if funcion_actual == 'main':
        quads.genera('end', None, None, None)
    else:
        quads.genera('endproc', None, None, None)

# Reglas Sintacticas de estatutos, algunas agregadas para eliminar Shift/Reduce
def p_vars_estatutos(p):
    ''' vars_estatutos : vars estatutos
                       | estatutos
        estatutos : estatuto estatutos
                  | 
        vars : tipo ID actualiza_id crea_var lista_dec vars_lista PUNTCOM mas_vars
        vars_lista : COMA ID actualiza_id crea_var lista_dec vars_lista
                   |
        mas_vars : vars
                 | 
        funcs : func funcs
              |
        func : tipo ID actualiza_id crea_func PARIZQ pars PARDER bloque_func
             | VOID tipo_void ID actualiza_id crea_func PARIZQ pars PARDER bloque_func
        var_func : VOID tipo_void ID actualiza_id crea_func PARIZQ pars PARDER bloque_func funcs'''

# Genera el quadrupllo de retorno para una función
def p_returns(p):
    '''returns : expresion PUNTCOM
               | PUNTCOM'''
    global pila_operandos
    global quads
    if len(p) > 2:
        tempRes = pila_operandos.pop()
        quads.genera('return', None, None, tempRes['dir_virtual'])

# Regla sintactica para definir parametros de una funcion.
def p_pars(p):
    '''pars : tipo ID actualiza_id crea_var gen_dir par
            | '''
    if len(p) > 1:
        dir_virtual = dir_func[funcion_actual]['tabla_vars'][p[2]]['dir_virtual']
        dir_func[funcion_actual]['secuencia_par'].append({'nombre': p[2], 'tipo': p[1], 'dir_virtual' : dir_virtual})

# Regla sintactica que apoya a definir parametros de una funcion, elimina regla ambigua.
def p_par(p):
    '''par : COMA tipo ID actualiza_id crea_var gen_dir par
           | '''
    if len(p) > 1:
        dir_virtual = dir_func[funcion_actual]['tabla_vars'][p[3]]['dir_virtual']
        dir_func[funcion_actual]['secuencia_par'].append({'nombre': p[3], 'tipo': p[2], 'dir_virtual' : dir_virtual})

# Genera direccion virtual para parametro.
def p_gen_dir(p):
    '''gen_dir : '''
    global dir_func
    dir_virtual = mapa.creaVarLocal(dir_func[funcion_actual]['tabla_vars'][id_actual]['tipo'])
    dir_func[funcion_actual]['tabla_vars'][id_actual]['dir_virtual'] = dir_virtual

# Actualiza al tipo actual como void.
def p_tipo_void(p):
    '''tipo_void : '''
    global tipo_actual
    tipo_actual = p[-1]

# Regla para agregar una funcion al directorio de funciones.
def p_crea_func(p):
    '''crea_func : '''
    global quads
    global dir_func
    global funcion_actual
    global mapa
    mapa.defFunc()
    funcion_actual = id_actual
    if dir_func.get(funcion_actual) == None:
        dir_func[funcion_actual] = {'nombre': funcion_actual, 'tipo': tipo_actual, 'secuencia_par': [], 'tabla_vars': {}, 'dir_inicio': quads.contador, 'tamano': 0}
    else:
        print("Funcion %s ya declarada" %(funcion_actual))
        sys.exit()

# Funcion para agregar un operador a la pila de operadores.
def p_push_oper(p):
    '''push_oper : '''
    global pila_operadores
    pila_operadores.append(p[-1])

# Funcion para sacar un operadorer de la pila de operadores.
def pop_oper(operadores):
    global pila_operadores
    global pila_operandos
    global mapa
    if len(pila_operadores) == 0 : return
    pop = False
    # Ver si el operador encima de la pila es uno de los operadores que se deben sacar
    for i in operadores:
        if i == pila_operadores[-1]:
            pop = True
    if pop:
        der = pila_operandos.pop()
        izq = pila_operandos.pop()
        oper = pila_operadores.pop()
        tipo_res = tabla_semantica.tipo(der['tipo'], izq['tipo'], oper)
        if tipo_res != '':
            if tipo_res == 'int':
                dir_virtual = mapa.creaVarLocal('tmpi')
            else:
                dir_virtual = mapa.creaVarLocal('tmpf')
            quads.genera(oper, izq['dir_virtual'], der['dir_virtual'], dir_virtual)
            pila_operandos.append({'nombre': 'temp',
                                   'tipo' : tipo_res,
                                   'dir_virtual' : dir_virtual})
        else:
            print("Type Mismatch")
            sys.exit()

# Funcion para sacar el operadorer | de la pila de operadores.
def p_pop_or(p):
    '''pop_or : '''
    pop_oper(['|'])

# Funcion para sacar el operadorer & de la pila de operadores.
def p_pop_and(p):
    '''pop_and : '''
    pop_oper(['&'])

# Funcion para sacar un operadore relacional de la pila de operadores.
def p_pop_rel_e(p):
    '''pop_rel_e : '''
    pop_oper(['!=', '<', '>', '<=', '>=', '=='])

# Funcion para sacar un operador suma o resta de la pila de operadores.
def p_pop_suma_resta(p):
    '''pop_suma_resta : '''
    pop_oper(['+', '-'])

# Funcion para sacar un operador multiplica, division o modulo  de la pila de operadores.
def p_pop_mult_div(p):
    '''pop_mult_div : '''
    pop_oper(['*', '/', '%'])

# Reglas sintacticas de expresiones.
def p_expresion(p):
    '''expresion : expr pop_or or_expr
       or_expr : OR push_oper expresion
               | 
       expr : exp pop_and and_exp
       and_exp : AND push_oper expr
               | 
       exp : e pop_rel_e rel_e
       rel_e : DIF push_oper exp
             | MENOR push_oper exp
             | MAYOR push_oper  exp
             | MENIGUAL push_oper exp
             | MAYIGUAL push_oper exp
             | IGUAL push_oper exp
             |
       e : termino pop_suma_resta suma_resta
       suma_resta : SUMA push_oper e
                  | RESTA push_oper e
                  | 
       termino : factor pop_mult_div mult_div 
       mult_div : MULT push_oper termino
                | DIV push_oper termino
                | MOD push_oper termino
                | 
       factor : PARIZQ push_paren expresion PARDER pop_paren
              | var
              | RESTA neg_push var neg_pop
       var : ID actualiza_id push_paren var_func_call pop_paren
       var_func_call : lista'''

def p_neg_push(p):
    '''neg_push : '''
    global negativo
    negativo = True

def p_neg_pop(p):
    '''neg_pop : '''
    global negativo
    negativo = False

# Agregar constante entera a la pila de operadores.
def p_var_int(p):
    '''var : CTE_I'''
    global pila_operandos
    global mapa
    global negativo
    if negativo:
        p[1] = -p[1]
    pila_operandos.append({'nombre': p[1],
                           'tipo' : 'int',
                           'dir_virtual' : dir_constant(p[1],'ctei')})

# Agregar constante flotante a la pila de operadores.
def p_var_float(p):
    '''var : CTE_F'''
    global pila_operandos
    global mapa
    global negativo
    if negativo:
        p[1] = -p[1]
    pila_operandos.append({'nombre': p[1],
                           'tipo' : 'float',
                           'dir_virtual' : dir_constant(p[1],'ctef')})

def p_var_error(p):
    '''var : error'''
    print("Type Mismatch")
    sys.exit()

def p_push_paren(p):
    '''push_paren : '''
    global pila_operadores
    pila_operadores.append('(')

def p_pop_paren(p):
    '''pop_paren : '''
    global pila_operadores
    top = pila_operadores.pop()
    if top != '(':
        print('Error', top) 
        sys.exit()

def p_push_dim(p):
    '''push_dim : '''
    global id_actual
    global var_dim
    var_dim.append(id_actual)

def p_pop_dim(p):
    '''pop_dim : '''
    global id_actual
    global var_dim
    id_actual = var_dim.pop()

def p_lista(p):
    '''lista : CORIZQ push_dim expresion CORDER matriz
             | '''
    global dir_func
    global pila_operandos
    if len(p) < 2:
        if dir_func[funcion_actual]['tabla_vars'].get(id_actual) != None:
            if len(dir_func[funcion_actual]['tabla_vars'][id_actual]['dim']) > 0:
                print("Variable %s is Multidimensional" %(id_actual))
                sys.exit()
            else:
                tipo = dir_func[funcion_actual]['tabla_vars'][id_actual]['tipo']
                dir_virtual = dir_func[funcion_actual]['tabla_vars'][id_actual]['dir_virtual']
                pila_operandos.append({'nombre': id_actual,
                                       'tipo' : tipo,
                                       'dir_virtual' : dir_virtual})
        elif dir_func['global']['tabla_vars'].get(id_actual) != None:
            if len(dir_func['global']['tabla_vars'][id_actual]['dim']) > 0:
                print("Variable %s is Multidimensional" %(id_actual))
                sys.exit()
            else:
                tipo = dir_func['global']['tabla_vars'][id_actual]['tipo']
                dir_virtual = dir_func['global']['tabla_vars'][id_actual]['dir_virtual']
                pila_operandos.append({'nombre': id_actual,
                                       'tipo' : tipo,
                                       'dir_virtual' : dir_virtual})
        else:
            print("Variable %s no declarada." %(id_actual))
            sys.exit()

def matrix_def(funcion_actual):
    global dir_func
    global pila_operandos
    global quads
    d2 = pila_operandos.pop()
    d1 = pila_operandos.pop()
    if d1['tipo'] != 'int' or d2['tipo'] != 'int':
        print("Indices must be integers")
        sys.exit()
    d2 = d2['dir_virtual']
    d1 = d1['dir_virtual']
    tipo = dir_func[funcion_actual]['tabla_vars'][id_actual]['tipo']
    if tipo == 'int':
        dir_virtual = mapa.creaVarLocal('tmpi')
        dir_virtual2 = mapa.creaVarLocal('tmpi')
        ptr = mapa.creaVarLocal('ptri')
    else:
        dir_virtual = mapa.creaVarLocal('tmpf')
        dir_virtual2 = mapa.creaVarLocal('tmpf')
        ptr = mapa.creaVarLocal('ptrf')
    li = dir_constant(0,'ctei')
    ls1 = dir_constant(dir_func[funcion_actual]['tabla_vars'][id_actual]['dim'][0] - 1,'ctei')
    ls2 = dir_constant(dir_func[funcion_actual]['tabla_vars'][id_actual]['dim'][1] - 1,'ctei')
    tam = dir_constant(dir_func[funcion_actual]['tabla_vars'][id_actual]['dim'][0], 'ctei')
    quads.genera('ver', d1, li, ls1)
    quads.genera('*', d1, tam, dir_virtual)
    quads.genera('ver', d2, li, ls2)
    quads.genera('+', d2, dir_virtual, dir_virtual2)
    dirB = dir_func[funcion_actual]['tabla_vars'][id_actual]['dir_virtual']
    quads.genera('+', dir_constant(dirB, 'ctei'), dir_virtual2, ptr)
    pila_operandos.append({'nombre': 'ptr', 'tipo' : tipo, 'dir_virtual': '~' + str(ptr)})

def vect_def(funcion_actual):
    global dir_func
    global pila_operandos
    global quads
    d1 = pila_operandos.pop()
    if d1['tipo'] != 'int':
        print("Indices must be integers")
        sys.exit()
    d1 = d1['dir_virtual']
    tipo = dir_func[funcion_actual]['tabla_vars'][id_actual]['tipo']
    if tipo == 'int':
        dir_virtual = mapa.creaVarLocal('ptri')
    else:
        dir_virtual = mapa.creaVarLocal('ptrf')
    li = dir_constant(0,'ctei')
    ls = dir_constant(dir_func[funcion_actual]['tabla_vars'][id_actual]['dim'][0] - 1,'ctei')
    quads.genera('ver', d1, li, ls)
    dirB = dir_func[funcion_actual]['tabla_vars'][id_actual]['dir_virtual']
    quads.genera('+', dir_constant(dirB, 'ctei'), d1, dir_virtual)
    pila_operandos.append({'nombre': 'ptr',
                           'tipo' : tipo,
                           'dir_virtual' : '~' + str(dir_virtual)})

def p_matriz(p):
    '''matriz : CORIZQ expresion CORDER pop_dim
              | pop_dim'''
    global dir_func
    if len(p) > 2:
        if dir_func[funcion_actual]['tabla_vars'].get(id_actual) != None:
            if len(dir_func[funcion_actual]['tabla_vars'][id_actual]['dim']) < 2:
                print("Variable %s is vector not matrix" %(id_actual))
                sys.exit()
            else:
                matrix_def(funcion_actual)
        elif dir_func['global']['tabla_vars'].get(id_actual) != None:
            if len(dir_func['global']['tabla_vars'][id_actual]['dim']) < 2:
                print("Variable %s is vector not matrix" %(id_actual))
                sys.exit()
            else:
                matrix_def('global')
        else:
            print("Variable %s no declarada." %(id_actual))
            sys.exit()
    else:
        if dir_func[funcion_actual]['tabla_vars'].get(id_actual) != None:
            if len(dir_func[funcion_actual]['tabla_vars'][id_actual]['dim']) > 1:
                print("Variable %s is matrix not vector" %(id_actual))
                sys.exit()
            else:
                vect_def(funcion_actual)
        elif dir_func['global']['tabla_vars'].get(id_actual) != None:
            if len(dir_func['global']['tabla_vars'][id_actual]['dim']) > 1:
                print("Variable %s is matrix not vector" %(id_actual))
                sys.exit()
            else:
                vect_def('global')
        else:
            print("Variable %s no declarada." %(id_actual))
            sys.exit()

# Reglas sintacticas para estatutos y bloques.
def p_estatuto(p):
    '''estatuto : asignacion
                | condicion
                | escritura
                | ciclo
                | instruccion
                | func_call PUNTCOM
       bloque : BRAIZQ estatutos BRADER '''

# Reglas sintacticas para llamadas de funcion.
def p_func_call(p):
    '''func_call : ID actualiza_id actualiza_func PARIZQ args gen_era PARDER gen_gosub
       var_func_call : PARIZQ actualiza_func args gen_era PARDER gen_gosub
       args : expresion asig_par arg
            |
       arg : COMA args
           | '''

# Regla que actualiza la llamad a funcion actual y verifcia que exista en el directorio de funciones.
def p_actualiza_func(p):
    '''actualiza_func :'''
    global func_call
    global dir_func
    if dir_func.get(id_actual) != None:
        func_call.append({'func' : id_actual, 'pars' : []})
    else:
        print("Function %s not defined, functions must be defined before calling them."%(id_actual))
        sys.exit()

# Funcion que genera quadruplo era
def p_gen_era(p):
    '''gen_era : '''
    global quads
    global dir_func
    global num_args
    global func_call
    func_actual = func_call[-1]
    num_args = 0
    if dir_func.get(func_actual['func']) != None:
        quads.genera('era', None, None,  len(dir_func[func_actual['func']]['secuencia_par']))
    else:
        print("Function", func_actual['func']," not declared")
        sys.exit()

# Funcion que genera quadruplos gosub y param
def p_gen_gosub(p):
    '''gen_gosub : '''
    global quads
    global mapa
    global pila_operandos
    global func_call
    func_actual = func_call.pop()
    for pars in func_actual['pars']:
        quads.genera('param',pars[0], func_actual['func'], pars[1])
    quads.genera('gosub', None, func_actual['func'], dir_func[func_actual['func']]['dir_inicio'])
    tipo = dir_func[func_actual['func']]['tipo']
    if tipo != 'void':
        if tipo == 'int':
            retorno = mapa.creaVarLocal('tmpi')
        else:
            retorno = mapa.creaVarLocal('tmpf')
        quads.genera('=', None, None, retorno)
        pila_operandos.append({'nombre': retorno,
                               'tipo' : dir_func[func_actual['func']]['tipo'],
                               'dir_virtual' : retorno})

# Funcion para asignar direcciones virtuales a los parametros.
def p_asig_par(p):
    '''asig_par : '''
    global pila_operandos
    global dir_func
    global num_args
    global quads
    global func_call
    arg = pila_operandos.pop()
    func_actual = func_call[-1]
    pars = dir_func[func_actual['func']]['secuencia_par']
    tam = len(pars)
    if num_args < tam:
        if pars[tam - num_args - 1]['tipo'] == arg['tipo']:
            func_call[-1]['pars'].append([arg['dir_virtual'], pars[tam - num_args - 1]['dir_virtual']])
        else:
            print("Type Mismatch") 
            sys.exit()
    else:
        print("Function", func_actual['func'], "Wrong Number of Arguments", num_args, tam)
        sys.exit()
    num_args += 1

def p_asignacion(p):
    '''asignacion : ID actualiza_id lista ASIG exp_input PUNTCOM'''
    global quads
    global dir_func
    global pila_operandos
    global asig_input
    if asig_input:
        asig_input = False
        tempAsig = pila_operandos.pop()
        if dir_func[funcion_actual]['tabla_vars'].get(p[1]) == None and dir_func['global']['tabla_vars'].get(p[1]) == None:
            print("Variable %s no declarada." %(p[1]))
            sys.exit()
        quads.genera('input', None, None, tempAsig['dir_virtual'])
    else:
        tempRes = pila_operandos.pop()
        tempAsig = pila_operandos.pop()
        if dir_func[funcion_actual]['tabla_vars'].get(p[1]) == None and dir_func['global']['tabla_vars'].get(p[1]) == None:
            print("Variable %s no declarada." %(p[1]))
            sys.exit()
        if tempRes['tipo'] == 'int' or tempRes['tipo'] == 'float':
            quads.genera('=', tempRes['dir_virtual'], None, tempAsig['dir_virtual'])
        else:
            print('Type Mismatch')
            sys.exit()

def p_exp_input(p):
    '''exp_input : expresion'''

def p_input(p):
    '''exp_input : INPUT PARIZQ PARDER'''
    global asig_input
    asig_input = True

def p_condicion(p):
    '''condicion : IF PARIZQ expresion fin_exp PARDER bloque else_bloque fin_cond
       else_bloque : ELSE inicio_else bloque
                   | '''

# Funcion para rellenar el quadruplo con el fin condicion.
def p_fin_cond(p):
    '''fin_cond : '''
    global quads
    global pila_saltos
    quads.rellena(pila_saltos.pop())

# Funcion para marcar el inicio de un (else) generando el quadruplo goto.
def p_inicio_else(p):
    '''inicio_else : '''
    global quads
    global pila_saltos
    quads.genera('goto', None, None, None)
    falso = pila_saltos.pop()
    pila_saltos.append(quads.contador - 1)
    quads.rellena(falso)

# Funcion para rellenar el fin de expresion con el quadruplo gotof.
def p_fin_exp(p):
    '''fin_exp : '''
    global quads
    global pila_operandos
    global pila_saltos
    val_esp = pila_operandos.pop()
    if val_esp['tipo'] == 'int':
        quads.genera('gotof', val_esp['dir_virtual'], None, None)
        pila_saltos.append(quads.contador - 1)
    else:
        print("Type Mismatch") 
        sys.exit()

# Regla sintactica del ciclo.
def p_ciclo(p):
    '''ciclo : REPEAT push_cont PARIZQ expresion fin_exp PARDER bloque fin_repeat'''

# Funcion para meter el contador actual de quads en la pila de saltos.
def p_push_cont(p):
    '''push_cont : '''
    global quads
    global pila_saltos
    pila_saltos.append(quads.contador)

# Funcion para marcar el finc de ciclo generando el quadruplo goto.
def p_fin_repeat(p):
    '''fin_repeat : '''
    global quads
    global pila_saltos
    fin = pila_saltos.pop()
    retorno = pila_saltos.pop()
    quads.genera('goto', None, None, retorno)
    quads.rellena(fin)

# Reglas sintacticas de escritura.
def p_escritura(p):
    '''escritura : PRINT PARIZQ arg_escritura PARDER PUNTCOM
       arg_escritura : expresion fin_arg args_escritura
                     | CTE_STR print_string args_escritura
       args_escritura : COMA arg_escritura
                      | '''

# Funcion para generar el cuadruplo print con una expresion.
def p_fin_arg(p):
    '''fin_arg : '''
    global quads
    global pila_operandos
    val_esp = pila_operandos.pop()
    quads.genera('print', None, None, val_esp['dir_virtual'])

# Funcion para generar el cuadruplo print con una cadena.
def p_print_string(p):
    '''print_string : '''
    global quads
    quads.genera('print', None, None, p[-1])

# Reglas sintacticas para funciones de dibujo.
def p_instruccion(p):
    '''instruccion : FORWARD actualiza_instr PARIZQ expresion PARDER fin_instr1 PUNTCOM
                   | BACKWARD actualiza_instr PARIZQ expresion PARDER fin_instr1 PUNTCOM
                   | LEFT actualiza_instr PARIZQ expresion PARDER fin_instr1 PUNTCOM
                   | RIGHT actualiza_instr PARIZQ expresion PARDER fin_instr1 PUNTCOM
                   | TURN actualiza_instr PARIZQ expresion PARDER fin_instr1 PUNTCOM
                   | SIZE actualiza_instr PARIZQ expresion PARDER fin_instr1 PUNTCOM
                   | CIRCLE actualiza_instr PARIZQ expresion PARDER fin_instr1 transform PUNTCOM
                   | TRIANGLE actualiza_instr PARIZQ expresion PARDER fin_instr1 transform PUNTCOM
                   | SQUARE actualiza_instr PARIZQ expresion PARDER fin_instr1 transform PUNTCOM
                   | NGON actualiza_instr PARIZQ expresion COMA expresion PARDER fin_instr2 transform PUNTCOM
                   | ARC actualiza_instr PARIZQ expresion PARDER fin_instr1 transform PUNTCOM
                   | UP actualiza_instr PARIZQ PARDER fin_instr PUNTCOM
                   | DOWN actualiza_instr PARIZQ PARDER fin_instr PUNTCOM
                   | COLOR PARIZQ expresion COMA expresion COMA expresion PARDER fin_color PUNTCOM
       fill : FILL actualiza_instr PARIZQ PARDER fin_instr trans
            | altera trans
       trans : PUNTO altera trans
             | 
       altera : ROTATE actualiza_instr PARIZQ expresion PARDER fin_instr1
              | STRETCH actualiza_instr PARIZQ expresion PARDER fin_instr1'''

# Genera quadruplo dibuja.
def p_dibuja(p):
    '''transform : PUNTO fill
                 | '''
    quads.genera("draw", None, None, None)

# Actualiza instruccion de dibujo.
def p_actualiza_instr(p):
    '''actualiza_instr : '''
    global instr_actual
    instr_actual = p[-1]

# Actualiza instruccion de dibujo.
def p_fin_instr(p):
    '''fin_instr : '''
    global quads
    global instr_actual
    quads.genera(instr_actual, None, None, None)

# Marcar fin de instruccion con un parametro.
def p_fin_instr1(p):
    '''fin_instr1 : '''
    global instr_actual
    global quads
    global pila_operandos
    val1 = pila_operandos.pop()
    quads.genera(instr_actual, None, None, val1['dir_virtual'])

# Marcar fin de instruccion con dos parametros.
def p_fin_instr2(p):
    '''fin_instr2 : '''
    global instr_actual
    global quads
    global pila_operandos
    val2 = pila_operandos.pop()
    val1 = pila_operandos.pop()
    quads.genera(instr_actual, None, val1['dir_virtual'], val2['dir_virtual'])

# Marcar fin de instruccion para cambiar el color.
def p_fin_color(p):
    '''fin_color : '''
    global quads
    global pila_operandos
    val3 = pila_operandos.pop()
    val2 = pila_operandos.pop()
    val1 = pila_operandos.pop()
    quads.genera('color', val1['dir_virtual'], val2['dir_virtual'], val3['dir_virtual'])

def p_error(p):
    print("Syntax error at token " + str(p.type) + " lineno " + str(p.lineno))
    sys.exit()

# FUNCION PRINCIPAL PARA EVELUAR UN ARCHIVO DE TEXTO - python3 ProyectoFinal_Yacc.py archivo
def parse(file):
    lexer = scanner.lexer
    tokens = scanner.tokens
    parser = yacc.yacc()
    file = open(file, 'r')
    data=file.read()
    file.close()
    parser.parse(data)
    # return [dir_func, tabla_constantes, quads.quads, mapa.vals]
    return [tabla_constantes, quads.quads, mapa.vals]
'''
def main():
    temp = parse(str(sys.argv[1]))
    i = 1
    for q in quads.quads:
        print(i, q)
        i += 1

if __name__ == '__main__':
    main()
'''