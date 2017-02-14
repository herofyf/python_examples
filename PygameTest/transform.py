import numpy as np

class Transform:
    def __init__(self):
        self.transform_matrix = Transform.identify_mat()

    @classmethod
    def identify_mat(cls):
        return np.array(
                    [
                        [1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1],
                    ]
                    )

    def transform_vertex(self, vertex):
        if isinstance(vertex, list) or isinstance(vertex, tuple):
            lpt = list(vertex)
        else:
            raise Exception("should be tuple type")

        lpt.append(1)
        pt_matrix = np.array(lpt)
        ret = np.dot(self.transform_matrix, pt_matrix)
        ret = ret[0:3].tolist()
        return tuple(ret)

    def combine_matrix(self, transform):
        if isinstance(transform, Transform) is False:
            return

        self.transform_matrix = np.dot(self.transform_matrix, transform.transform_matrix)


class Translation(Transform):
    def __init__(self, dx = 0, dy = 0, dz = 0):
        Transform.__init__(self)
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.transform_matrix = np.array(
                    [
                        [1, 0, 0, self.dx],
                        [0, 1, 0, self.dy],
                        [0, 0, 1, self.dz],
                        [0, 0, 0, 1],
                    ]
                )

class ScaleTransform(Transform):
    def __init__(self, sx = 0, sy = 0, sz = 0):
        Transform.__init__(self)
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.transform_matrix = np.array(
                    [
                        [1 + sx, 0, 0, 0],
                        [0, 1 + sy, 0, 0],
                        [0, 0, 1 + sz, 0],
                        [0, 0, 0,      1],
                    ]
                )

class RotateTransform(Transform):
    def __init__(self):
        Transform.__init__(self)



class RotateXTransform(RotateTransform):
    def __init__(self, rx = 0):
        RotateTransform.__init__(self)
        self.rx = rx
        c = np.cos(rx)
        s = np.sin(rx)
        self.transform_matrix = np.array(
            [
                [1, 0, 0, 0],
                [0, c, s, 0],
                [0, -s, c, 0],
                [0, 0, 0, 1]
            ]
        )

class RotateYTransform(RotateTransform):
    def __init__(self, ry = 0):
        RotateTransform.__init__(self)
        self.ry = ry
        c = np.cos(ry)
        s = np.sin(ry)
        self.transform_matrix = np.array(
            [
                [c, 0, -s, 0],
                [0, 1, 0, 0],
                [-s, 0, c, 0],
                [0, 0, 0, 1]
            ]
        )

class RotateZTransform(RotateTransform):
    def __init__(self, rz = 0):
        RotateTransform.__init__(self)
        self.rz = rz
        c = np.cos(rz)
        s = np.sin(rz)
        self.transform_matrix = np.array(
            [
                [c, s, 0, 0],
                [-s, c, 0,  0],
                [0, 0, 1, 0],
                [0, 0, 0,  1]
            ]
        )

'''
ts = []
ts.append(Translation(1, 1, 1))
ts.append(Translation(1, 1, 1))
m = Translation()
vertex = (0, 1, 0)
for t in ts:
    m.combine_matrix(t)
print(m.transform_vertex(vertex))
'''