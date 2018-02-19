import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
from OpenGL.GLUT import *

def axis():
	glColor3d(0,0,0)
	glBegin(GL_LINES)
	glVertex2d(0,-1)
	glVertex2d(0,1)
	glVertex2d(-1,0)
	glVertex2d(1,0)
	glEnd()
	
def cords():
	glColor3d(1,0,0)
	glBegin(GL_LINES)
	for i in np.arange(-1,1.1,.1):
		glVertex2d(1,i)
		glVertex2d(-1,i)
	for j in np.arange(-1,1.1,.1):
		glVertex2d(j,1)
		glVertex2d(j,-1)
	glEnd()
	
def circle(r,x0,y0,s,R=1,G=1,B=1,t=1):
    if s == "L":
        glBegin(GL_LINE_LOOP)
        for i in np.arange(0, 2 * pi * t, 0.001):
            x = x0+r * cos(i)
            y = y0+r * sin(i)
            glVertex2d(x, y)
        glEnd()
    elif s == "P":
        glColor3d(R,G,B)
        glBegin(GL_POLYGON)
        for i in np.arange(0, 2 * pi * t, 0.01):
            x = x0 + r * cos(i)
            y = y0 + r * sin(i)
            glVertex2d(x, y)
        glEnd()
        
def rect(x,y,length,weigth,R=1,G=1,B=1):
    glColor3d(R,G,B)
    glBegin(GL_POLYGON)
    glVertex2f(x,y)
    glVertex2f(x+weigth,y)
    glVertex2f(x+weigth,y+length)
    glVertex2f(x,y+length)
    glEnd()
    
def G_hand_Right():
    glColor3d(0.17, 0.17, 0.17)
    glBegin(GL_POLYGON)
    glVertex2f(-.5,-.15)
    glVertex2f(-.6,0)
    glVertex2f(-.7,-.05)
    glVertex2f(-0.7,-.1)
    glVertex2f(-.5,-.15)
    glVertex2f(-.6,-.3)
    glVertex2f(-0.7,-.25)
    glVertex2f(-0.7,-.2)
    glEnd()
 
def G_hand_Left():
    glColor3d(0.17, 0.17, 0.17)
    glBegin(GL_POLYGON)
    glVertex2f(.5,-.15)
    glVertex2f(.6,0)
    glVertex2f(.7,-.05)
    glVertex2f(0.7,-.1)
    glVertex2f(.5,-.15)
    glVertex2f(.6,-.3)
    glVertex2f(0.7,-.25)
    glVertex2f(0.7,-.2)
    glEnd()
    
def body():
    R,G,B=0.17, 0.17, 0.17

    rect(-.3,0,-.4,.6,R,G,B)
    circle(.1,-.2,-.4,"P",R,G,B)
    circle(.1,.2,-.4,"P",R,G,B)
    rect(-.2,-.5,.1,.4,R,G,B)


    rect(-.29,-0.01,-.38,.58)
    circle(.09,-.2,-.4,"P")
    circle(.09,.2,-.4,"P")
    rect(-.19,-.49,.1,.39)

    circle(.04,0,-.2,"P",R,G,B)
    circle(.03,0,-.2,"P",0.13, 0.45, 0.96)

    circle(.04,0.1,-.2,"P",R,G,B)
    circle(.03,0.1,-.2,"P",0.13, 0.45, 0.96)

    circle(.04,-0.1,-.2,"P",R,G,B)
    circle(.03,-0.1,-.2,"P",0.13, 0.45, 0.96)

 
def hands():
 	R,G,B=0.17, 0.17, 0.17

 	G_hand_Right()
 	G_hand_Left()

 	rect(-.3,-.11,-.075,-.2,R,G,B)
 	rect(-.3,-.12,-.055,-.2,0.85, 0.88, 0.93)

 	circle(.06,-.5,-.15,"P",R,G,B)
 	circle(.05,-.5,-.15,"P")
 	circle(.03,-.5,-.15,"P",R,G,B)


 	rect(.3,-.11,-.075,.2,R,G,B)
 	rect(.3,-.12,-.055,.2,0.85, 0.88, 0.93)

 	circle(.06,.5,-.15,"P",R,G,B)
 	circle(.05,.5,-.15,"P")
 	circle(.03,.5,-.15,"P",R,G,B)

 	circle(.06,-.3,-.15,"P",R,G,B)
 	circle(.05,-.3,-.15,"P")

 	circle(.06,.3,-.15,"P",R,G,B)
 	circle(.05,.3,-.15,"P")




def head():
	R,G,B=0.17, 0.17, 0.17
#R_Ear	
	rect(.2,.14,.13,.1,R,G,B)
	rect(.21,.15,.11,.08)
#L_Ear 
	rect(-.2,.14,.13,-.1,R,G,B)
	rect(-.19,.15,.11,-.1)
# top_of_head
	rect(-.02,.45,.2,.04,R,G,B)
	circle(.05,0,.65,"P",R,G,B)
	circle(.04,0,.65,"P",0.97, 0.90, 0.27)
	rect(-.04,.54,.02,.08,R,G,B)
	rect(-.04,.57,.02,.08,R,G,B)
#neck
	rect(-.1,0.02,.02,.2,R,G,B)
	circle(.01,-.1,0.03,"P",R,G,B)
	circle(.01,.1,0.03,"P",R,G,B)
#head
	rect(-.23,.05,.2,.46,R,G,B)
	circle(.23,0,.25,"P",R,G,B,.5)
	rect(-.22,.06,.2,.44)
	circle(.22,0,.25,"P",1,1,1,.5)
#eye
	circle(.09,0,.2,"P",0.85, 0.88, 0.93)
	circle(.07,0,.2,"P")
	circle(.04,0,.2,"P",R,G,B)


def leg():
	R,G,B=0.17, 0.17, 0.17

	rect(-.3,-.692,-.02,.6,0.81, 0.84, 0.91)
	circle(.01,-.3,-.702,"P",0.81, 0.84, 0.91)
	circle(.01,.3,-.702,"P",0.81, 0.84, 0.91)

	circle(.08,-.12,-.5,"P",R,G,B)
	circle(.065,-.12,-.5,"P")

	circle(.08,.12,-.5,"P",R,G,B)
	circle(.065,.12,-.5,"P")

	rect(-.12,-.5,-.08,.24,R,G,B)
	circle(.12,0,-.58,"P",R,G,B)
	rect(-.11,-.49,-.08,.22,0.56, 0.60, 0.69)
	circle(.11,0,-.58,"P",0.56, 0.60, 0.69)

	rect(-.07,-.55,-.02,.14,R,G,B)
	circle(.01,-.07,-.56,"P",R,G,B)
	circle(.01,.07,-.56,"P",R,G,B)

	rect(-.07,-.6,-.02,.14,R,G,B)
	circle(.01,-.07,-.61,"P",R,G,B)
	circle(.01,.07,-.61,"P",R,G,B)




def display():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    
    #cords()
    #axis()
    hands()
    head()
    leg()    
    body()
    


    glFlush()   
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Robot V-1.3")
glutDisplayFunc(display)
glutMainLoop()
