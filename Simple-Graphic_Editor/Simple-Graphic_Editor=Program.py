import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showerror, showwarning, showinfo
import pyscreenshot
from PIL import ImageTk, Image

ScreenX = 400
ScreenY = 400

root = Tk()
root.title("SGEditor | Dvoryanchikov51")
root.geometry(str(ScreenX)+'x'+str(ScreenY))
root.resizable(False, False)
root.option_add("*tearOff", FALSE)

cnv = Canvas(bg="white", width=ScreenX, height=ScreenY)
cnv.pack(anchor=N, fill="both", expand=1)

def NewPosition():
    root.geometry("+0+0")
def SaveScreen():
    image = pyscreenshot.grab(bbox=(14, 42, ScreenX+106, ScreenY+131))
    image.save("SGEpic.png")
def exit_click():
    root.destroy()
def menu_ClearScreen():
    cnv.delete("all")
def menu_ClearСursor():
    cnv.delete("ln")

logic_NaturalAlgorithmLine = False
logic_BresenhamAlgorithmLine = False
logic_NaturalAlgorithmCircle = False
logic_RecursiveAlgorithmSeed = False
logic_AlgorithmBarkBeetle = False
def menu_NaturalAlgorithmLine():
    global logic_NaturalAlgorithmLine
    logic_NaturalAlgorithmLine = True if not logic_NaturalAlgorithmLine else False
    print('logic_NaturalAlgorithmLine:',logic_NaturalAlgorithmLine)
def menu_BresenhamAlgorithmLine():
    global logic_BresenhamAlgorithmLine
    logic_BresenhamAlgorithmLine = True if not logic_BresenhamAlgorithmLine else False
    print('logic_BresenhamAlgorithmLine:',logic_BresenhamAlgorithmLine)
def menu_NaturalAlgorithmCircle():
    global logic_NaturalAlgorithmCircle
    logic_NaturalAlgorithmCircle = True if not logic_NaturalAlgorithmCircle else False
    print('logic_NaturalAlgorithmCircle',logic_NaturalAlgorithmCircle)
def menu_RecursiveAlgorithmSeed():
    global logic_RecursiveAlgorithmSeed
    logic_RecursiveAlgorithmSeed = True if not logic_RecursiveAlgorithmSeed else False
    print('logic_RecursiveAlgorithmSeed',logic_RecursiveAlgorithmSeed)
def menu_AlgorithmBarkBeetle():
    global logic_AlgorithmBarkBeetle
    logic_AlgorithmBarkBeetle = True if not logic_AlgorithmBarkBeetle else False
    print('logic_AlgorithmBarkBeetle',logic_AlgorithmBarkBeetle)

main_menu = Menu()
#
save_menu = Menu()
save_menu.add_command(label="Step-1 (Position)", command=NewPosition)
save_menu.add_command(label="Step-2 (Screen)", command=SaveScreen)

file_menu = Menu()
file_menu.add_command(label="New")
file_menu.add_command(label="Clear Screen", command=menu_ClearScreen)
file_menu.add_command(label="Clear Cursor", command=menu_ClearСursor)
file_menu.add_cascade(label="Save", menu=save_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_click)

#
draw_menuline = Menu()
draw_menuline.add_checkbutton(label="Естественный алгоритм рисования прямой", command=menu_NaturalAlgorithmLine)
draw_menuline.add_checkbutton(label="Алгоритм Брезенхама рисования прямой", command=menu_BresenhamAlgorithmLine)
draw_menuline.add_checkbutton(label="Естественный алгоритм рисования окружности", command=menu_NaturalAlgorithmCircle)
draw_menuline.add_separator()
draw_menuline.add_command(label="Clear Screen", command=menu_ClearScreen)

draw_menupaint = Menu()
draw_menupaint.add_checkbutton(label="Рекурсивный алгоритм с 'затравкой'", command=menu_RecursiveAlgorithmSeed)
draw_menupaint.add_checkbutton(label="Алгоритм 'Короеда'", command=menu_AlgorithmBarkBeetle)
draw_menupaint.add_separator()
draw_menupaint.add_command(label="Clear Screen", command=menu_ClearScreen)
#
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Draw-lines", menu=draw_menuline)
main_menu.add_cascade(label="Draw-PaintOver", menu=draw_menupaint)


