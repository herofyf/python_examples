from PygameTest.main import *

donePrint = False
def cube(t):
    vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )
    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 7),
        (6, 3),
        (6, 4),
        (6, 7),
        (5, 1),
        (5, 4),
        (5, 7)
    )
    global donePrint
    glBegin(GL_LINES)
    for i in range(2):
        edge = edges[i]
        for vertex in edge:
            glColor3f(0.0, 1.0, 1.0)
            v = vertices[vertex]
            v = t.transform_vertex(v)
            if donePrint == False:
                print(v)
            glVertex3fv(v)

    if donePrint == False:
        donePrint = True

    glEnd()


class RenderCube(RenderContext):
    def render_object(self):
        t1 = self.get_world_transform()
        t2 = Translation(0, 0, -5)
        cube(t1)


rc = RenderCube()
t = Translation(0, 0, -5)
rc.add_world_transform(t)
main(rc)