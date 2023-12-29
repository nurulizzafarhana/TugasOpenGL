import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def Octagon():
    glBegin(GL_POLYGON)
    glColor3f(1.0, 0.0, 0.0)  # Merah
    glVertex2f(0.0, 1.0)
    glColor3f(1.0, 0.5, 0.0)  # Oranye
    glVertex2f(0.7, 0.7)
    glColor3f(1.0, 1.0, 0.0)  # Kuning
    glVertex2f(1.0, 0.0)
    glColor3f(0.5, 1.0, 0.0)  # Hijau
    glVertex2f(0.7, -0.7)
    glColor3f(0.0, 1.0, 1.0)  # Cyan
    glVertex2f(0.0, -1.0)
    glColor3f(0.0, 0.0, 1.0)  # Biru
    glVertex2f(-0.7, -0.7)
    glColor3f(0.5, 0.0, 1.0)  # Ungu
    glVertex2f(-1.0, 0.0)
    glColor3f(1.0, 0.0, 1.0)  # Magenta
    glVertex2f(-0.7, 0.7)
    glEnd()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background color to white
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.5, 1.5, -1.5, 1.5)  # Projection

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Octagon with Colors')
    gluOrtho2D(-1.5, 1.5, -1.5, 1.5)
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT)
        Octagon()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