BlackPixel = []
def DrawDrawing(event):
    x = event.x
    y = event.y
    BlackPixel.append([x, y])
    BlackPixel.append([x+1, y])
    BlackPixel.append([x, y+1])
    BlackPixel.append([x-1, y])
    BlackPixel.append([x, y-1])
    cnv.create_rectangle(x, y, x + 1, y + 1, fill="#000000", outline="#000000")


def ClearScreen(event):
    cnv.delete("all")
def ClearСursor(event):
    cnv.delete("ln")
def Сursor(event):
    x = event.x
    y = event.y
    cnv.delete("ln")
    cnv.create_line(x,0,x,ScreenY, fill="red", tag="ln")
    cnv.create_line(0, y, ScreenX, y, fill="red", tag="ln")
    cnv.create_text(x - 90, y - 17, font="TimesNewRoman 10", anchor=NW, text="x: " + str(x) + " | y: " + str(y),
                    fill="#00BFFF", tag="ln")
    cnv.create_text(40, 10, text="x: " + str(x) + " | y: " + str(y), fill="#00BFFF", tag="ln")

def Point(x, y):
    cnv.create_rectangle(x, y, x + 1, y + 1, fill="#80CBC4", outline="#004D40")
def Point_(x, y, color):
    cnv.create_rectangle(x, y, x + 1, y + 1, fill=color, outline=color)

x0 = 0
y0 = 0
def PointXY(event):
    global x0
    global y0
    x0 = event.x
    y0 = event.y
    cnv.create_oval(x0-5, y0-5, x0+5, y0+5, fill="#80CBC4", outline="#004D40")
    cnv.create_text(x0, y0+12, text="0 | x: " + str(x0) + " | y: " + str(y0), fill="#00BFFF")
x0_ = 0
y0_ = 0
RedPixel = []
def PointXY_(event):
    global x0_; global y0_
    x0_ = event.x
    y0_ = event.y
    cnv.create_rectangle(x0_, y0_, x0_+1, y0_+1, fill="black", outline="black")
x1 = 0
y1 = 0
def Point_X_Y(event):
    global x1
    global y1
    x1 = event.x
    y1 = event.y
    cnv.create_oval(x1-5, y1-5, x1+5, y1+5, fill="#80CBC4", outline="#004D40")
    cnv.create_text(x1, y1+12, text="1 | x: " + str(x1) + " | y: " + str(y1), fill="#00BFFF")


def NaturalAlgorithmLine():
    global x0
    global y0
    a = 0
    if (y1 - y0 == 0) or (x1 - x0 == 0):
        a = 0
    else:
        a = (y1 - y0) / (x1 - x0)
    b = y0 - a * x0
    if abs(x1-x0)<abs(y1-y0):
        if y1 < y0:
            y = y0
            while y >= y1:
                if x0 == x1:
                    BlackPixel.append([x0, y])
                    BlackPixel.append([x0 + 1, y])
                    BlackPixel.append([x0, y + 1])
                    BlackPixel.append([x0 - 1, y])
                    BlackPixel.append([x0, y - 1])
                    Point(x0, y)
                elif y0 == y1:
                    BlackPixel.append([x0, y])
                    BlackPixel.append([x0 + 1, y])
                    BlackPixel.append([x0, y + 1])
                    BlackPixel.append([x0 - 1, y])
                    BlackPixel.append([x0, y - 1])
                    Point(x0, y)
                else:
                    BlackPixel.append([(y-b)/a, y])
                    BlackPixel.append([(y-b)/a + 1, y])
                    BlackPixel.append([(y-b)/a, y + 1])
                    BlackPixel.append([(y-b)/a - 1, y])
                    BlackPixel.append([(y-b)/a, y - 1])
                    Point((y-b)/a, y)
                y -= 1
        else:
            y = y0
            while y <= y1:
                if x0 == x1:
                    BlackPixel.append([x0, y])
                    BlackPixel.append([x0 + 1, y])
                    BlackPixel.append([x0, y + 1])
                    BlackPixel.append([x0 - 1, y])
                    BlackPixel.append([x0, y - 1])
                    Point(x0, y)
                elif y0 == y1:
                    BlackPixel.append([x0, y])
                    BlackPixel.append([x0 + 1, y])
                    BlackPixel.append([x0, y + 1])
                    BlackPixel.append([x0 - 1, y])
                    BlackPixel.append([x0, y - 1])
                    Point(x0, y)
                else:
                    BlackPixel.append([(y - b) / a, y])
                    BlackPixel.append([(y - b) / a + 1, y])
                    BlackPixel.append([(y - b) / a, y + 1])
                    BlackPixel.append([(y - b) / a - 1, y])
                    BlackPixel.append([(y - b) / a, y - 1])
                    Point((y-b)/a, y)
                y += 1
    else:
        if x1 < x0:
            x = x0
            while x >= x1:
                BlackPixel.append([x, x*a+b])
                BlackPixel.append([x + 1, x*a+b])
                BlackPixel.append([x, x*a+b + 1])
                BlackPixel.append([x - 1, x*a+b])
                BlackPixel.append([x, x*a+b - 1])
                Point(x, x*a+b)
                x -= 1
        else:
            x = x0
            while x <= x1:
                BlackPixel.append([x, x*a+b])
                BlackPixel.append([x + 1, x*a+b])
                BlackPixel.append([x, x*a+b + 1])
                BlackPixel.append([x - 1, x*a+b])
                BlackPixel.append([x, x*a+b - 1])
                Point(x, x*a+b)
                x += 1

