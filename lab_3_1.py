from graphics import *
from math import *

win = GraphWin('MyWin', 500, 800)



def Sky():
	sky = Rectangle(Point(0, 0), Point(500, 450))	
	sky.setFill("#00ffff")
	sky.setOutline("#00ffff")
	sky.draw(win)


def Ice():
	ice = Rectangle(Point(0, 450), Point(500, 800))	
	ice.setFill("#e6e6e6")
	ice.setOutline("#e6e6e6")
	ice.draw(win)


def Horizont():
	horizont = Line(Point(0, 450), Point(500, 450))
	horizont.setWidth(1)
	horizont.draw(win)


def Sun(x, y):
	sun = Circle(Point(x, y), 170)		
	sun.setFill("#00ffff")
	sun.setOutline("#cdf7dd")
	sun.setWidth(30)
	
	sun_line1 = Line(Point(x - 170, y), Point(x + 170, y))
	sun_line1.setWidth(30)
	sun_line1.setOutline("#cdf7dd")

	sun_line2 = Line(Point(x, y - 170), Point(x, y + 170))
	sun_line2.setWidth(30)
	sun_line2.setOutline("#cdf7dd")

	sun_shine0 = Rectangle(Point(x - 15, y - 15), Point(x + 15, y + 15))	
	sun_shine0.setFill("#fcf6d6")
	sun_shine0.setWidth(0)

	sun_shine1 = Rectangle(Point(x - 185, y - 15), Point(x - 155, y + 15))	
	sun_shine1.setFill("#fcf6d6")
	sun_shine1.setWidth(0)

	sun_shine2 = Rectangle(Point(x + 155, y - 15), Point(x + 185, y + 15))	
	sun_shine2.setFill("#fcf6d6")
	sun_shine2.setWidth(0)

	sun_shine3 = Rectangle(Point(x - 15, y + 155), Point(x + 15, y + 185))	
	sun_shine3.setFill("#fcf6d6")
	sun_shine3.setWidth(0)

	sun.draw(win)
	sun_line1.draw(win)
	sun_line2.draw(win)
	sun_shine0.draw(win)
	sun_shine1.draw(win)
	sun_shine2.draw(win)
	sun_shine3.draw(win)


def Right_Bear(x, y, k):
	head = Oval(Point(x, y), Point(x + 55 * k, y + 30 * k))
	head.setFill("#e6e6e6")
	body = Oval(Point(x + 15 * k, y + 20 * k), Point(x + 95 * k, y + 150 * k))
	body.setFill("#e6e6e6")
	leg = Oval(Point(x, y + 110 * k), Point(x + 55 * k, y + 155 * k))
	leg.setFill("#e6e6e6")
	foot = Oval(Point(x - 25 * k, y + 140 * k), Point(x + 20 * k, y + 160 * k))
	foot.setFill("#e6e6e6")
	paw = Oval(Point(x - 5 * k, y + 50 * k), Point(x + 35 * k, y + 70 * k))
	paw.setFill("#e6e6e6")
	ear = Circle(Point(x + 50 * k, y + 8 * k), 6 * k)		
	ear.setFill("#e6e6e6")
	nose = Circle(Point(x + k, y + 13 * k), 2 * k)		
	nose.setFill("#000000")
	eye = Circle(Point(x + 32 * k, y + 10 * k), 2 * k)		
	eye.setFill("#000000")
	mouth = Line(Point(x + 3 * k, y + 22 * k), Point(x + 30 * k, y + 22 * k))
	mouth.setWidth(1)
	rode = Line(Point(x + 35 * k, y + 100 * k), Point(x - 90 * k, y - 40 * k))
	rode.setWidth(2)
	fishing_line = Line(Point(x - 90 * k, y + 140 * k), Point(x - 90 * k, y - 40 * k))
	fishing_line.setWidth(1)
	ice_hole1 = Oval(Point(x - 150 * k, y + 120 * k), Point(x - 60 * k, y + 160 * k))
	ice_hole1.setFill("#4d4d4d")
	ice_hole2 = Oval(Point(x - 140 * k, y + 130 * k), Point(x - 70 * k, y + 160 * k))
	ice_hole2.setFill("#165044")

	ice_hole1.draw(win)
	ice_hole2.draw(win)
	fishing_line.draw(win)
	rode.draw(win)
	head.draw(win)
	body.draw(win)
	leg.draw(win)
	foot.draw(win)
	paw.draw(win)
	ear.draw(win)
	nose.draw(win)
	eye.draw(win)
	mouth.draw(win)


