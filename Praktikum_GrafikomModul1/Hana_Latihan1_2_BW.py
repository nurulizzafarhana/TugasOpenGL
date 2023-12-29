import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def Cube():
    glBegin(GL_QUADS)
    glVertex3f(-0.8, -0.8, 0.8)
    glVertex3f(0.8, -0.8, 0.8)
    glVertex3f(0.8, 0.8, 0.8)
    glVertex3f(-0.8, 0.8, 0.8)
    glEnd()

def init():
    glClearColor(0.0, 0.0, 1.0, 1.0); #Set background color to blue
    glColor3f(1.0, 1.0, 1.0);          #set object color to white
    glMatrixMode (GL_PROJECTION);        
    glLoadIdentity();                    #load identity
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0);   #projection


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Hello World..!!')
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
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