# Proyecto Final - Compiladores
# Autores: Carmelo Ramirez (A01175987) y Juan Pablo Galaz (A01251406)
import ProyectoFinal_Yacc as parser
import MapaMemoria
import sys
import turtle
import math


dir_func = {}
quads = []
stack_pointer = 0
mem = None
func_reg = 0

def load_constantes(tabla_constantes):
    global mem
    for val in tabla_constantes:
        mem.insert(tabla_constantes[val], val)

def main():
    global dir_func
    global quads
    global stack_pointer
    global mem
    global func_reg
    dir_func, tabla_constantes, quads, val = parser.parse(str(sys.argv[1]))
    mem = MapaMemoria.MapaMemoria(val[0], val[1], val[2], val[3], val[4], val[5], 40000)
    load_constantes(tabla_constantes)
    '''
    i = 1
    for q in quads:
        print(i, q)
        i += 1
    print('---------------------------------')
    '''
    myTurtle = turtle.Turtle(shape="turtle")
    screen = turtle.getscreen()
    fill = False
    #Function to close Turtle Window
    def close():
        turtle.bye()
    # When clicking SPACE, close Turtle Window
    screen.onkeypress(close, "space")
    screen.listen()

    while quads[stack_pointer][0] != 10:
        # print(quads[stack_pointer])
        if quads[stack_pointer][0] == 0:
            # canvas crear una imagen
            width = int(mem.find(quads[stack_pointer][2]))
            height = int(mem.find(quads[stack_pointer][2]))
            screen.screensize(width,height)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 1:
            # background color de imagen
            r = int(mem.find(quads[stack_pointer][1]))
            g = int(mem.find(quads[stack_pointer][2]))
            b = int(mem.find(quads[stack_pointer][3]))
            screen.colormode(255)
            screen.bgcolor(r, g, b)
            screen.update()
            stack_pointer += 1
        elif quads[stack_pointer][0] == 2:
            # import abrir una imagen
            '''
            image = quads[stack_pointer][3][1:-1]
            print(image)
            screen.setup(720, 1334)
            screen.bgpic("image.jpg")
            screen.update()
            '''
            stack_pointer += 1
        elif quads[stack_pointer][0] == 3:
            # endproc
            stack_pointer = mem.endproc()
        elif quads[stack_pointer][0] == 4:
            # return
            func_reg = mem.find(quads[stack_pointer][3])
            stack_pointer += 1
        elif quads[stack_pointer][0] == 5:
            # ver
            index = mem.find(quads[stack_pointer][1])
            li = mem.find(quads[stack_pointer][2])
            ls = mem.find(quads[stack_pointer][3])
            if index < li or index > ls:
                print("Out of index")
                sys.exit()
            stack_pointer += 1
        elif quads[stack_pointer][0] == 6:
            # goto 
            stack_pointer = quads[stack_pointer][3] - 1
        elif quads[stack_pointer][0] == 7:
            # era
            mem.era(quads[stack_pointer][3])
            stack_pointer += 1
        elif quads[stack_pointer][0] == 8:
            # gosub
            mem.gosub(stack_pointer)
            stack_pointer = quads[stack_pointer][3] - 1
        elif quads[stack_pointer][0] == 9:
            # param
            mem.param(mem.find(quads[stack_pointer][1]), quads[stack_pointer][3])
            stack_pointer += 1
        elif quads[stack_pointer][0] == 11:
            # gotof
            val = mem.find(quads[stack_pointer][1])
            if val == 0:
                stack_pointer = quads[stack_pointer][3] - 1
            else:
                stack_pointer += 1
        elif quads[stack_pointer][0] == 12:
            # print
            opdo = quads[stack_pointer][3]
            if type(opdo) is str:
                if opdo[0] == '~':
                    print(mem.find(opdo), end='')            
                else:
                    if len(opdo[1:-1]) == 0:
                        print("")
                    else:
                        print(opdo[1:-1], end='')
            else:
                print(mem.find(opdo), end='')
            stack_pointer += 1
        elif quads[stack_pointer][0] == 13:
            # color cambiar color
            r = mem.find(quads[stack_pointer][1])
            g = mem.find(quads[stack_pointer][2])
            b = mem.find(quads[stack_pointer][3])
            myTurtle.pencolor(r,g,b)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 14:
            # forward
            dist = mem.find(quads[stack_pointer][3])
            myTurtle.forward(dist)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 15:
            # backward
            dist = mem.find(quads[stack_pointer][3])
            myTurtle.backward(dist)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 16:
            # left
            angulo = mem.find(quads[stack_pointer][3])
            myTurtle.left(angulo)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 17:
            # right
            angulo = mem.find(quads[stack_pointer][3])
            myTurtle.right(angulo)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 18:
            # turn
            angulo = mem.find(quads[stack_pointer][3])
            myTurtle.right(angulo)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 19:
            # size
            tam = mem.find(quads[stack_pointer][3])
            myTurtle.pensize(tam)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 20:
            # circle
            tamCircle = mem.find(quads[stack_pointer][3])
            myTurtle.circle(tamCircle)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 21:
            # triangle
            size = mem.find(quads[stack_pointer][3])
            for i in range(3):
                myTurtle.forward(size)
                myTurtle.left(120)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 22:
            # square
            dim = mem.find(quads[stack_pointer][3])
            tam_lados = math.sqrt(dim)
            #dibujar cuadrado
            for i in range(4):
                myTurtle.forward(tam_lados)
                myTurtle.left(90)

            stack_pointer += 1
        elif quads[stack_pointer][0] == 23:
            # ngon
            num_sides = mem.find(quads[stack_pointer][3])
            angle = 360.0 / num_sides
            for i in range(num_sides):
                myTurtle.forward(70)
                myTurtle.right(angle)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 24:
            # arc
            radius = mem.find(quads[stack_pointer][3])
            myTurtle.circle(radius, 180)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 25:
            # up
            myTurtle.penup()
            stack_pointer += 1
        elif quads[stack_pointer][0] == 26:
            # down
            myTurtle.pendown()
            stack_pointer += 1
        elif quads[stack_pointer][0] == 27:
            # rotate
            stack_pointer += 1
        elif quads[stack_pointer][0] == 28:
            # stretch
            stack_pointer += 1
        elif quads[stack_pointer][0] == 29:
            # fill
            fill = True
            stack_pointer += 1
        elif quads[stack_pointer][0] == 30:
            # ||
            op1 = mem.find(quads[stack_pointer][1])
            op2 = mem.find(quads[stack_pointer][2])
            if op1 != 0 or op2 != 0:
                mem.insert(quads[stack_pointer][3], 1)
            else:
                mem.insert(quads[stack_pointer][3], 0)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 31:
            # &&
            op1 = mem.find(quads[stack_pointer][1])
            op2 = mem.find(quads[stack_pointer][2])
            if op1 != 0 and op2 != 0:
                mem.insert(quads[stack_pointer][3], 1)
            else:
                mem.insert(quads[stack_pointer][3], 0)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 32:
            # !=
            op1 = mem.find(quads[stack_pointer][1])
            op2 = mem.find(quads[stack_pointer][2])
            if op1 != op2:
                mem.insert(quads[stack_pointer][3], 1)
            else:
                mem.insert(quads[stack_pointer][3], 0)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 33:
            # <
            op1 = mem.find(quads[stack_pointer][1])
            op2 = mem.find(quads[stack_pointer][2])
            if op1 < op2:
                mem.insert(quads[stack_pointer][3], 1)
            else:
                mem.insert(quads[stack_pointer][3], 0)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 34:
            # > 
            op1 = mem.find(quads[stack_pointer][1])
            op2 = mem.find(quads[stack_pointer][2])
            if op1 > op2:
                mem.insert(quads[stack_pointer][3], 1)
            else:
                mem.insert(quads[stack_pointer][3], 0)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 35:
            # ==
            op1 = mem.find(quads[stack_pointer][1])
            op2 = mem.find(quads[stack_pointer][2])
            if op1 == op2:
                mem.insert(quads[stack_pointer][3], 1)
            else:
                mem.insert(quads[stack_pointer][3], 0)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 36:
            # <=
            op1 = mem.find(quads[stack_pointer][1])
            op2 = mem.find(quads[stack_pointer][2])
            if op1 <= op2:
                mem.insert(quads[stack_pointer][3], 1)
            else:
                mem.insert(quads[stack_pointer][3], 0)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 37:
            # >=
            op1 = mem.find(quads[stack_pointer][1])
            op2 = mem.find(quads[stack_pointer][2])
            if op1 >= op2:
                mem.insert(quads[stack_pointer][3], 1)
            else:
                mem.insert(quads[stack_pointer][3], 0)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 38:
            # +
            op1 = mem.find(quads[stack_pointer][1])
            op2 = mem.find(quads[stack_pointer][2])
            mem.insert(quads[stack_pointer][3], op1 + op2)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 39:
            # -
            op1 = mem.find(quads[stack_pointer][1])
            op2 = mem.find(quads[stack_pointer][2])
            mem.insert(quads[stack_pointer][3], op1 - op2)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 40:
            # *
            op1 = mem.find(quads[stack_pointer][1])
            op2 = mem.find(quads[stack_pointer][2])
            mem.insert(quads[stack_pointer][3], op1 * op2)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 41:
            # /
            op1 = mem.find(quads[stack_pointer][1])
            op2 = mem.find(quads[stack_pointer][2])
            if op2 == 0:
                print('Division by zero')
                sys.exit()
            mem.insert(quads[stack_pointer][3], op1/op2)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 42:
            # =
            if quads[stack_pointer][1] == None:
                mem.insert(quads[stack_pointer][3], func_reg)
            else:
                op1 = mem.find(quads[stack_pointer][1])
                mem.insert(quads[stack_pointer][3], op1)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 43:
            # %
            op1 = mem.find(quads[stack_pointer][1])
            op2 = mem.find(quads[stack_pointer][2])
            if op2 == 0:
                print('Division by zero')
                sys.exit()
            mem.insert(quads[stack_pointer][3], op1%op2)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 44:
            # input
            op1 = input()
            try:
                op1 = int(op1)
            except ValueError:
                print("Inputs must be numeric")
                sys.exit()
            mem.insert(quads[stack_pointer][3], op1)
            stack_pointer += 1
        elif quads[stack_pointer][0] == 45:
            # module
            screen.title(quads[stack_pointer][3][1:-1])
            stack_pointer += 1
        elif quads[stack_pointer][0] == 46:
            # draw
            stack_pointer += 1
        else:
            print(quads[stack_pointer])
            print('Error')
            sys.exit()
    # print(quads[stack_pointer])
    # print(mem.mapa_memoria)

    #INICIA APLICACION TURTLE
    screen._root.mainloop()
   # screen.getcanvas().postscript(file="temp.ps")

if __name__ == '__main__':
    main()