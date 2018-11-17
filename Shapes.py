import numpy as np
# Proyecto Final - Compiladores
# Autores: Carmelo Ramirez (A01175987) y Juan Pablo Galaz (A01251406)
'''
    Clase Shape
        Clase para tener figuras a dibujar.
    Variables:
        points, los puntos de la figura.
        distortion_matrix, matriz de alguna transformacion
    Metodos:
        __init__()
        rotate()
        scale()
        stretch()
        gen_points()

'''
class Shape:
    '''
        __init__()
            Constructor inicial que define una matriz vacia para los puntos.
        Parametros:
            Sin parametros
        Retorno:
            Nada
    '''
    def __init__(self):
        self.points = []
        self.distortion_matrix = np.eye(2)
    '''
        rotate()
            Metodo para rotar la matriz de puntos theta grados.
        Parametros:
            Theta, grado de rotacion
        Retorno:
            Nada
    '''
    def rotate(self, theta):
        cos = np.cos(theta)
        sin = np.sin(theta)
        self.distortion_matrix[0,0] = cos
        self.distortion_matrix[0,1] = -sin
        self.distortion_matrix[1,0] = sin
        self.distortion_matrix[1,1] = cos
        self.points = np.matmul(self.distortion_matrix, self.points)
    '''
        scale()
            Metodo para escalar la matriz de puntos por x.
        Parametros:
            x, escala
        Retorno:
            Nada
    '''
    def scale(self, x):
        self.points = np.diag([x, x]).dot(self.points)
    '''
        stretch()
            Metodo para escalar la matriz por x en el eje x.
        Parametros:
            x, escala
        Retorno:
            Nada
    '''
    def stretch(self, x):
        self.distortion_matrix[0,0] = x
        self.distortion_matrix[0,1] = 0
        self.distortion_matrix[1,0] = 0
        self.distortion_matrix[1,1] = 1
        self.points = np.matmul(self.distortion_matrix, self.points)
    '''
        gen_points()
            Metodo para generar n puntos de una figura.
        Parametros:
            num_sides, numero de lados
        Retorno:
            Nada
    '''
    def gen_points(self, num_sides, arc=False):
        if num_sides < 3:
            num_sides = 3
        if num_sides > 30:
            num_sides = 30
        diff = (2*np.pi / num_sides)
        if arc:
            num_sides = int(num_sides/2)
        x = 0
        y = 0
        angle = 0
        for i in range(num_sides):
            self.points.append([x,y])
            y += 20*np.sin(angle)/num_sides
            x += 20*np.cos(angle)/num_sides
            angle += diff
        self.points = np.transpose(np.asarray(self.points))
    