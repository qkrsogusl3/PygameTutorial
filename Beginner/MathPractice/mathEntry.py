import pygame
from OpenGL.raw.GLU import gluPerspective
from pygame.locals import *
from OpenGL.GL import *
from MathPractice.exam_dotproduct import update as dotUpdate


def main(funcUpdate):
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45,(display[0]/display[1]),0.1,50.0)

    glTranslatef(0.0,0.0,-5)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        funcUpdate()

        pygame.display.flip()
        pygame.time.wait(10)



main(dotUpdate)