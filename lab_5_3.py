
from random import randrange as rnd, choice
import tkinter as tk
import math
import time
global root
root=tk.Tk()
def main():
    global screen
    global root
    global n
    global root1
    root1 = tk.Tk()
    fr = tk.Frame(root1)
    root1.geometry('800x600')
    canv = tk.Canvas(root1, bg='white')
    canv.pack(fill=tk.BOTH, expand=1)
    screen= canv.create_text(400, 300, text='', font='28')
    global bullet
    global balls
    bullet = 0
    balls = []

    class ball():
        def __init__(self, x=20, y=450):
            """ Конструктор класса ball
            Args:
            x - начальное положение мяча по горизонтали
            y - начальное положение мяча по вертикали
            """
            self.x = x
            self.y = y
            self.r = 10
            self.vx = 0
            self.vy = 0
            self.ay = 1.5
            self.xtr = 0
            self.ytr = 0
            self.color = choice(['blue', 'green', 'red', 'brown'])
            self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
            )
            self.live = 30

        def set_coords(self):
            canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
            )

        def move(self):
            """Переместить мяч по прошествии единицы времени.
            Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
            self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
            и стен по краям окна (размер окна 800х600).
            """
            self.xtr = -0.1 * self.vx
            self.ytr = -0.1 * self.vy
            if (self.x - self.r < 0 or self.x + self.r > 800):
                self.vx = -self.vx
                self.ytr = -0.1 * self.vy
                self.vy += self.ay + self.ytr
            elif (self.y - self.r < 0 or self.y + self.r > 600):
                self.vy = -self.vy
                self.vx += self.xtr
                self.vy += self.ay
            else:
                self.vy += self.ay
            self.vy += self.ay
            self.y += self.vy
            self.x += self.vx
            canv.move(self.id, self.vx, self.vy)
            if self.y + self.r > 650:
                self.vy = 0
                self.ay = 0
                self.vx = 0
                self.xtr = 0
                self.ytr = 0
                canv.delete(self.id)

        def hittest(self, obj):
            """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
            Args:
                obj: Обьект, с которым проверяется столкновение.
            Returns:
                Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
            """
            if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (obj.r + self.r) ** 2:
                return True
            else:
                return False

    class gun():
        def __init__(self):
            self.f2_power = 10
            self.f2_on = 0
            self.an = 1
            self.vy = 5
            self.x = 20
            self.y = 450
            self.id = canv.create_line(self.x, self.y, self.x + 30, self.y - 20,
                                       width=7)

        def onclick1(self, event):
            self.y -= 5
            # canv.move(self.id, 0, self.vy)

        def onclick2(self, event):
            self.y += 5

        def fire2_start(self, event):
            self.f2_on = 1

        def fire2_end(self, event):
            """Выстрел мячом.
            Происходит при отпускании кнопки мыши.
            Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
            """
            global balls, bullet
            bullet += 1
            new_ball = ball(g1.x, g1.y)
            new_ball.r += 5
            self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
            new_ball.vx = self.f2_power * math.cos(self.an)
            new_ball.vy = self.f2_power * math.sin(self.an)
            balls += [new_ball]
            self.f2_on = 0
            self.f2_power = 10

        def targetting(self, event=0):
            """Прицеливание. Зависит от положения мыши."""
            if event:
                self.an = math.atan((event.y - 450) / (event.x - 20))
            if self.f2_on:
                canv.itemconfig(self.id, fill='orange')
            else:
                canv.itemconfig(self.id, fill='black')
            canv.coords(self.id, self.x, self.y,
                        self.x + max(self.f2_power, 20) * math.cos(self.an),
                        self.y + max(self.f2_power, 20) * math.sin(self.an)
                        )

        def power_up(self):
            if self.f2_on:
                if self.f2_power < 100:
                    self.f2_power += 1
                canv.itemconfig(self.id, fill='orange')
            else:
                canv.itemconfig(self.id, fill='black')

    class target():
        def __init__(self, n):
            self.points = 0
            self.live = 1
            self.id = canv.create_oval(0, 0, 0, 0)
            self.color = n
            x = self.x = rnd(600, 780)
            y = self.y = rnd(300, 550)
            r = self.r = rnd(2, 50)
            vx = self.vx = rnd(-10, 10)
            vy = self.vy = rnd(-10, 10)
            dx = self.dx = vx
            dy = self.dy = vy
            canv.coords(self.id, x - r, y - r, x + r, y + r)
            canv.itemconfig(self.id, fill = self.color)

        def hit(self, points=1):
            """Попадание шарика в цель"""
            canv.coords(self.id, -10, -10, -10, -10)

        def move2(self):
            """Движение мишени"""
            self.x += self.dx
            self.y += self.dy
            if ((canv.coords(self.id)[2] + self.dx >= 800) and self.dx > 0) \
                    or ((canv.coords(self.id)[0] + self.dx <= 200) and (self.dx < 0)):
                self.dx = -self.dx
            if ((canv.coords(self.id)[3] + self.dy >= 600) and self.dy > 0) \
                    or ((canv.coords(self.id)[1] + self.dy <= 10) and self.dy < 0):
                self.dy = -self.dy
            if canv.coords(self.id)[0] == -10:
                self.dx = 0
                self.dy = 0
            canv.move(self.id, self.dx, self.dy)
    global g1
    g1 = gun()
    global targets
    targets= []
    def new_game(event=''):
        global t1,balls, bullet, gun, n, root
        global screen
        global targets
        for i in range(5):
            targets.append(target(n))
        bullet = 0
        balls = []
        root.bind("<KeyPress-Up>", g1.onclick1)
        root.bind("<KeyPress-Down>", g1.onclick2)
        canv.bind('<Button-1>', g1.fire2_start)
        canv.bind('<ButtonRelease-1>', g1.fire2_end)
        canv.bind('<Motion>', g1.targetting)
        z = 0.03
        for i in targets:
            i.live = 1
        while len(targets) != 0 or balls:
            for b in balls:
                if b.vx == 0 and b.vy == 0:
                    canv.delete(b.id)
                b.move()
                for i in targets:
                    if b.hittest(i) and i.live:
                        i.live = 0
                        i.hit()
                        targets.remove(i)
            if len(targets) == 0:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов' +'\n'+'Ждем Вас снова в нашей игре(нет) ' )
            canv.update()
            time.sleep(z)
            g1.targetting()
            g1.power_up()
            for i in targets:
                i.move2()
        canv.itemconfig(screen, text='')
        canv.delete(gun)
        root1.after(750, new_game)
    def on_closing():
        global root, root1
        root1.destroy()
        root.deiconify()
    root1.protocol("WM_DELETE_WINDOW", on_closing)

    new_game()
    root1.mainloop()

