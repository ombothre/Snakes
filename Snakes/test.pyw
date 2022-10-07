import pygame as p,tkinter as tk

e=False
win=tk.Tk()

win.mainloop()

w=p.display.set_mode((900,600))

while not e:
    for i in p.event.get():

        if i.type==p.QUIT:
            e=True
p.quit()