def Left_Bear(x, y, k):
	head = Oval(Point(x, y), Point(x - 55 * k, y + 30 * k))
	head.setFill("#e6e6e6")
	body = Oval(Point(x - 15 * k, y + 20 * k), Point(x - 95 * k, y + 150 * k))
	body.setFill("#e6e6e6")
	leg = Oval(Point(x, y + 110 * k), Point(x - 55 * k, y + 155 * k))
	leg.setFill("#e6e6e6")
	foot = Oval(Point(x + 25 * k, y + 140 * k), Point(x - 20 * k, y + 160 * k))
	foot.setFill("#e6e6e6")
	paw = Oval(Point(x + 5 * k, y + 50 * k), Point(x - 35 * k, y + 70 * k))
	paw.setFill("#e6e6e6")
	ear = Circle(Point(x - 50 * k, y + 8 * k), 6 * k)		
	ear.setFill("#e6e6e6")
	nose = Circle(Point(x - k, y + 13 * k), 2 * k)		
	nose.setFill("#000000")
	eye = Circle(Point(x - 32 * k, y + 10 * k), 2 * k)		
	eye.setFill("#000000")
	mouth = Line(Point(x - 3 * k, y + 22 * k), Point(x - 30 * k, y + 22 * k))
	mouth.setWidth(1)
	rode = Line(Point(x - 35 * k, y + 100 * k), Point(x + 90 * k, y - 40 * k))
	rode.setWidth(2)
	fishing_line = Line(Point(x + 90 * k, y + 140 * k), Point(x + 90 * k, y - 40 * k))
	fishing_line.setWidth(1)
	ice_hole1 = Oval(Point(x + 150 * k, y + 120 * k), Point(x + 60 * k, y + 160 * k))
	ice_hole1.setFill("#4d4d4d")
	ice_hole2 = Oval(Point(x + 140 * k, y + 130 * k), Point(x + 70 * k, y + 160 * k))
	ice_hole2.setFill("#165044")

	ice_hole1.draw(win)
	ice_hole2.draw(win)
	fishing_line.draw(win)
	rode.draw(win)
	head.draw(win)
	body.draw(win)
	leg.draw(win)
	foot.draw(win)
	paw.draw(win)
	ear.draw(win)
	nose.draw(win)
	eye.draw(win)
	mouth.draw(win)


