import sys
import pygame
from screeninfo import get_monitors
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *

def solidTeapot():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glutSolidTeapot(1.0)
    glutSwapBuffers()
    
def wireTeapot():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glutWireTeapot(1.0)
    glutSwapBuffers()
    
def solidCube():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glutSolidCube(1.0)
    glutSwapBuffers()
    
def wireCube():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glutWireCube(1.0)
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, width / height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    
def get_display_size():
    primary_monitor = get_monitors()[0]
    width = primary_monitor.width
    height = primary_monitor.height
    return [width, height]

def get_window_size(scale=1):
    display_size = get_display_size()
    size = round(display_size[0]*scale)
    if round(display_size[1]*scale) > size :
        size = round(display_size[1]*scale)
    return size

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    
    scale = 0.4
    size = get_window_size(scale)
    
    glutInitWindowSize(size,size)
    glutCreateWindow(b"Hana")
    glEnable(GL_DEPTH_TEST)
    # glutDisplayFunc(solidCube)
    # glutDisplayFunc(wireCube)
    glutDisplayFunc(wireTeapot)
    # glutDisplayFunc(solidTeapot)
    glutReshapeFunc(reshape)
    glutMainLoop()

main()
