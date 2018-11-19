# Proyecto Final - Compiladores
# Autores: Carmelo Ramirez (A01175987) y Juan Pablo Galaz (A01251406)
import imageio
import math
import sys
import turtle
import MapaMemoria
import ProyectoFinal_Yacc as parser
import Shapes

# cuadruplos generados
quads = []
# instruction pointer
instruction_pointer = 0
# mapa de memoria
mem = None
# registro de funcion, contiene el valor de retorno de una funcion durante el cambio de contexto
func_reg = 0
# figura a dibujar
shape = Shapes.Shape()

# metera las constantes en el mapa de memoria
def load_constantes(tabla_constantes):
    global mem
    for val in tabla_constantes:
        mem.insert(tabla_constantes[val], val)

def main():
    global quads
    global instruction_pointer
    global mem
    global func_reg
    tabla_constantes, quads, direcciones = parser.parse(str(sys.argv[1]))
    mem = MapaMemoria.MapaMemoria(direcciones[0], direcciones[1], direcciones[2],
                                  direcciones[3], direcciones[4], direcciones[5],
                                  80000)
    load_constantes(tabla_constantes)
    myTurtle = turtle.Turtle(shape="classic")
    screen = turtle.getscreen()
    screen.colormode(255)
    fill = False
    arc = False
    #Function to close Turtle Window
    def close():
        turtle.bye()
        sys.exit()
    screen.listen()
    while quads[instruction_pointer][0] != 10:
        if quads[instruction_pointer][0] == 0:
            # canvas crear una imagen
            width = int(mem.find(quads[instruction_pointer][2]))
            height = int(mem.find(quads[instruction_pointer][2]))
            screen.setup(width,height)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 1:
            # background color de imagen
            r = int(mem.find(quads[instruction_pointer][1]))
            g = int(mem.find(quads[instruction_pointer][2]))
            b = int(mem.find(quads[instruction_pointer][3]))
            screen.bgcolor(r, g, b)
            screen.update()
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 2:
            # import abrir una imagen
            try:
                image = imageio.imread(quads[instruction_pointer][3][1:-1])
                height, width, _ = image.shape
                imageio.mimsave('temp.gif', [image])
                screen.setup(width, height)
                screen.bgpic('temp.gif')
            except FileNotFoundError:
                print("File %s Not Found" %(quads[instruction_pointer][3][1:-1]))
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 3:
            # endproc
            instruction_pointer = mem.endproc()
        elif quads[instruction_pointer][0] == 4:
            # return
            func_reg = mem.find(quads[instruction_pointer][3])
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 5:
            # ver
            index = mem.find(quads[instruction_pointer][1])
            li = mem.find(quads[instruction_pointer][2])
            ls = mem.find(quads[instruction_pointer][3])
            if index < li or index > ls:
                print("Out of index")
                sys.exit()
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 6:
            # goto 
            instruction_pointer = quads[instruction_pointer][3] - 1
        elif quads[instruction_pointer][0] == 7:
            # era
            mem.era(quads[instruction_pointer][3])
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 8:
            # gosub
            mem.gosub(instruction_pointer)
            instruction_pointer = quads[instruction_pointer][3] - 1
        elif quads[instruction_pointer][0] == 9:
            # param
            mem.param(mem.find(quads[instruction_pointer][1]), quads[instruction_pointer][3])
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 11:
            # gotof
            val = mem.find(quads[instruction_pointer][1])
            if val == 0:
                instruction_pointer = quads[instruction_pointer][3] - 1
            else:
                instruction_pointer += 1
        elif quads[instruction_pointer][0] == 12:
            # print
            opdo = quads[instruction_pointer][3]
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
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 13:
            # color cambiar color
            r = int(mem.find(quads[instruction_pointer][1]))
            g = int(mem.find(quads[instruction_pointer][2]))
            b = int(mem.find(quads[instruction_pointer][3]))
            myTurtle.pencolor(r,g,b)
            myTurtle.fillcolor(r,g,b)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 14:
            # forward
            dist = mem.find(quads[instruction_pointer][3])
            myTurtle.forward(dist)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 15:
            # backward
            dist = mem.find(quads[instruction_pointer][3])
            myTurtle.backward(dist)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 16:
            # left
            dist = mem.find(quads[instruction_pointer][3])
            myTurtle.left(90)
            myTurtle.forward(dist)
            myTurtle.left(-90)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 17:
            # right
            angulo = mem.find(quads[instruction_pointer][3])
            dist = mem.find(quads[instruction_pointer][3])
            myTurtle.right(90)
            myTurtle.forward(dist)
            myTurtle.right(-90)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 18:
            # turn
            angulo = mem.find(quads[instruction_pointer][3])
            myTurtle.right(angulo)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 19:
            # size
            tam = mem.find(quads[instruction_pointer][3])
            myTurtle.pensize(tam)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 20:
            # circle
            dim = mem.find(quads[instruction_pointer][3])
            shape.gen_points(30)
            shape.scale(dim)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 21:
            # triangle
            dim = mem.find(quads[instruction_pointer][3])
            shape.gen_points(3)
            shape.scale(dim)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 22:
            # square
            dim = mem.find(quads[instruction_pointer][3])
            shape.gen_points(4)
            shape.scale(dim)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 23:
            # ngon
            num_sides = mem.find(quads[instruction_pointer][2])
            dim = mem.find(quads[instruction_pointer][3])
            shape.gen_points(num_sides)
            shape.scale(dim)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 24:
            # arc
            arc = True
            dim = mem.find(quads[instruction_pointer][3])
            shape.gen_points(30, arc)
            shape.scale(dim)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 25:
            # up
            myTurtle.penup()
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 26:
            # down
            myTurtle.pendown()
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 27:
            # rotate
            angle = float(mem.find(quads[instruction_pointer][3]))
            shape.rotate(angle)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 28:
            # stretch
            dim = float(mem.find(quads[instruction_pointer][3]))
            shape.stretch(dim)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 29:
            # fill
            fill = True
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 30:
            # |
            op1 = mem.find(quads[instruction_pointer][1])
            op2 = mem.find(quads[instruction_pointer][2])
            if op1 != 0 or op2 != 0:
                mem.insert(quads[instruction_pointer][3], 1)
            else:
                mem.insert(quads[instruction_pointer][3], 0)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 31:
            # &
            op1 = mem.find(quads[instruction_pointer][1])
            op2 = mem.find(quads[instruction_pointer][2])
            if op1 != 0 and op2 != 0:
                mem.insert(quads[instruction_pointer][3], 1)
            else:
                mem.insert(quads[instruction_pointer][3], 0)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 32:
            # !=
            op1 = mem.find(quads[instruction_pointer][1])
            op2 = mem.find(quads[instruction_pointer][2])
            if op1 != op2:
                mem.insert(quads[instruction_pointer][3], 1)
            else:
                mem.insert(quads[instruction_pointer][3], 0)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 33:
            # <
            op1 = mem.find(quads[instruction_pointer][1])
            op2 = mem.find(quads[instruction_pointer][2])
            if op1 < op2:
                mem.insert(quads[instruction_pointer][3], 1)
            else:
                mem.insert(quads[instruction_pointer][3], 0)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 34:
            # > 
            op1 = mem.find(quads[instruction_pointer][1])
            op2 = mem.find(quads[instruction_pointer][2])
            if op1 > op2:
                mem.insert(quads[instruction_pointer][3], 1)
            else:
                mem.insert(quads[instruction_pointer][3], 0)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 35:
            # ==
            op1 = mem.find(quads[instruction_pointer][1])
            op2 = mem.find(quads[instruction_pointer][2])
            if op1 == op2:
                mem.insert(quads[instruction_pointer][3], 1)
            else:
                mem.insert(quads[instruction_pointer][3], 0)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 36:
            # <=
            op1 = mem.find(quads[instruction_pointer][1])
            op2 = mem.find(quads[instruction_pointer][2])
            if op1 <= op2:
                mem.insert(quads[instruction_pointer][3], 1)
            else:
                mem.insert(quads[instruction_pointer][3], 0)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 37:
            # >=
            op1 = mem.find(quads[instruction_pointer][1])
            op2 = mem.find(quads[instruction_pointer][2])
            if op1 >= op2:
                mem.insert(quads[instruction_pointer][3], 1)
            else:
                mem.insert(quads[instruction_pointer][3], 0)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 38:
            # +
            op1 = mem.find(quads[instruction_pointer][1])
            op2 = mem.find(quads[instruction_pointer][2])
            mem.insert(quads[instruction_pointer][3], op1 + op2)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 39:
            # -
            op1 = mem.find(quads[instruction_pointer][1])
            op2 = mem.find(quads[instruction_pointer][2])
            mem.insert(quads[instruction_pointer][3], op1 - op2)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 40:
            # *
            op1 = mem.find(quads[instruction_pointer][1])
            op2 = mem.find(quads[instruction_pointer][2])
            mem.insert(quads[instruction_pointer][3], op1 * op2)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 41:
            # /
            op1 = mem.find(quads[instruction_pointer][1])
            op2 = mem.find(quads[instruction_pointer][2])
            if op2 == 0:
                print('Division by zero')
                sys.exit()
            mem.insert(quads[instruction_pointer][3], op1/op2)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 42:
            # =
            if quads[instruction_pointer][1] == None:
                mem.insert(quads[instruction_pointer][3], func_reg)
            else:
                op1 = mem.find(quads[instruction_pointer][1])
                mem.insert(quads[instruction_pointer][3], op1)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 43:
            # %
            op1 = mem.find(quads[instruction_pointer][1])
            op2 = mem.find(quads[instruction_pointer][2])
            if op2 == 0:
                print('Division by zero')
                sys.exit()
            mem.insert(quads[instruction_pointer][3], op1%op2)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 44:
            # input
            op1 = input()
            try:
                op1 = float(op1)
            except ValueError:
                print("Inputs must be numeric")
                sys.exit()
            mem.insert(quads[instruction_pointer][3], op1)
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 45:
            # module
            screen.title(quads[instruction_pointer][3][1:-1])
            instruction_pointer += 1
        elif quads[instruction_pointer][0] == 46:
            # draw
            myTurtle.pendown()
            x = myTurtle.xcor()
            y = myTurtle.ycor()
            if fill:
                myTurtle.begin_fill()
            for i in range(len(shape.points[0])):
                myTurtle.goto(x + shape.points[0][i], y + shape.points[1][i])
            if arc:
                arc = False
            else:
                myTurtle.goto(x, y)
            if fill:
                myTurtle.end_fill()
            fill = False
            shape.points = []
            instruction_pointer += 1
        else:
            print(quads[instruction_pointer])
            print('Error')
            sys.exit()
    # When clicking SPACE, close Turtle Window
    screen.onkeypress(close, "space")
    #INICIA APLICACION TURTLE
    screen.mainloop()

if __name__ == '__main__':
    main()