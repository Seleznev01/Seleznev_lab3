from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg = 'white')
canv.pack(fill = BOTH,expand = 1)

def Name():
        print('NAME:')
        name = str(input())
        file = open('Players.txt', 'a')
        file.write(name)
        file.write(' - ')
        file.close()
colors = ['red','orange','yellow','green','blue']
score = 0
Name()
Balls = []
mistake=0

class Ball:

        def __init__(self):
                self.x = rnd(100, 700)
                self.y = rnd(100, 500)
                self.r = rnd(30, 50)
                self.dx = rnd(-2, 2)
                self.dy = rnd(-2, 2)
                self.obj = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r,
                                            self.y + self.r, fill = choice(colors), width = 2, tag = 'ball')
        def Refr(self):
                if self.x <= self.r or self.x >= 800 - self.r:
                        self.dx = - self.dx
                if self.y <= self.r or self.y >= 600 - self.r:
                        self.dy = - self.dy

        def Move(self):
                self.x = self.x + self.dx
                self.y = self.y + self.dy
                canv.move(self.obj, self.dx, self.dy)
        def Delete(self):
                canv.delete(self.obj)


        
def Create():
        global Numb
        for i in range(Numb):
                Balls.append(Ball())
                        
def Play():
        for i in Balls:
                i.Move()
                i.Refr()
        root.after(20, Play)

def Start():

        global Numb,count
        Numb = rnd(1,10)
        canv.delete('ball')
        Create()
        Play()
def click(event):
        global Numb, score, mistake
        mistake +=1
        for i in Balls:
                if ((event.x - i.x) ** 2 + (event.y - i.y) ** 2) ** 0.5 <= i.r:
                        score += 1
                        canv.delete('score')
                        canv.create_text(750, 50, text = str(score), justify = CENTER, font = "Verdana 14", tag = 'score')
                        i.Delete()
                        mistake -=1
                        Balls.remove(i)
                        Balls.append(Ball())
        if mistake==6:
                root.quit()
                print('Score:', score)
                file = open('Players.txt', 'a')
                file.write(str(score))
                file.write('\n')
                file.close()
canv.bind('<Button-1>', click)
Start()
mainloop()
