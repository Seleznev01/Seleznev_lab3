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
    for i in range(min(int(x1),int(x)) - int(a), max(int(x1),int(x)) + int(a), ++1):
        for j in range(min(int(y1),int(y)) - int(a), max(int(y1),int(y)) + int(a), ++1):
            if ((x-i)**2 + (y-j)**2)**0.5 + ((x1-i) ** 2+ (y1-j) **2) **0.5 <= a:
                point(i,j)
    for i in range(min(int(x1),int(x)) - int(a), max(int(x1),int(x)) + int(a), ++1):
        for j in range(min(int(y1),int(y)) - int(a), max(int(y1),int(y)) + int(a), ++1):
            if int(((x-i)**2 + (y-j)**2)**0.5 + ((x1-i) ** 2+ (y1-j) **2) **0.5 )== int(a):
                penColor('black')
                point(i,j)


def klubok(size,x,y):#координаты относительно начала СО
    brushColor(153,153,153)
    circle(x,y,28*size) 
    polyline([(x+12*size, y+8*size),(x+10*size,y ),(x+5*size, y-3*size),(x-8*size,y-15*size)]) # вторая линия сверху
    polyline([(x+20*size,y+1*size),(x,y-13*size),(-5*size+x,y-18*size),(-16*size+x,-24*size+y)])# первая линия сверху
    polyline([(x+5*size, y+24*size),(+8*size+x,17*size+y),(+12*size+x,10*size+y)])# самая правая
    polyline([(x-5*size,26*size+y),(-2*size+x,18*size+y),(+5*size+x,2*size+y)])# снизу в середине
    polyline([(-15*size+x,23*size+y),(-10*size+x,18*size+y),(-5*size+x,-3*size+y)])# самая левая снизу
def kot(x,y,color,lr,size):
    if color==1:
        brushColor(200, 113, 55)
        penColor(200,113,55)
    else:
        brushColor(108,93,83)
        penColor(108,93,83)
    ellipse(x+70*size*lr,y,x+130*size*lr,y+40*size,80*size)
    penColor('black')
    polygon(oval(size * 80, size * 40, x, y))
    polygon(oval(size*12,size*24,x - 88 * size*lr, y + 12 * size))
    circle(x + 55*size*lr, y + 20*size, size * 20)
    polygon(oval(size*10,size*20,x+70*size*lr,y+45*size))
    circle(x-75*size*lr,y-5*size,size*32)
    polygon(oval(size*23,size*13,x-55*size*lr,y+37*size))
    brushColor(223,171,135)
    polygon([(x-105*size*lr,y-20*size),(x-105*size*lr,y-40*size),(x-90*size*lr,y-30*size)])
    polygon([(x-60*size*lr,y-30*size),(x-45*size*lr,y-40*size),(x-45*size*lr,y-20*size)])
    polygon([(x-71*size*lr,y+10*size),(x-79*size*lr,y+10*size),(x-75*size*lr,y+14*size)])

    line(x-75*size*lr, y+14*size, x-75*size*lr, y+18*size)
    if color==1:
        brushColor(136, 170, 0)
    else:
        brushColor(42,212,255)
    circle(x-88*size*lr,y-2*size,size*9)
    circle(x-60*size*lr,y-2*size,size*9)
    brushColor('black')
    polygon(oval(size*8,size*1,x-88*size*lr,y-2*size))# зрачки в правом глазу
    polygon(oval(size*8,size*1,x-60*size*lr,y-2*size))# зрачки в левом глазу
    penSize(1)

brushColor(125,104,0)
rectangle(0,313,500,700)
brushColor(85,70,0)
rectangle(0,0,500,313)
#Делаем окна по циклам
for i in range(7):
    for j in range(3):
        window(40*(i+1)+30*(i+1),60*(j+1)+50*(j))  
brushColor(190,110,60)
penColor(190,110,60)
penSize(1)
kot(335,373,1,1,1)
kot(85,380,1,-1,0.3)
kot(143,451,-1,-1,1)
kot(170,550,-1,-1,0.3)
kot(360,500,1,1,0.3)
kot(450,450,1,-1,0.3)
kot(450,550,-1,1,0.3)
klubok(0.5,375,550)
klubok(0.5,150,370)
klubok(0.5,375,460)
klubok(1.5,300,550)
klubok(1,450,500)
klubok(1,300,460)
klubok(0.5,100,550)
run()