def Left_Crucian(x, y, k, alpha):
	fish = Polygon(Point(sin(alpha) * (- 45 * k) + x, cos(alpha) * (- 45 * k) + y), 
		Point(cos(alpha) * (- 100 * k) + x, - sin(alpha) * (- 100 * k) + y), 
		Point(sin(alpha) * (45 * k) + x, cos(alpha) * (45 * k) + y), 
		Point(cos(alpha) * (100 * k) + x, - sin(alpha) * (100 * k) + y), 
		Point(sin(alpha) * (- 45 * k) + x, cos(alpha) * (- 45 * k) + y))
	fish.setFill("#93aca7")
	tail = Polygon(Point(cos(alpha) * (- 100 * k) + x, - sin(alpha) * (- 100 * k) + y), 
		Point(cos(alpha) * (- 175 * k) + sin(alpha) * (- 30 * k) + x, cos(alpha) * (- 30 * k) - sin(alpha) * (- 175 * k) + y), 
		Point(cos(alpha) * (- 175 * k) + sin(alpha) * (30 * k) + x, cos(alpha) * (30 * k) - sin(alpha) * (- 175 * k) + y),
		Point(cos(alpha) * (- 100 * k) + x, - sin(alpha) * (- 100 * k) + y))
	tail.setFill("#93aca7")
	up_fin = Polygon(Point(cos(alpha) * (20 * k) + x, - sin(alpha) * (20 * k) + y), 
		Point(cos(alpha) * (60 * k) + sin(alpha) * (- 55 * k) + x, cos(alpha) * (- 55 * k) - sin(alpha) * (60 * k) + y), 
		Point(cos(alpha) * (- 70 * k) + sin(alpha) * (- 80 * k) + x, cos(alpha) * (- 80 * k) - sin(alpha) * (- 70 * k) + y),
		Point(cos(alpha) * (20 * k) + x, - sin(alpha) * (20 * k) + y))
	up_fin.setFill("#d35f5f")
	fin = Polygon(Point(x, y),
		Point(cos(alpha) * (80 * k) + sin(alpha) * (30 * k) + x, cos(alpha) * (30 * k) - sin(alpha) * (80 * k) + y),
		Point(cos(alpha) * (45 * k) + sin(alpha) * (50 * k) + x, cos(alpha) * (50 * k) - sin(alpha) * (45 * k) + y),
		Point(x, y))
	fin.setFill("#d35f5f")
	down_fin = Polygon(Point(cos(alpha) * (- 40 * k) + x, - sin(alpha) * (- 40 * k) + y),
		Point(cos(alpha) * (- 70 * k) + sin(alpha) * (40 * k) + x, cos(alpha) * (40 * k) - sin(alpha) * (- 70 * k) + y),
		Point(cos(alpha) * (- 30 * k) + sin(alpha) * (60 * k) + x, cos(alpha) * (60 * k) - sin(alpha) * (- 30 * k) + y),
		Point(cos(alpha) * (- 10 * k) + x, - sin(alpha) * (- 10 * k) + y),
		Point(cos(alpha) * (- 40 * k) + x, - sin(alpha) * (- 40 * k) + y))
	down_fin.setFill("#d35f5f")
	eye1 = Circle(Point(cos(alpha) * (65 * k) + x, - sin(alpha) * (65 * k) + y), 9 * k)		
	eye1.setFill("#2123f6")
	eye2 = Circle(Point(cos(alpha) * (65 * k) + x, - sin(alpha) * (65 * k) + y), 5 * k)		
	eye2.setFill("#000000")

	down_fin.draw(win)
	fin.draw(win)
	up_fin.draw(win)
	fish.draw(win)
	tail.draw(win)
	eye1.draw(win)
	eye2.draw(win)