def BresenhamAlgorithmLine():
    x = x0
    y = y0
    dx = x1 - x0
    dy = y1 - y0
    m = 0
    e = m - 1 / 2
    i = 0
    j = 0
    Point(x, y)
    print('ok')
    if dx != 0:
        # Алгоритм для 1 части круга
        if (abs(dy / dx) <= 1) and (dy / dx >= 0):
            m = dy / dx
            while i <= dx:
                if e >= 0:
                    y = y + 1
                    e = e + abs(m) - 1
                else:
                    e = e + abs(m)
                x = x + 1
                BlackPixel.append([x, y])
                BlackPixel.append([x + 1, y])
                BlackPixel.append([x, y + 1])
                BlackPixel.append([x - 1, y])
                BlackPixel.append([x, y - 1])
                Point(x, y)
                i = i + 1

        # Алгоритм для 4 части круга
        if (abs(dy / dx) <= 1) and (dy / dx <= 0):
            m = dy / dx
            while i >= dx:
                if e < 0:
                    y = y + 1
                    e = e - abs(m) + 1
                else:
                    e = e - abs(m)
                x = x - 1
                BlackPixel.append([x, y])
                BlackPixel.append([x + 1, y])
                BlackPixel.append([x, y + 1])
                BlackPixel.append([x - 1, y])
                BlackPixel.append([x, y - 1])
                Point(x, y)
                i = i - 1

        # Алгоритм для 5 части круга
        if (abs(dy / dx) < 1) and (dy / dx >= 0):
            m = dy / dx
            while i >= dx:
                if e < 0:
                    y = y - 1
                    e = e - abs(m) + 1
                else:
                    e = e - abs(m)
                x = x - 1
                BlackPixel.append([x, y])
                BlackPixel.append([x + 1, y])
                BlackPixel.append([x, y + 1])
                BlackPixel.append([x - 1, y])
                BlackPixel.append([x, y - 1])
                Point(x, y)
                i = i - 1

        # Алгоритм для 8 части круга
        if (abs(dy / dx) <= 1) and (dy / dx <= 0):
            m = dy / dx
            while i <= dx:
                if e >= 0:
                    y = y - 1
                    e = e + abs(m) - 1
                else:
                    e = e + abs(m)
                x = x + 1
                BlackPixel.append([x, y])
                BlackPixel.append([x + 1, y])
                BlackPixel.append([x, y + 1])
                BlackPixel.append([x - 1, y])
                BlackPixel.append([x, y - 1])
                Point(x, y)
                i = i + 1

    if dy != 0:
        # Алгоритм для 2 части круга
        if (abs(dx / dy) <= 1) and (dx / dy >= 0):
            m = dx / dy
            while j <= dy:
                if e >= 0:  # Меняется в зависимости от оси Y отражения по
                    x = x + 1  # Для положительной Оси Y
                    e = e + abs(m) - 1
                else:
                    e = e + abs(m)
                y = y + 1
                BlackPixel.append([x, y])
                BlackPixel.append([x + 1, y])
                BlackPixel.append([x, y + 1])
                BlackPixel.append([x - 1, y])
                BlackPixel.append([x, y - 1])
                Point(x, y)
                j = j + 1

        # Алгоритм для 3 части круга
        if (abs(dx / dy) <= 1) and (dx / dy <= 0):
            m = dx / dy
            while j <= dy:
                if e >= 0:
                    x = x - 1
                    e = e + abs(m) - 1
                else:
                    e = e + abs(m)
                y = y + 1
                BlackPixel.append([x, y])
                BlackPixel.append([x + 1, y])
                BlackPixel.append([x, y + 1])
                BlackPixel.append([x - 1, y])
                BlackPixel.append([x, y - 1])
                Point(x, y)
                j = j + 1

        # Алгоритм для 6 части круга
        if (abs(dx / dy) <= 1) and (dx / dy >= 0):
            m = dx / dy
            while j >= dy:
                if e < 0:  # Меняется в зависимости от оси Y отражения по
                    x = x - 1  # Для положительной Оси Y
                    e = e - abs(m) + 1
                else:
                    e = e - abs(m)
                y = y - 1
                BlackPixel.append([x, y])
                BlackPixel.append([x + 1, y])
                BlackPixel.append([x, y + 1])
                BlackPixel.append([x - 1, y])
                BlackPixel.append([x, y - 1])
                Point(x, y)
                j = j - 1

        # Алгоритм для 7 части круга
        if (abs(dx / dy) < 1) and (dx / dy <= 0):
            m = dx / dy
            while j >= dy:
                if e < 0:
                    x = x + 1
                    e = e - abs(m) + 1
                else:
                    e = e - abs(m)
                y = y - 1
                BlackPixel.append([x, y])
                BlackPixel.append([x + 1, y])
                BlackPixel.append([x, y + 1])
                BlackPixel.append([x - 1, y])
                BlackPixel.append([x, y - 1])
                Point(x, y)
                j = j - 1

