import numpy as np

class Shape:
    def __init__(self):
        self.points = []
        self.distortion_matrix = np.eye(2)
    def rotate(self, theta):
        cos = np.cos(theta)
        sin = np.sin(theta)
        self.distortion_matrix[0,0] = cos
        self.distortion_matrix[0,1] = -sin
        self.distortion_matrix[1,0] = sin
        self.distortion_matrix[1,1] = cos
        self.points = np.matmul(self.distortion_matrix, self.points)
    def scale(self, x):
        self.points = np.diag([x, x]).dot(self.points)
    def stretch(self, x):
        self.distortion_matrix[0,0] = x
        self.distortion_matrix[0,1] = 0
        self.distortion_matrix[1,0] = 0
        self.distortion_matrix[1,1] = 1
        self.points = np.matmul(self.distortion_matrix, self.points)
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
            y += np.sin(angle)
            x += np.cos(angle)
            angle += diff
        self.points = np.transpose(np.asarray(self.points))
    