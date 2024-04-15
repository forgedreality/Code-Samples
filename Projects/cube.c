// to compile:
// gcc -o ../build/cube cube.c -lopengl32 -lglu32 -lfreeglut

#include <gl/glut.h>
#include <stdio.h>
#include <math.h>

int fullscreen = 0;
int mouseDown = 0;

int m_pos_x = 0;
int m_pos_y = 0;

float xrot = 0.0f;
float yrot = 0.0f;

float xdiff = 0.0f;
float ydiff = 0.0f;

float x_dist = 0.0f;
float y_dist = 0.0f;

float RGB[6][3] = {
    {0.0f, 0.0f, 0.0f},
    {0.0f, 0.0f, 0.0f},
    {0.0f, 0.0f, 0.0f},
    {0.0f, 0.0f, 0.0f},
    {0.0f, 0.0f, 0.0f},
    {0.0f, 0.0f, 0.0f}
};

int centered_mouse_x = 0;
int centered_mouse_y = 0;

int tint[3] = {0, 0, 0};

void setRGB(int side)
{
    if (RGB[side][0] == 0 && RGB[side][1] == 0 && RGB[side][2] == 0)
    {
        RGB[side][0] = (rand() % 10000) / 10000.0;
        RGB[side][1] = (rand() % 10000) / 10000.0;
        RGB[side][2] = (rand() % 10000) / 10000.0;
    }

    tint[0] = RGB[side][0];
    tint[1] = RGB[side][1];
    tint[2] = RGB[side][2];
}

