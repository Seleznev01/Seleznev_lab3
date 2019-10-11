from graph import *
def window(x,y):
    penColor('white')
    brushColor('white')
    #Окно снизу справа
    rectangle(x,y,x-40,y-60) #большая рамка
    brushColor(164,223,242)
    rectangle(x-1,y-1,x-39,y-59)#малая рамка
    penSize(3)
    line(x,y-40,x-40,y-40)
    line(x-20,y,x-20,y-60)
    penSize(3)
#
def oval(a,b,x,y):
    list=[]
    if int(a)!=0:
        for i in range(int(-a),int(a),1):
            z=y+b*((1-(i/a)**2)**(0.5))
            list.append((i+x,z))
        for i in range(int(a),int(-a),-1):
            z2 = y - b * ((1 - (i / a) ** 2) ** (0.5))
            list.append((i + x, z2))
        return list
    else:
        penSize(2)
        return [(x,y-b),(x,y+b)]

def ellipse (x,y,x1,y1,a):
    list1=[]
    for i in range(min(int(x1), int(x)) - int(a), max(int(x1), int(x)) + int(a), ++1):
        for j in range(min(int(y1), int(y)) - int(a), max(int(y1), int(y)) + int(a), ++1):
            if ((x - i) ** 2 + (y - j) ** 2) ** 0.5 + ((x1 - i) ** 2 + (y1 - j) ** 2) ** 0.5 <= a:
                list1.append((point(i, j)))
    for i in range(min(int(x1),int(x)) - int(a), max(int(x1),int(x)) + int(a), ++1):
        for j in range(min(int(y1),int(y)) - int(a), max(int(y1),int(y)) + int(a), ++1):
            if int(((x-i)**2 + (y-j)**2)**0.5 + ((x1-i) ** 2+ (y1-j) **2) **0.5 )== int(a):
                penColor('black')
                list1.append((point(i,j)))
    return list1


def klubok(size,x,y):#координаты относительно начала СО
    brushColor(153,153,153)
    circle(x,y,28*size)
    polyline([(x+12*size, y+8*size),(x+10*size,y ),(x+5*size, y-3*size),(x-8*size,y-15*size)]) # вторая линия сверху
    polyline([(x+20*size,y+1*size),(x,y-13*size),(-5*size+x,y-18*size),(-16*size+x,-24*size+y)])# первая линия сверху
    polyline([(x+5*size, y+24*size),(+8*size+x,17*size+y),(+12*size+x,10*size+y)])# самая правая
    polyline([(x-5*size,26*size+y),(-2*size+x,18*size+y),(+5*size+x,2*size+y)])# снизу в середине
    polyline([(-15*size+x,23*size+y),(-10*size+x,18*size+y),(-5*size+x,-3*size+y)])# самая левая снизу
def kot(x,y,color,lr,size):
    listkot=[]
    if color==1:
        brushColor(200, 113, 55)
        penColor(200,113,55)
    else:
        brushColor(108,93,83)
        penColor(108,93,83)
    listkot.extend(ellipse(x+70*size*lr,y,x+130*size*lr,y+40*size,80*size))
    penColor('black')
    listkot.append((polygon(oval(size * 80, size * 40, x, y))))
    listkot.append(polygon(oval(size*12,size*24,x - 88 * size*lr, y + 12 * size)))
    listkot.append(circle(x + 55*size*lr, y + 20*size, size * 20))
    listkot.append(polygon(oval(size*10,size*20,x+70*size*lr,y+45*size)))
    listkot.append(circle(x-75*size*lr,y-5*size,size*32))
    listkot.append(polygon(oval(size*23,size*13,x-55*size*lr,y+37*size)))
    brushColor(223,171,135)
    listkot.append(polygon([(x-105*size*lr,y-20*size),(x-105*size*lr,y-40*size),(x-90*size*lr,y-30*size)]))
    listkot.append(polygon([(x-60*size*lr,y-30*size),(x-45*size*lr,y-40*size),(x-45*size*lr,y-20*size)]))
    listkot.append(polygon([(x-71*size*lr,y+10*size),(x-79*size*lr,y+10*size),(x-75*size*lr,y+14*size)]))

    line(x-75*size*lr, y+14*size, x-75*size*lr, y+18*size)
    if color==1:
        brushColor(136, 170, 0)
    else:
        brushColor(42,212,255)
    listkot.append(circle(x-88*size*lr,y-2*size,size*9))
    listkot.append(circle(x-60*size*lr,y-2*size,size*9))
    brushColor('black')
    listkot.append(polygon(oval(size*8,size*1,x-88*size*lr,y-2*size)))# зрачки в правом глазу
    listkot.append(polygon(oval(size*8,size*1,x-60*size*lr,y-2*size)))# зрачки в левом глазу
    penSize(1)
    return listkot
brushColor(125,104,0)
rectangle(0,313,500,700)
brushColor(85,70,0)
rectangle(0,0,500,313)
#Делаем окна по циклам
for i in range(7):
    for j in range(3):
        window(40*(i+1)+30*(i+1),60*(j+1)+50*(j))
x0=85
y0=380
x=-50
y=50
brushColor(190,110,60)
penColor(190,110,60)
penSize(1)
cr0=1
cr1=1
cr2=-1
cr3=1
cr4=-1
cr5=1
kot0=kot(85,380,cr0,-1,0.3)
kot1=kot(143,451,cr1,-1,1)
kot2=kot(170,550,cr2,-1,0.3)
kot3=kot(360,500,cr3,1,0.3)
kot4=kot(450,450,cr4,-1,0.3)
kot5=kot(450,550,cr5,1,0.3)
def moving0(OBJ):
    global x0
    global y0
    global x
    global y
    for obj in OBJ:
        if (x0 < 0) and (x < 0):
            x = -x
        if (x0 > 500) and (x > 0):
            x = -x
        if (y0 < 0) and (y < 0):
            y = -y
        if (y0 > 600) and (y > 0):
            y = -y
        moveObjectBy(obj, x, y)
    x0=x0+x
    y0=y0+y
x02=170
y02=550
x2=40
y2=-40
def moving2(OBJ):
    global x02
    global y02
    global x2
    global y2
    for obj in OBJ:
        if (x02 < 0) and (x2 < 0):
            x2 = -x2
        if (x02 > 500) and (x2 > 0):
            x2 = -x2
        if (y02 < 0) and (y2 < 0):
            y2 = -y2
        if (y02 > 600) and (y2 > 0):
            y2 = -y2
        moveObjectBy(obj, x2, y2)
    x02=x02+x2
    y02=y02+y2
x01=140
y01=450
x1=1
y1=-1
def moving1(OBJ):
    global x01
    global y01
    global x1
    global y1
    for obj in OBJ:
        if (x01 < 0) and (x1 < 0):
            x1 = -x1
        if (x01 > 500) and (x1 > 0):
            x1 = -x1
        if (y01 < 0) and (y1 < 0):
            y1 = -y1
        if (y01 > 600) and (y1 > 0):
            y1 = -y1
        moveObjectBy(obj, x1, y1)
    x01=x01+x1
    y01=y01+y1
def update():
    moving0(kot0)
    moving1(kot1)
    moving2(kot2)
    #moving(kot3)
    #moving(kot4)
    #moving(kot5)
onTimer(update, 1)
klubok(0.5,375,550)
klubok(0.5,150,370)
klubok(0.5,375,460)
klubok(1.5,300,550)
klubok(1,450,500)
klubok(1,300,460)
klubok(0.5,100,550)
run()
