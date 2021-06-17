from tkinter import *
import tkinter as tk

from PIL import ImageTk, Image

# import back

#global declarations


def aux():
	pass

root = Tk()  # main root

colorFondo = "#CDCDCD"
colorLetra = "#FFF"

width = root.winfo_screenwidth()
height = root.winfo_screenheight()-100

root.title("Visualizador")
root.geometry(f'{width}x{height}')
root.configure(background='#CDCDCD')

canvas = tk.Canvas(root, bg='#CDCDCD', width=width, height=height+100)
canvas.place(x=0, y=0)

canvas.create_line(0, 4, width, 4, width=5)
canvas.create_line(0, height+34, width, height+34, width=5)

canvas.create_line(4, 0, 4, height+100, width=5)
canvas.create_line(width-4, 0, width-4, height+100, width=5)
canvas.create_line(860, 0, 860, height+100, width=5)

def helper():
    # ----helper----
    x = 10
    for x in range(x, width-20, 50):
        for y in range(40, height-2, 30):
            t1 = f'({x},{y})'
            t2 = str(x)
            t3 = str(y)
            canvas.create_oval(x, y, x+20, y+20, fill='blue')
            canvas.create_text(x+5, y-10, text=t3)
    #  ----helper----


def display():
    cam_box = Frame(canvas, bg='black', width=800, height=540)
    cam_box.place(x=30, y=30)

    source = Image.open("pic01.png")
    source_resized = source.resize((800, 540))
    render = ImageTk.PhotoImage(source_resized)
    img = Label(image=render)
    img.image = render
    img.place(x=30, y=30)

    Button(canvas, text='Iniciar Tiempo Real', width=20, height=1, bg='grey').place(x=40, y=590)

    Button(canvas, text='Detener Tiempo Real', width=20, height=1, bg='grey').place(x=250, y=590)

    Button(canvas, text='Pantalla completa', width=20, height=1, bg="grey").place(x=450, y=590)

    Button(canvas, text='Guardar en', width=20,
           height=1, bg="grey").place(x=650, y=590)

    Button(canvas, text='Iniciar grabacion', width=20,
           height=1, bg="grey").place(x=40, y=650)

    Button(canvas, text='Detener grabacion', width=20,
           height=1, bg="grey").place(x=250, y=650)

    brigthness = Scale(canvas, label='BRILLO (Rango de 0 a 100)', bg='#CDCDCD', from_=0,
    to=100, orient=tk.HORIZONTAL, length=350, showvalue=1, resolution=1).place(x=910, y=40)


    contrast = Scale(canvas, label='CONTRASTE (Rango de -100 a 100', bg='#CDCDCD', from_=-100,
                     to=100, orient=tk.HORIZONTAL, length=350, showvalue=1, resolution=1).place(x=910, y=90)


    saturation = Scale(canvas, label='SATURACION (Rango de -100 a 100', bg='#CDCDCD', from_=-100, to=100,
                       orient=tk.HORIZONTAL, length=350, showvalue=1, resolution=1).place(x=910, y=140)

    sharpness = Scale(canvas, label='NITIDEZ (Rango de -100 a 100)', bg='#CDCDCD', from_=-100, to=100,
                      orient=tk.HORIZONTAL, length=350, showvalue=1, resolution=1).place(x=910, y=190)


    resolution = Scale(canvas, label='RESOLUCION (Rango de 1 a 60)', bg='#CDCDCD', from_=1, to=60,
                       orient=tk.HORIZONTAL, length=350, showvalue=1, resolution=1).place(x=910, y=240)

    rotation = Scale(canvas, label='ROTACION', bg='#CDCDCD', from_=0, to=270, orient=tk.HORIZONTAL,
    length=350, showvalue=1, resolution=90).place(x=910, y=290)                       

    shutter_speed = Scale(canvas, label='VELOCIDAD OBTURACION (Rango de 0 a 1000)', bg='#CDCDCD', from_=0,
    to=1000, orient=tk.HORIZONTAL, length=350, showvalue=1, resolution=1).place(x=910, y=340)

    timelapse = Scale(canvas, label='TIMELAPSE (Rango de 0 a 60 minutos)', bg='#CDCDCD', from_=0, to=1944,
                      orient=tk.HORIZONTAL, length=350, showvalue=1, resolution=1).place(x=910, y=390)
    
    #----iso label----
    Label(canvas, text='ISO : Seleccione un valor', width=49).place(x=910, y=570)
    values = [100,200,320,400,500,640,800] #----restricted iso values----
    pos = 910  
    for value in values:
        temp = Button(canvas, text=value, width=6, height=1, bg='grey')
        temp.place(x=pos, y=590)
        pos = pos + 50

# helper()
display()

mainloop()