void drawBox()
{
    glBegin(GL_QUADS);

    // Mouse coords with 0,0 being center of window
    centered_mouse_x = m_pos_x - ((glutGet(GLUT_WINDOW_WIDTH) / 2) - 100);
    centered_mouse_y = m_pos_y - ((glutGet(GLUT_WINDOW_HEIGHT) / 2) - 100);

    int side_counter = 0;

    setRGB(side_counter);

    // x - (screen_width / 2)
    tint[0] = (256 * RGB[side_counter][0]) + (centered_mouse_x / 4);
    tint[0] = (tint[0] < 0) ? 0 : (tint[0] < 255) ? tint[0] : 255;

    tint[1] = (256 * RGB[side_counter][1]) + (centered_mouse_x / 4);
    tint[1] = (tint[1] < 0) ? 0 : (tint[1] < 255) ? tint[1] : 255;

    tint[2] = (256 * RGB[side_counter][2]) + (centered_mouse_x / 4);
    tint[2] = (tint[2] < 0) ? 0 : (tint[2] < 255) ? tint[2] : 255;

    glColor3f(tint[0] / 256.0, tint[1] / 256.0, tint[2] / 256.0);

    // FRONT
    glVertex3f(-0.5f, -0.5f, 0.5f);
    glVertex3f( 0.5f, -0.5f, 0.5f);
    glVertex3f( 0.5f, 0.5f, 0.5f);
    glVertex3f(-0.5f, 0.5f, 0.5f);

    side_counter++;

    setRGB(side_counter);

    // x - (screen_width / 2)
    tint[0] = (256 * RGB[side_counter][0]) + (centered_mouse_x / 4);
    tint[0] = (tint[0] < 0) ? 0 : (tint[0] < 255) ? tint[0] : 255;

    tint[1] = (256 * RGB[side_counter][1]) + (centered_mouse_x / 4);
    tint[1] = (tint[1] < 0) ? 0 : (tint[1] < 255) ? tint[1] : 255;

    tint[2] = (256 * RGB[side_counter][2]) + (centered_mouse_x / 4);
    tint[2] = (tint[2] < 0) ? 0 : (tint[2] < 255) ? tint[2] : 255;

    glColor3f(tint[0] / 256.0, tint[1] / 256.0, tint[2] / 256.0);

    // BACK
    glVertex3f(-0.5f, -0.5f, -0.5f);
    glVertex3f(-0.5f, 0.5f, -0.5f);
    glVertex3f( 0.5f, 0.5f, -0.5f);
    glVertex3f( 0.5f, -0.5f, -0.5f);

    side_counter++;

    setRGB(side_counter);

    // x - (screen_width / 2)
    tint[0] = (256 * RGB[side_counter][0]) + (centered_mouse_x / 4);
    tint[0] = (tint[0] < 0) ? 0 : (tint[0] < 255) ? tint[0] : 255;

    tint[1] = (256 * RGB[side_counter][1]) + (centered_mouse_x / 4);
    tint[1] = (tint[1] < 0) ? 0 : (tint[1] < 255) ? tint[1] : 255;

    tint[2] = (256 * RGB[side_counter][2]) + (centered_mouse_x / 4);
    tint[2] = (tint[2] < 0) ? 0 : (tint[2] < 255) ? tint[2] : 255;

    glColor3f(tint[0] / 256.0, tint[1] / 256.0, tint[2] / 256.0);

    // LEFT
    glVertex3f(-0.5f, -0.5f, 0.5f);
    glVertex3f(-0.5f, 0.5f, 0.5f);
    glVertex3f(-0.5f, 0.5f, -0.5f);
    glVertex3f(-0.5f, -0.5f, -0.5f);

    side_counter++;

    setRGB(side_counter);

    // x - (screen_width / 2)
    tint[0] = (256 * RGB[side_counter][0]) + (centered_mouse_x / 4);
    tint[0] = (tint[0] < 0) ? 0 : (tint[0] < 255) ? tint[0] : 255;

    tint[1] = (256 * RGB[side_counter][1]) + (centered_mouse_x / 4);
    tint[1] = (tint[1] < 0) ? 0 : (tint[1] < 255) ? tint[1] : 255;

    tint[2] = (256 * RGB[side_counter][2]) + (centered_mouse_x / 4);
    tint[2] = (tint[2] < 0) ? 0 : (tint[2] < 255) ? tint[2] : 255;

    glColor3f(tint[0] / 256.0, tint[1] / 256.0, tint[2] / 256.0);

    // RIGHT
    glVertex3f( 0.5f, -0.5f, -0.5f);
    glVertex3f( 0.5f, 0.5f, -0.5f);
    glVertex3f( 0.5f, 0.5f, 0.5f);
    glVertex3f( 0.5f, -0.5f, 0.5f);

    side_counter++;

    setRGB(side_counter);

    // x - (screen_width / 2)
    tint[0] = (256 * RGB[side_counter][0]) + (centered_mouse_x / 4);
    tint[0] = (tint[0] < 0) ? 0 : (tint[0] < 255) ? tint[0] : 255;

    tint[1] = (256 * RGB[side_counter][1]) + (centered_mouse_x / 4);
    tint[1] = (tint[1] < 0) ? 0 : (tint[1] < 255) ? tint[1] : 255;

    tint[2] = (256 * RGB[side_counter][2]) + (centered_mouse_x / 4);
    tint[2] = (tint[2] < 0) ? 0 : (tint[2] < 255) ? tint[2] : 255;

    glColor3f(tint[0] / 256.0, tint[1] / 256.0, tint[2] / 256.0);

    // TOP
    glVertex3f(-0.5f, 0.5f, 0.5f);
    glVertex3f( 0.5f, 0.5f, 0.5f);
    glVertex3f( 0.5f, 0.5f, -0.5f);
    glVertex3f(-0.5f, 0.5f, -0.5f);

    side_counter++;

    setRGB(side_counter);

    // x - (screen_width / 2)
    tint[0] = (256 * RGB[side_counter][0]) + (centered_mouse_x / 4);
    tint[0] = (tint[0] < 0) ? 0 : (tint[0] < 255) ? tint[0] : 255;

    tint[1] = (256 * RGB[side_counter][1]) + (centered_mouse_x / 4);
    tint[1] = (tint[1] < 0) ? 0 : (tint[1] < 255) ? tint[1] : 255;

    tint[2] = (256 * RGB[side_counter][2]) + (centered_mouse_x / 4);
    tint[2] = (tint[2] < 0) ? 0 : (tint[2] < 255) ? tint[2] : 255;

    glColor3f(tint[0] / 256.0, tint[1] / 256.0, tint[2] / 256.0);

    // BOTTOM
    glVertex3f(-0.5f, -0.5f, 0.5f);
    glVertex3f(-0.5f, -0.5f, -0.5f);
    glVertex3f( 0.5f, -0.5f, -0.5f);
    glVertex3f( 0.5f, -0.5f, 0.5f);

    glEnd();
}

