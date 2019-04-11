'''
实现二维向量
'''

import math

class Vector2(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    @classmethod
    def from_points(cls, P1, P2): #这里用classmethod装饰器，因为我们需要传入的不是x，y，而是两个点，可是我们又需要用到Vector2类的值
        return cls(P2[0]-P1[0], P2[1] - P1[1])

    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude

    def __vectorAdd__(self, rhs):
        return Vector2(self.x + rhs.x, self.y + rhs.y)

    def __vectorSub__(self, rhs):
        return Vector2(self.x - rhs.x, self.y - rhs.y)

    def __vectorMul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __vectorDiv__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)



if __name__ == '__main__':
    A = (10.0, 20.0)
    B = (30.0, 35.0)
    AB = Vector2.from_points(A, B)

    v = Vector2(20, 15)
    v_magnitude = v.get_magnitude()

    v2 = Vector2(10, 10)
    vaddv2 = v.__vectorAdd__(v2)
    vsubv2 = v.__vectorSub__(v2)
    vmulv2 = v.__vectorMul__(2)
    vdivv2 = v.__vectorDiv__(2)
    v.normalize()

    print(AB, v_magnitude, v, vaddv2, vsubv2, vmulv2, vdivv2)