def NaturalAlgorithmCircle():
    X = abs(x1 - x0)
    Y = abs(y1 - y0)
    R = math.sqrt(pow(X, 2) + pow(Y, 2))
    x = x0 - R
    while x < x0 + R:
        Point(x, y0 + math.sqrt(pow(R, 2) - pow(abs(x - x0), 2)))
        Point(x, y0 - math.sqrt(pow(R, 2) - pow(abs(x - x0), 2)))
        x += 1

def Recursive_NaturalAlgorithm(pixel):
    global RedPixel
    if (pixel not in RedPixel) and (pixel not in BlackPixel):
        RedPixel.append(pixel)
        Point_(pixel[0], pixel[1], 'red')
        step1 = [pixel[0] + 1, pixel[1]]
        step2 = [pixel[0], pixel[1] + 1]
        step3 = [pixel[0] - 1, pixel[1]]
        step4 = [pixel[0], pixel[1] - 1]
        if (step1 not in RedPixel) and (step1 not in BlackPixel):
            Recursive_NaturalAlgorithm(step1)
        if (step2 not in RedPixel) and (step2 not in BlackPixel):
            Recursive_NaturalAlgorithm(step2)
        if (step3 not in RedPixel) and (step3 not in BlackPixel):
            Recursive_NaturalAlgorithm(step3)
        if (step4 not in RedPixel) and (step4 not in BlackPixel):
            Recursive_NaturalAlgorithm(step4)
def RecursiveAlgorithmSeed():
    try:
        Recursive_NaturalAlgorithm([x0_, y0_])
    except RecursionError as err:
        showerror(title="!!!Ошибка!!!", message="Превышено количество пикселей закраски!!! (более 1000 пикселей)")