def Right_Crucian(x, y, k, alpha):
	fish = Polygon(Point(sin(alpha) * (- 45 * k) + x, cos(alpha) * (- 45 * k) + y), 
		Point(cos(alpha) * (100 * k) + x, - sin(alpha) * (100 * k) + y), 
		Point(sin(alpha) * (45 * k) + x, cos(alpha) * (45 * k) + y), 
		Point(cos(alpha) * (- 100 * k) + x, - sin(alpha) * (- 100 * k) + y), 
		Point(sin(alpha) * (- 45 * k) + x, cos(alpha) * (- 45 * k) + y))
	fish.setFill("#93aca7")
	tail = Polygon(Point(cos(alpha) * (100 * k) + x, - sin(alpha) * (100 * k) + y), 
		Point(cos(alpha) * (175 * k) + sin(alpha) * (- 30 * k) + x, cos(alpha) * (- 30 * k) - sin(alpha) * (175 * k) + y), 
		Point(cos(alpha) * (175 * k) + sin(alpha) * (30 * k) + x, cos(alpha) * (30 * k) - sin(alpha) * (175 * k) + y),
		Point(cos(alpha) * (100 * k) + x, - sin(alpha) * (100 * k) + y))
	tail.setFill("#93aca7")
	up_fin = Polygon(Point(cos(alpha) * (- 20 * k) + x, - sin(alpha) * (- 20 * k) + y), 
		Point(cos(alpha) * (- 60 * k) + sin(alpha) * (- 55 * k) + x, cos(alpha) * (- 55 * k) - sin(alpha) * (- 60 * k) + y), 
		Point(cos(alpha) * (70 * k) + sin(alpha) * (- 80 * k) + x, cos(alpha) * (- 80 * k) - sin(alpha) * (70 * k) + y),
		Point(cos(alpha) * (- 20 * k) + x, - sin(alpha) * (- 20 * k) + y))
	up_fin.setFill("#d35f5f")
	fin = Polygon(Point(x, y),
		Point(cos(alpha) * (- 80 * k) + sin(alpha) * (30 * k) + x, cos(alpha) * (30 * k) - sin(alpha) * (- 80 * k) + y),
		Point(cos(alpha) * (- 45 * k) + sin(alpha) * (50 * k) + x, cos(alpha) * (50 * k) - sin(alpha) * (- 45 * k) + y),
		Point(x, y))
	fin.setFill("#d35f5f")
	down_fin = Polygon(Point(cos(alpha) * (40 * k) + x, - sin(alpha) * (40 * k) + y),
		Point(cos(alpha) * (70 * k) + sin(alpha) * (40 * k) + x, cos(alpha) * (40 * k) - sin(alpha) * (70 * k) + y),
		Point(cos(alpha) * (30 * k) + sin(alpha) * (60 * k) + x, cos(alpha) * (60 * k) - sin(alpha) * (30 * k) + y),
		Point(cos(alpha) * (10 * k) + x, - sin(alpha) * (10 * k) + y),
		Point(cos(alpha) * (40 * k) + x, - sin(alpha) * (40 * k) + y))
	down_fin.setFill("#d35f5f")
	eye1 = Circle(Point(cos(alpha) * (- 65 * k) + x, - sin(alpha) * (- 65 * k) + y), 9 * k)		
	eye1.setFill("#2123f6")
	eye2 = Circle(Point(cos(alpha) * (- 65 * k) + x, - sin(alpha) * (- 65 * k) + y), 5 * k)		
	eye2.setFill("#000000")

	down_fin.draw(win)
	fin.draw(win)
	up_fin.draw(win)
	fish.draw(win)
	tail.draw(win)
	eye1.draw(win)
	eye2.draw(win)


def Three_crucians(x, y, k):
	Left_Crucian(x, y, k, 0.3)
	Left_Crucian(x + 200 * k, y + 60 * k, k, 3.3)
	Right_Crucian(x - 270 * k, y + 65 * k, k, 3.1)
	

def Left_Four_crucians(x, y, k):
	Left_Crucian(x, y, k, 5.9)
	Right_Crucian(x - 105 * k, y + 10 * k, k, 6)
	Right_Crucian(x - 27 * k, y + 100 * k, k, 6.1)
	Left_Crucian(x - 210 * k, y + 90 * k, k, 0.35)


def Right_Four_crucians(x, y, k):
	Right_Crucian(x, y, k, -5.9)
	Left_Crucian(x + 105 * k, y + 10 * k, k, -6)
	Left_Crucian(x + 27 * k, y + 100 * k, k, -6.1)
	Right_Crucian(x + 210 * k, y + 90 * k, k, -0.35)



Sky()
Ice()
Horizont()
Sun(310, 100)

Three_crucians(300, 770, 0.18)
Three_crucians(160, 670, 0.12)
Three_crucians(190, 520, 0.1)
Three_crucians(390, 465, 0.085)

Left_Four_crucians(180, 740, 0.16)
Right_Four_crucians(185, 580, 0.12)
Right_Four_crucians(380, 520, 0.1)

Right_Bear(250, 460, 0.65)
Right_Bear(440, 425, 0.5)
Right_Bear(420, 630, 1.4)
Left_Bear(75, 600, 0.75)



win.getMouse()
win.close()
