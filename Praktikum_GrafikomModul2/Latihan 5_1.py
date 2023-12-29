import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(1.0)
    glBegin(GL_LINES)
    glVertex2f(-2.0, 0.0)
    glVertex2f(2.0, 0.0)
    glVertex2f(0.0, 2.0)
    glVertex2f(0.0, -2.0)
    glEnd()
    for t in np.arange(-5.0,6.28, 0.001):
        x = math.sin(t)
        y = math.cos(t)
        glBegin(GL_POINTS)
        glVertex2f(x,y)
        glEnd()
        glFlush()
        
def main():
    pygame.init()
    display = (400,400)
    pygame.display.set_caption('Function Plot')
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