pattern = [['black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'white', 'white', 'white'],
           ['black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'white', 'white', 'white'],
           ['black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'white', 'white', 'white'],

           ['black', 'black', 'black',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white',      'black', 'black', 'black',      'white', 'white', 'white'],
           ['black', 'black', 'black',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white',      'black', 'black', 'black',      'white', 'white', 'white'],
           ['black', 'black', 'black',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white',      'black', 'black', 'black',      'white', 'white', 'white'],

           ['black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'white', 'white', 'white'],
           ['black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'white', 'white', 'white'],
           ['black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'white', 'white', 'white'],

           ['black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white',      'black', 'black', 'black',      'white', 'white', 'white'],
           ['black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white',      'black', 'black', 'black',      'white', 'white', 'white'],
           ['black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white',      'black', 'black', 'black',      'white', 'white', 'white'],

           ['black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'white', 'white', 'white'],
           ['black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'white', 'white', 'white'],
           ['black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'white', 'white', 'white'],

           ['black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white'],
           ['black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white'],
           ['black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white',      'white', 'white', 'white'],

           ['black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black'],
           ['black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black'],
           ['black', 'black', 'black',      'white', 'white', 'white',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black',      'black', 'black', 'black']]
def AlgorithmBarkBeetle(pixel):
    global RedPixel
    print(BlackPixel)
    stack_data = []
    stack_data.append(pixel)
    while len(stack_data)!=0:
        pixel = stack_data.pop()
        print(pixel)
        if (pixel not in RedPixel) and (pixel not in BlackPixel):
            RedPixel.append(pixel)
            color = pattern[pixel[0]%21][pixel[1]%18]
            Point_(pixel[0], pixel[1], color)

            step1 = [pixel[0] + 1, pixel[1]]
            step2 = [pixel[0], pixel[1] + 1]
            step3 = [pixel[0] - 1, pixel[1]]
            step4 = [pixel[0], pixel[1] - 1]
            if (step1 not in RedPixel) and (step1 not in BlackPixel):
                stack_data.append(step1)
            if (step2 not in RedPixel) and (step2 not in BlackPixel):
                stack_data.append(step2)
            if (step3 not in RedPixel) and (step3 not in BlackPixel):
                stack_data.append(step3)
            if (step4 not in RedPixel) and (step4 not in BlackPixel):
                stack_data.append(step4)

def MonitorProgram(event):
    if logic_NaturalAlgorithmLine:
        NaturalAlgorithmLine()
    elif logic_BresenhamAlgorithmLine:
        BresenhamAlgorithmLine()
    elif logic_NaturalAlgorithmCircle:
        NaturalAlgorithmCircle()
    elif logic_RecursiveAlgorithmSeed:
        RecursiveAlgorithmSeed()
    elif logic_AlgorithmBarkBeetle:
        AlgorithmBarkBeetle([x0_, y0_])

def PicterExp():
    global x0; global y0
    global x1; global y1
    x0 = 50; y0 = 50
    x1 = 80; y1 = 50
    BresenhamAlgorithmLine()
    x0 = 50; y0 = 80
    x1 = 80; y1 = 80
    NaturalAlgorithmLine()
    x0 = 50; y0 = 50
    x1 = 50; y1 = 80
    BresenhamAlgorithmLine()
    x0 = 80; y0 = 50
    x1 = 80; y1 = 80
    NaturalAlgorithmLine()
    x0 = 300; y0 = 300
    x1 = 330; y1 = 330
    NaturalAlgorithmCircle()
    Recursive_NaturalAlgorithm([65,65])

    x0 = 100; y0 = 100
    x1 = 200; y1 = 100
    BresenhamAlgorithmLine()
    x0 = 100; y0 = 200
    x1 = 200; y1 = 200
    NaturalAlgorithmLine()
    x0 = 100; y0 = 100
    x1 = 100; y1 = 200
    BresenhamAlgorithmLine()
    x0 = 200; y0 = 100
    x1 = 200; y1 = 200
    NaturalAlgorithmLine()
    AlgorithmBarkBeetle([120,120])
    global BlackPixel
    global RedPixel
    BlackPixel = []
    RedPixel = []
main_menu.add_command(label="Picter", command=PicterExp)

root.bind("<Up>", PointXY_)
root.bind("<Left>", PointXY)
root.bind("<B1-Motion>", Сursor)
root.bind("<B2-Motion>", DrawDrawing)
root.bind("<B3-Motion>", ClearСursor)
root.bind("<Right>", Point_X_Y)
root.bind("<Return>", MonitorProgram)
root.bind("<Delete>", ClearScreen)

root.config(menu=main_menu)
root.mainloop()