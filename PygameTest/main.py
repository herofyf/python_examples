import pygame as pg
import OpenGL
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PygameTest.transform import *


class RenderContext:
    def __init__(self, w = 800, h = 600, title = "3D Test"):
        self.w_width = w
        self.w_height = h
        self.w_title = title
        self.world_transform_actions = []
        self.view_transform_actions = []
        self.pers_angle = 45
        self.pers_near = 0.1
        self.pers_far = 50

    def init(self):
        self.set_perspective(self.pers_angle, self.pers_near, self.pers_far)

    def set_perspective(self, angle, near, far):
        self.pers_angle = angle
        self.pers_near = near
        self.pers_far = far
        gluPerspective(self.pers_angle, (self.w_width / self.w_height), self.pers_near, self.pers_far)

    def add_world_transform(self, transform):
        self.world_transform_actions.append(transform)

    def get_world_transform(self):
        work_transform = Transform()
        for t in self.world_transform_actions:
            work_transform.combine_matrix(t)

        return work_transform

    def render_object(self):
        pass

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.render_object()
        pg.display.flip()

    def on_mouse_evt(self):
        pass

def main(renderContext):
    pg.init()
    display = (renderContext.w_width, renderContext.w_height)
    gameDisplay = pg.display.set_mode(display, DOUBLEBUF|OPENGL)
    pg.display.set_caption(renderContext.w_title)

    renderContext.init()

    clock = pg.time.Clock()

    crashed = False
    while not crashed:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                crashed = True
            # print(event)
            #glRotatef(15, 0, 0, 1)
            #glTranslatef(0.0, 0.0, step)
            renderContext.on_mouse_evt()

        # update our display
        renderContext.render()




