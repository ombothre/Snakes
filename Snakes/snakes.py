#Snakes

import pygame as p,random as r,time as t,tkinter as tk,tkinter.messagebox

p.mixer.init()

p.mixer.music.load("vector.mp3")
p.mixer.music.play(loops=2)

#Window
w=tk.Tk()

def play():
    w.destroy()

pic=tk.PhotoImage(file='images.png')

w.geometry("700x300")
w.title("Snakes")
w.configure(bg="#FFFFFF")
w.iconbitmap('images.png')

l1=tk.Label(w,text="Snakes - Retro Version",bg="#FFFFFF",font=('Mexcellent',44))
l2=tk.Label(w,image=pic)

b=tk.Button(w,text="Play",command=play)

l1.pack()
l2.pack()
b.pack()

w.mainloop()

#Game window
def rs():
    f=open("h.txt",'r')
    sc=f.read()
    f.close()
    return int(sc)

screen_w=900
screen_h=600

win=p.display.set_mode((screen_w,screen_h))    #window

#Initial pos of snake

s_x=r.randint(20,800)
s_y=r.randint(20,500)
s_size=20

i_v=4
v_x=0
v_y=0

f_x=r.randint(s_size,screen_w-s_size)  #s-snake f-food v-velocity
f_y=r.randint(s_size,screen_h-s_size) 
f_size=15

score=0

fps=60

#Colours

white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)

p.display.set_caption("Snakes")
p.display.update()

exit_game=False
game_over=False

clock=p.time.Clock()

ss=rs()

#Game loop

while not exit_game:
    for i in p.event.get():
        #handle updates here

        if i.type==p.QUIT:
            exit_game=True

        #Checking for key press

        if i.type==p.KEYDOWN:

            #Event handling

            if i.key==p.K_RIGHT:
                v_x=i_v
                v_y=0

            if i.key==p.K_LEFT:
                v_x=-i_v
                v_y=0

            if i.key==p.K_UP:
                v_y=-i_v
                v_x=0

            if i.key==p.K_DOWN:
                v_y=i_v
                v_x=0

    s_x+=v_x
    s_y+=v_y     #velocities

    if(s_x>screen_w-s_size+1 or s_x<-1 or s_y<-1 or s_y>screen_h-s_size+1):
        v_x=v_y=0
        t.sleep(2)
        print("Game Over")
        exit_game=True
        
    if(abs(s_x-f_x)<f_size and abs(s_y-f_y)<f_size):    #sensitivity
        score+=1
        print("Score = ",score*10)
        f_x=r.randint(s_size,screen_w-s_size)  #s-snake f-food v-velocity
        f_y=r.randint(s_size,screen_h-s_size)
        
    win.fill(white)
    p.draw.rect(win,red,[f_x,f_y,f_size,f_size])
    p.draw.rect(win,black,[s_x,s_y,s_size,s_size])
    p.display.update()
    
    clock.tick(fps) #setting fps 
    
p.quit()

if(score>ss):
    f=open("h.txt",'w')
    f.write(str(score))
    f.close()

#High Score window
wi=tk.Tk()

ss=rs()

wi.geometry("200x200")
wi.title("Scorecard")

tkinter.messagebox.showinfo(title="Game Over",message="Well Played")

l1=tk.Label(wi,text="Your Score = %d"%(score))
l2=tk.Label(wi,text="High Score = %d"%(ss))

l1.pack()
l2.pack()

wi.mainloop()