int init()
{
    glClearColor(0.69f, 0.69f, 0.69f, 0.0f);

    glEnable(GL_DEPTH_TEST);
    glDepthFunc(GL_LEQUAL);
    glClearDepth(1.0f);

    return 1;
}

void display()
{
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();

    // printf("x:%f - y:%f, x_dist: %f - y_dist: %f, mouse_x: %i, mouse_y: %i\n", xrot, yrot, x_dist, y_dist, centered_mouse_x, centered_mouse_y);

    gluLookAt(
        0.0f, 0.0f, 3.0f,
        0.0f, 0.0f, 0.0f,
        0.0f, 1.0f, 0.0f
    );

    glRotatef(xrot, 1.0f, 0.0f, 0.0f);
    glRotatef(yrot, 0.0f, 1.0f, 0.0f);

    drawBox();

    glFlush();
    glutSwapBuffers();
}

void resize(int w, int h)
{
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();

    glViewport(0, 0, w, h);

    gluPerspective(45.0f, 1.0f * w / h, 1.0f, 100.0f);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

void idle()
{
    if (!mouseDown)
    {
        // printf("TESTING DIST: %f %f :: Mouse_x: %i, Mouse_y: %i\n", x_dist, y_dist, m_pos_x, m_pos_y);
        if (fabs(x_dist) > 0.0f)
        {
            if (x_dist > 0.0f)
            {
                x_dist -= x_dist * 0.01f;
                yrot += x_dist;
            }
            else
            {
                x_dist -= x_dist * 0.01f;
                yrot += x_dist;
            }
        }

        if (fabs(y_dist) > 0.0f)
        {
            if (y_dist > 0.0f)
            {
                y_dist -= y_dist * 0.01f;
                xrot += y_dist;
            }
            else
            {
                y_dist -= y_dist * 0.01f;
                xrot += y_dist;
            }
        }
    }

    glutPostRedisplay();
}

void keyboard(unsigned char key, int x, int y)
{
    switch(key)
    {
        case 27 : 
        exit(1); break;
    }
}

void specialKeyboard(int key, int x, int y)
{
    if (key == GLUT_KEY_F1)
    {
        fullscreen = (fullscreen) ? 0 : 1;

        if (fullscreen)
        {
            glutFullScreen();
        }

        else
        {
            glutReshapeWindow(600, 600);
            glutPositionWindow(50, 50);
        }
    }
}

void mouse(int button, int state, int x, int y)
{
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
    {
        mouseDown = 1;

        xdiff = x - yrot;
        ydiff = -y + xrot;

        x_dist = x;
        y_dist = y;
    }
    else
    {
        x_dist = (x - x_dist) / 100;
        y_dist = (y - y_dist) / 100;
        mouseDown = 0;
    }
}

void mouseMotion(int x, int y)
{
    if (mouseDown)
    {
        yrot = x - xdiff;
        xrot = y + ydiff;

        glutPostRedisplay();
    }
}

// Used to update mouse coords for use with other functions
void setMousePos(int x, int y) {
    m_pos_x = x;
    m_pos_y = y;
}

int main(int argc, char *argv[])
{
    glutInit(&argc, argv);

    glutInitWindowPosition(50, 50);
    glutInitWindowSize(600, 600);

    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE);

    glutCreateWindow("Rotating Cube");

    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);
    glutSpecialFunc(specialKeyboard);
    glutMouseFunc(mouse);
    glutMotionFunc(mouseMotion);
    glutReshapeFunc(resize);
    glutIdleFunc(idle);

    glutPassiveMotionFunc(setMousePos);

    if (!init())
    {
        return 1;
    }

    glutMainLoop();

    return 0;
}
