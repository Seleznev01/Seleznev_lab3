Result=open("Result.txt", "a", newline="\n")
from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']
Names1 = ['Cаня', 'Глеб', 'Сережа', 'Дима' ,'Данила']
rand1 = rnd(0,4)
rand2 = rnd(0,4)
Names2 = ['Арутюнова', 'Ивановой', 'Карасева', 'Огаркова' ,'Морозова']
#def new_square():
	#global x3, y3, r3, ball3, dx3, dy3
	#canv.delete('square1')
	#y1 = rnd(70, 550)
	#r1 = rnd(30, 60)
def new_ball1():

	global x1, y1, r1, ball1, dx1, dy1, broker
	canv.delete('ball1')
	x1 = rnd(70, 400)
	y1 = rnd(70, 550)
	r1 = rnd(30, 60)
	ball1 = canv.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, fill = choice(colors), width=2, tag = 'ball1')
	dx1 = rnd(-3, 3)
	dy1 = rnd(-3, 3)
	def move1():
		global x1, y1, dx1, dy1
		canv.move(ball1, dx1, dy1)
		x1 = x1 + dx1
		y1 = y1 + dy1
		root.after(50, move1)
		if (x1 <= 0) or (x1 >= 800):
			dx1 = - dx1
		if (y1 <= 0) or (y1 >= 600):
			dy1 = - dy1
	move1()
def new_ball2():
	global x2, y2, r2, ball2, dx2, dy2
	canv.delete('ball2')
	x2 = rnd(70, 700)
	y2 = rnd(70, 550)
	r2 = rnd(30, 60)
	ball2 = canv.create_oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2, fill=choice(colors), width=2, tag='ball2')
	dx2 = 2
	dy2 = -2
	def move2():
		global x2, y2, dx2, dy2
		canv.move(ball2, dx2, dy2)
		x2 = x2 + dx2
		y2 = y2 + dy2
		root.after(50, move2)
		if (x2 <= 0) or (x2 >= 800):
			dx2 = - dx2
		if (y2 <= 0) or (y2 >= 600):
			dy2 = - dy2
	move2()
count=0
def click(event):
	global count, x1, y1, x2, y2, broker1
	if ((event.x - x1) ** 2 + (event.y - y1) ** 2) ** 0.5 <= r1:
		canv.delete('ball1')
		canv.delete('count')
		canv.create_text(750, 50, text='БРС='+str(count + 1), justify = CENTER, font = "Verdana 14", tag = 'count')
		count = count + 1
		new_ball1()
	if ((event.x - x2) ** 2 + (event.y - y2) ** 2) ** 0.5 <= r2:
		canv.delete('ball2')
		canv.delete('count')
		canv.create_text(750, 50, text='БРС='+str(count + 1), justify = CENTER, font = "Verdana 14", tag = 'count')
		count = count + 1
		new_ball2()
canv.bind('<Button-1>', click)
new_ball1()
new_ball2()
def myf():
	global count
	Result.write(Names1[rand1] + " получил " + str(count) + " на коллоке у " + Names2[rand2] + '\n')
	root.destroy()
root.protocol('WM_DELETE_WINDOW', myf)
root.mainloop()
Result.close()



