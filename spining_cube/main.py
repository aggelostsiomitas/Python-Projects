import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Vertices of a cube
vertices = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1],
]

# Edges of the cube (pairs of vertex indices)
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Back face
    (4, 5), (5, 6), (6, 7), (7, 4),  # Front face
    (0, 4), (1, 5), (2, 6), (3, 7),  # Connecting edges
]

# Colors for each vertex
colors = [
    (1, 0, 0),          #red
    (0, 1, 0),          #green
    (0, 0, 1),          #blue 
    (1, 1, 0),          #yellow
    (1, 0, 1),          #magenta
    (0, 1, 1),          #cyan
    (1, 1, 1),          #white
    (0.5, 0.5, 0.5),    #gray
]

#draw cube 
def draw_cube():
    glBegin(GL_QUADS)   #draw rectangles
    for face in [
            [0, 1, 2, 3],
            [4, 5, 6, 7], 
            [0, 1, 5, 4], 
            [2, 3, 7, 6], 
            [0, 3, 7, 4], 
            [1, 2, 6, 5]
        ]:
        
        #set the color for the vertex and send the verted potition to OpenGL
        for vertex in face:
            glColor3fv(colors[vertex])
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES) #draw straight lines betwee vertex pairs
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    # Initialize Pygame
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Set perspective
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5) #move the cube a little bit of the camera

    # Rotation angles
    x_rotation = 0
    y_rotation = 0

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        # Rotate cube
        x_rotation += 1
        y_rotation += 1


        #clear color buffer and depth buffer
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #apply transformation
        glPushMatrix()

        #save current transformation state
        glRotatef(x_rotation, 1, 0, 0)  # Rotate around X-axis
        glRotatef(y_rotation, 0, 1, 0)  # Rotate around Y-axis
        draw_cube() #draw the new cube
        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
