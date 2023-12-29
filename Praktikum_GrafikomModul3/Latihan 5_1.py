import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math


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
        glColor3f (1, 1, 0) 
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
        
def main():
    pygame.init()
    display = (400,400)
    pygame.display.set_caption('Nurul Izza Farhana 0102523729')
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        plotfunc()
        pygame.display.flip()
        pygame.time.wait(10)

main()