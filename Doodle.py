from tkinter import *
from random import *
from time import *

root = Tk()

c = Canvas(root, width=800, height=1000, bg='white')
c.pack()
root.geometry('800x1000')
v_0 = 0.5  # скорость при отскоке от платформы
Level = 400  # линия, выше которой не поднимается изображение дудла на экране
P_Width = 80  # ширина платформы
P_Height = 5  # толщина платформы
doodle_stop = False  # переменная отвечает за тип движения объектов (true - движутся платформы, false - дудл)
start = True  # отвечает за начало игры
pause = False  # отвечает за приостановку игры
p_lim = 90  # начальная вероятность появления платформы


# функция рисует иконку дудла
def doodle_draw(x, y):
    c.create_oval(x + 15, y - 35, x + 45, y - 5, tags="doodle", fill="blue")
    c.create_rectangle(x, y - 20, x + 60, y, tags="doodle", fill="green")
    c.create_line(x, y, x, y + 10, tags="doodle")
    c.create_line(x + 20, y, x + 20, y + 10, tags="doodle")
    c.create_line(x + 40, y, x + 40, y + 10, tags="doodle")
    c.create_line(x + 60, y, x + 60, y + 10, tags="doodle")


# класс дудла
class Doodle():

    def __init__(self):
        self.x = 300
        self.y = 600
        self.vx = 10
        self.vy = 0
        self.g = 0
        self.life = True
        doodle_draw(self.x, self.y)

    def upd(self):
        if self.y > 800:
            self.life = False
        self.vy -= self.g
        if not doodle_stop:
            self.y -= self.vy
            c.move("doodle", 0, -self.vy)

    def move_left(self):
        if self.x < -60:
            self.x -= self.vx - 800
            c.move("doodle", 800 - self.vx, 0)
        else:
            self.x -= self.vx
            c.move("doodle", - self.vx, 0)

    def move_right(self):
        if self.x > 800:
            self.x += self.vx - 800
            c.move("doodle", -800 + self.vx - 30, 0)
        else:
            self.x += self.vx
        c.move("doodle", self.vx, 0)


# собственно его единственный экземпляр
doodle = Doodle()


# класс платформ
class Platform():

    def __init__(self, x1, y1):
        self.width = P_Width
        self.height = P_Height
        self.x = x1
        self.y = y1
        self.vx = 0
        self.vy = 0
        self.life = True
        self.obj = c.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill='green')

    def upd(self):
        if self.y > 1600:
            self.life = False
        self.y += doodle.vy
        c.move(self.obj, 0, doodle.vy)


# это массив платформ
platforms = []


# функция,которая гененрирует платформы во время игры
def generate_extra_platforms():
    n = 1
    h = 10
    l = platforms[len(platforms) - 1].y
    if doodle.y <= Level and -400 < l < 0:
        for i in range(1, 40):
            for k in range(1, 10):
                a = randrange(1, 100)
                if a > p_lim:
                    platforms.append(Platform((k - 1) * P_Width, l - (i - 1) * h))


# функция,которая генерирует платформы в начале игры:
def generate_platforms():
    global P_Width, P_Height
    h = 15
    for i in range(1, 100):
        for k in range(0, 10):
            a = randrange(1, 100)
            if a > p_lim:
                platforms.append(Platform(k * P_Width, (i - 1) * h))


# проверяет, напрыгнул ли дудл на платформу, а ещё удаляет платформы ниже экрана (по всем платформам)
def jump_check():
    for p in platforms:
        if not p.life:
            c.delete(p.obj)
            platforms.remove(p)
        elif (doodle.vy <= 0) and (p.x - 60 < doodle.x < p.x + p.width) and (p.y - 10 <= doodle.y <= p.y + P_Height):
            doodle.vy = v_0


# функция, которая проверяет, что должно двигаться : дудл или платформы
def change_check():
    global doodle_stop
    if doodle.y <= Level and doodle.vy >= 0:
        doodle_stop = True
    elif doodle.vy < 0:
        doodle_stop = False


# движение всех объектов на экране
def scr_upd():
    doodle.upd()
    if doodle_stop:
        for p in platforms:
            p.upd()
    c.update()


# запуск игры
def start_game():
    global start
    if not start:
        c.delete(ALL)
        generate_platforms()  # функция, которая генерит платформы в начале
        start = True
        game_main()
    else:
        c.delete(ALL)


# приостановка и возобновление игры
def pause_game(event):
    global doodle, pause, d_vy, g_0, platforms, platforms_data
    if start and pause:
        pause = False
    elif start and not pause:
        pause = True


