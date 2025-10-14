from OpenGL.GL import *
from OpenGL.GLUT import *

def init():
    glClearColor(0.0, 50.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.5, 1.0, 0.0, 1.0, -1.5, 1.5)
    glMatrixMode(GL_MODELVIEW)
    
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glVertex3f(0.55, 0.25, 5.0)
    glVertex3f(0.75, 0.55, 0.0)
    glVertex3f(0.75, 0.75, 0.0)
    glVertex3f(0.55, 0.75, 0.0)
    glEnd()
    glutSwapBuffers()
    
def reshape(width, height):
    glViewport(0, 0, width, height)
    
def reshape2(width, height):
    size = width if width < height else height
    glViewport(0, 0, size, size)
    
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(250, 250)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"OpenGL Window")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
    reshape(250, 250)
    
    
if __name__ == "__main__":
    main()