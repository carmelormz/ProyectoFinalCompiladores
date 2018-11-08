# Proyecto Final - Compiladores
# Autores: Carmelo Ramirez (A01175987) y Juan Pablo Galaz (A01251406)
import ProyectoFinal_Yacc as parser
import sys
dir_func = {}
tabla_constantes = {}
quads = []
stack_pointer = 0
'''
'int': lI, 'float': lF,
                           'tmpi': lTI, 'tmpf': lTF,
                           'ptri': lPI, 'ptrf': lPF,}
        self.globales = {'int': gI, 'float': gF,
                         'ctei': gCI, 'ctef': gCF}
    MapaDeMemoria {''}
'''
def main():
    global dir_func
    global tabla_constantes
    global quads
    global stack_pointer
    dir_func, tabla_constantes, quads = parser.parse(str(sys.argv[1]))
    while quads[stack_pointer][0] != 10:
        if quads[stack_pointer][0] == 0:
            # canvas crear una imagen
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 1:
            # background color de imagen
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 2:
            # import abrir una imagen
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 3:
            # endproc
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 4:
            # return
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 5:
            # ver
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 6:
            # goto 
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 7:
            # era
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 8:
            # gosub
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 9:
            # param
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 11:
            # gotof
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 12:
            # print
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 13:
            # color cambiar color
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 14:
            # forward
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 15:
            # backward
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 16:
            # left
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 17:
            # right
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 18:
            # turn
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 19:
            # size
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 20:
            # circle
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 21:
            # triangle
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 22:
            # square
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 23:
            # ngon
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 24:
            # arc
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 25:
            # up
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 26:
            # down
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 27:
            # rotate
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 28:
            # stretch
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 29:
            # fill
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 30:
            # ||
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 31:
            # &&
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 32:
            # !=
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 33:
            # <
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 34:
            # > 
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 35:
            # ==
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 36:
            # <=
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 37:
            # >= 
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 38:
            # +
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 39:
            # -
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 40:
            # *
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 41:
            # /
            print(quads[stack_pointer])
        elif quads[stack_pointer][0] == 42:
            # =
            print(quads[stack_pointer])
        else:
            print('Error')
            sys.exit()
        stack_pointer += 1

if __name__ == '__main__':
    main()