# выход из игры
def stop_game(event):
    global start
    if start:
        c.delete(ALL)
        start = False


def key(event):
    if (event.char == 'a'):
        doodle.move_left()
    if (event.char == 'd'):
        doodle.move_right()


checker = 0


# основной ход игры ПРОБЛЕМА - не знаю, как реализовать
def game_main():
    global start, v_0, p_lim, Level, checker
    if start:
        c.bind('<Key>', key)
        generate_platforms()
        doodle.vy = v_0
        doodle.g = 0.001
        while doodle.life:
            jump_check()
            change_check()
            # generate_extra_platforms()
            if not pause:
                scr_upd()  # функция, которая занимается движением всего на экране


Res = open("Res.txt", "a", newline="\n")
check = 0


def Menu():
    global check  # Счетчик для проверки на сохранение имени
    global Res  # Файл с результатами
    global window  # экран, отвечающий за интерфейс
    window = Tk()
    window.title("Doodle Jump")
    window.geometry("350x400")
    window.configure(background='blue')
    lbl2 = Label(window, text=' Doodle Jump', font='Times 30', fg="white", bg="blue")  # Название игры
    lbl2.place(x=60, y=10)
    button_1 = Button(window,text="Start", width=20, height=3, font='arial 14', bg="light yellow")
    button_1.place(x=60, y=220)  # кнопка, отвечающая за старт игры
    button_2 = Button(window,text="Instruction", width=20, height=3, font='arial 14', bg="light green")
    button_2.place(x=60, y=310)  # кнопка, отвечающая за инструкцию
    lbl_name = Label(window,
                     text='Привет, рады видеть тебя в нашей игры \n Для начала представься',
                     font='Times 14', fg="black", bg="blue")
    lbl_name.place(x=22, y=60)  # Приветствие
    txt = Entry(window, width=10)  # Записываем имя
    txt.place(x=140, y=105)  # окно для ввода имени
    button_save = Button(window, text="Save name", width=20, height=3, font='arial 14', bg="pink")  # сохранение имени
    button_save.place(x=60, y=130)
    lbl_gl = Label(window, font='Times 14', fg="black", bg="blue")  # Пожелание хорошей игры
    lbl_gl.place(x=20, y=60)

    if (check == 1):  # Проверка на дибила, если имя не записал
        lbl_name.destroy()
        lbl_name = Label(window,
                         text='Ты забыл написать имя - напиши \n И начинай игру'
                         ,
                         font='Times 14', fg="black", bg="blue")
        lbl_name.place(x=40, y=50)
    if (check == 2):  # Проверка на дибила, если имя написал
        lbl_name.destroy()
        lbl_name = Label(window,
                         text='Все отлично, ты готов ко всему \n Начинай игру!'
                         ,
                         font='Times 14', fg="black", bg="blue")
        lbl_name.place(x=40, y=50)
        txt.destroy()
        button_save.place(x=1500, y=1500)
        button_1.place(x=60, y=100)
        button_2.place(x=60, y=190)

    def save(event):
        global check
        s = txt.get()
        lbl_gl['text'] = 'Молодец, теперь прочитай инструкцию, \n если еще этого не сделал \n и начинай игру '
        lbl_name.destroy()
        Res.write(txt.get() + ' ')
        txt.destroy()
        check = 2
        button_save.destroy()
        button_1.place(x=60, y=130)
        button_2.place(x=60, y=220)

    def back_to_menu(event):
        global check
        if (check == 0):
            check = 1
        window.destroy()
        Menu()

    def NEW_GAME(event):
        global button_1
        window.destroy()
        c.focus_set()
        game_main()
        root.deiconify()

    def Instruction(event):
        global button1, button2, button3
        lbl1 = Label(window,
                     text="Цель игры заключается в том,\n чтобы пропрыгать как можно выше,\n если вы упадете, то проиграте\n "
                          "Чтобы двигатся влево нажмите 'A', \n  вправо 'D'. Удачной игры!!! ", font='Times 14',
                     fg='black', bg="blue")
        lbl1.pack()
        button_1.destroy()
        button_2.destroy()
        lbl_name.destroy()
        lbl_gl.destroy()
        button_3 = Button(window, text="Вернуться к меню", width=20, height=5, font='arial 14', bg="light blue")

        button_3.bind('<Button-1>', back_to_menu)
        button_3.pack()

    button_save.bind('<Button-1>', save)  # Сохранение имени
    button_1.bind('<Button-1>', NEW_GAME)  # Начало игры
    button_2.bind('<Button-1>', Instruction)  # Инструкция

    window.mainloop()

Menu()  # вызывает в самом начале меню для игры
mainloop()
withdraw(window)
