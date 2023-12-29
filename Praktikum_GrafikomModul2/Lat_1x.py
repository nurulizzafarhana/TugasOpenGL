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
    for x in np.arange(-5.0, 5.0, 0.01):
        y = x*x
        glColor3f(0.0, 0.0, 0.0)
        glBegin(GL_POINTS)
        glVertex2f(x,y)
        glEnd()
        for a in np.arange(-5.0, 5.0, 0.01):
            if a < x*x:
                glColor3f(0.50,0.50,0.50)
                glBegin(GL_POINTS)
                glVertex2f(x,a)
                glEnd()
                glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)
    glEnd()
    glFlush()

def plotfunc2():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(3.0)
    glBegin(GL_LINES)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)
    glEnd()
    for x in np.arange(-5.0, 5.0, 0.01):
        y = x*x
        glBegin(GL_POINTS)
        glVertex2f(x,y)
        # pygame.time.wait(50)
        glEnd()
        glFlush()
def init():
    glClearColor (1.0, 0.0, 0.0, 1.0); ## background colour
def main():
    pygame.init()
    display = (400,400)
    pygame.display.set_caption('Function Plot')
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    glClearColor(0, 1.0, 0.0, 1.0)
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