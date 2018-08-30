import numpy as np

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({}, {}, {})" .format(self.x, self.y, self.z)

    def __repr__(self):
        return "{}{}" .format(self.__class__.__name__, str(self))

    def __add__(self, other):
        if isinstance(other, Vector3D):
            return self.__class__(self.x + other.x,
                                  self.y + other.y,
                                  self.z + other.z)
        else:
            raise TypeError("Can not add vector and {}." .format(type(other)))

    def __sub__(self, other):
        return self.__class__(self.x - other.x,
                              self.y - other.y,
                              self.z - other.z)

    def __neg__(self):
        return self.__class__(-self.x, -self.y, -self.z)

    def dot(self, other):
        if isinstance(other,self.__class__):
            return self.x*other.x + self.y*other.y + self.z*other.z
        elif isinstance(other, int):
            return self.x*other + self.y*other + self.z*other

    def __mul__(self, other):
        return self.dot(other)

    def __rmul__(self, other):
        return self.__mul__

    def cross(self, other):
        x = self.y*other.z - self.z*other.y
        y = self.z*other.x - self.x*other.z
        z = self.x*other.y - self.y*other.x
        return self.__class__(x, y, z)

    def __matmul__(self, other):
        return self.cross(other)

    def perpendicular(self, other):
        return np.isclose(self*other, 0)

    @property
    def length(self):
        return np.sqrt(self*self)

    @length.setter
    def length(self, new_length):
        scale = new_length/self.new_length
        sef.x *= scale
        sef.y *= scale
        sef.z *= scale
        return np.sqrt(self*self)

    @property
    def unit_vector(self):
        new_vector = self.__class__(self.x, self.y, self.z)
        new_vector.length = 1
        return new_vector

u = Vector3D(2, 2, 0)
v = Vector3D(1, 0, 1)
w = u - v

print(u*v)
print(u@v)

print(w.length)
