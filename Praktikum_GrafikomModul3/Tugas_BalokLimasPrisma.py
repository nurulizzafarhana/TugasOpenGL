from screeninfo import get_monitors
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_cube(x, y, z, size):
    glPushMatrix()
    glTranslatef(x, y, z)
    glutSolidCube(size)
    glPopMatrix()

def draw_sphere(x, y, z, radius, slices=30, stacks=30):
    glPushMatrix()
    glTranslatef(x, y, z)
    glutSolidSphere(radius, slices, stacks)
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(5, 5, 5, 0, 0, 0, 0, 1, 0)

    glColor3f(1.0, 0.0, 0.0)  # warna merah
    draw_cube(-1, 0, 0, 1)

    glColor3f(0.0, 0.0, 1.0)  # warna biru
    draw_cube(1, 0, 0, 1)

    glColor3f(0.0, 1.0, 0.0)  # warna hijau
    draw_sphere(0,0,0, 0.5)

    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

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
    scale = 0.4
    size = get_window_size(scale)
    
    glutInitWindowSize(size,size)
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutCreateWindow(b"Hana")
    glEnable(GL_DEPTH_TEST)
    
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

main()
