import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math
import sys


def plotfunc(): 
    squares = [
        [[-1,-1,1], [1,-1,1], [1,1,1], [-1,1,1]],
        [[1,-1,-1], [1,1,-1], [-1,1,-1],[-1,-1,-1]],
        [[-1,1,-1], [-1,1,1], [1,1,1],[1,1,-1]],
        
        [[-1,-1,-1], [1,-1,-1], [1,-1,1], [-1,-1,1]],
        [[1,-1,-1], [1,1,-1], [1,1,1],[1,-1,1]],
        [[-1,-1,-1], [-1,-1,1], [-1,1,1],[-1,1,-1]],
    ]
    
    glClear (GL_COLOR_BUFFER_BIT)
    glColor3f (0.0, 0.0, 0.0)
    glPointSize (1.0)
    for square in squares: 
        glColor3f (1, 0, 0) 
        glBegin(GL_POLYGON) 
        for point in square:
            glVertex3f (point[0], point[1], point[2])
        glEnd()
        glColor3f (0, 0, 0)
        glBegin (GL_LINE_LOOP) 
        for point in square:
            glVertex3f (point [0], point [1], point [2])
        glEnd()
    glFlush ()
   

def displaye():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glutSolidTeapot(1.0)
    # glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, width / height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
         
def main():
    glutInit(sys.argv)
    # glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    pygame.init()
    display = (400,400)
    pygame.display.set_caption('Hana')
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        displaye()
        # pygame.display.flip()
        # pygame.time.wait(10)



main()