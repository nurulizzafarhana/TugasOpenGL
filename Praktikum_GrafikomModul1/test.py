import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def Cube():
    glBegin(GL_QUADS)
    glVertex3f(-1.6, -1.6, 1.6)
    glVertex3f(1.6, -1.6, 1.6)
    glVertex3f(1.6, 1.6, 1.6)
    glVertex3f(-1.6, 1.6, 1.6)
    glEnd()

def init():
    glClearColor(1.0, 1.0, 0.0, 1.0)  # Set background color to yellow
    glColor3f(0.5, 0.5, 0.5)  # Set object color to gray
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Hello World..!!')
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
