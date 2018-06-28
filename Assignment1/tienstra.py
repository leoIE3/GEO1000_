# GEO1000 - Assignment 1
# Authors: Leonardo Melo
# Studentnumbers: 4690923

import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
	
def angle(a, b, c, var):
    
	if var=='A':
	    return math.acos((b**2+c**2-a**2)/(2.0*b*c))
	elif var=='B':
	    return math.acos((a**2-b**2+c**2)/(2.0*c*a))
	elif var=='C':
	    return math.acos((a**2+b**2-c**2)/(2.0*a*b))
	else:
	    print "please insert the corresponding angle A, B or C in the function arguments"
	return
	
def cot(x):
    return math.cos(x)/math.sin(x)

def tienstra(ax, ay, bx, by, cx, cy, alpha, gamma):
    #compute missing angle
	alpha_rad=math.radians(alpha)
	gamma_rad=math.radians(gamma)
	beta_rad=2.0*math.pi-alpha_rad-gamma_rad
	#------------------------------------------------------
	#compute cartesian distances
	AB=distance(ax,ay,bx,by)
	BC=distance(bx,by,cx,cy)
	CA=distance(cx,cy,ax,ay)
	#------------------------------------------------------
	#compute angles A, B and C
	#AB is the distance between points A and B which is c
	#BC is the distance between points B and C which is a
	#CA is the distance between points C and A whihc is b
	c=AB
	a=BC
	b=CA
	ang_A=angle(a,b,c,'A')
	ang_B=angle(a,b,c,'B')
	ang_C=angle(a,b,c,'C')
	#------------------------------------------------------
	#Calculate coeficient Ks
	K_1=1.0/(cot(ang_A)-cot(alpha_rad))
	K_2=1.0/(cot(ang_B)-cot(beta_rad))
	K_3=1.0/(cot(ang_C)-cot(gamma_rad))
	#Calculate P(x,y)
	P_x=(((K_1*ax)+(K_2*bx)+(K_3*cx))/(K_1+K_2+K_3))
	P_y=(((K_1*ay)+(K_2*by)+(K_3*cy))/(K_1+K_2+K_3))
	print 'The coordinate px is',P_x
	print 'The coordinate py is',P_y
	
tienstra(
    1000.0, 5300.0,
    2200.0, 6300.0,
    3100.0, 5000.0,
    115.052, 109.3045)

