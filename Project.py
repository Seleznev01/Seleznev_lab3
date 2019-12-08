from random import randrange as rnd, choice
from tkinter import *
import math
import time
def Menu():
    global window # экран, отвечающий за интерфейс
    window = Tk()
    window.title("Doodle Jump")
    window.geometry("350x350")
    window.configure(background= 'green')
    lbl2 = Label(window,text=' Doodle Jump',font='Times 30', fg= "red", bg="green")
    lbl2.place(x=60, y=10)
    def back_to_menu(event):
        window.destroy()
        Menu()
    button_1 = Button(text="Start", width=20, height=3, font='arial 14', bg="green")
    def NEW_GAME(event):
        global button_1
        window.destroy()
        main()
    button_1.bind('<Button-1>', NEW_GAME)
    button_1.place(x=60, y=80)
    button_2=Button(text="Instruction", width=20, height=3, font='arial 14', bg="green" )
    def Instruction(event):
        global button1, button2, button3
        lbl1 = Label(window, text= "Цель игры заключается в том,\n чтобы пропрыгать как можно выше,\n если вы упадете, то проиграте\n "
        "Чтобы двигатся влево нажмите 'A', \n  вправо 'D'. Удачной игры!!! ", font='Times 14', fg='black', bg="green")
        lbl1.pack()
        button_1.destroy()
        button_2.destroy()
        button_3 = Button(text="Вернуться к меню", width=20, height=5, font='arial 14', bg="green")

        button_3.bind('<Button-1>', back_to_menu)
        button_3.pack()

    button_2.bind('<Button-1>', Instruction)
    button_2.place(x=60, y=200)
    window.mainloop()
    def main():
        return 0
Menu()