n=0
root.geometry("300x300")
men = tk.Canvas(root, width=200, height=200, bg='white')
b = tk.Button(text="Начать гамать", width=20, height=3, font='arial 14')
def NEW_GAME(event):
    global b, n
    if (n==0):
        n='green'
    root.iconify()
    main()
b.place(x=250, y=300)
b.bind('<Button-1>', NEW_GAME)
b.pack()
c=tk.Button(text="Настройки", width=20, height=3, font='arial 14')
def Settings(event):
    global d, e, f, n
    d=tk.Button(text="Синие Мишеньки")
    def Parametr1(event):
            global n
            n='blue'
            d.destroy()
            e.destroy()
            f.destroy()
    def Parametr2(event):
            global n
            n= 'red'
            d.destroy()
            e.destroy()
            f.destroy()
    def Parametr3(event):
            global n
            n= 'yellow'
            d.destroy()
            e.destroy()
            f.destroy()
    e=tk.Button(text="Красные мишеньки")
    f=tk.Button(text="Вау, да это же желтые мишеньки")
    d.bind('<Button-1>', Parametr1)
    e.bind('<Button-1>', Parametr2)
    f.bind('<Button-1>', Parametr3)
    d.pack()
    e.pack()
    f.pack()
c.bind('<Button-1>', Settings)
c.place(x=250, y=300)
c.pack()
root.mainloop()
