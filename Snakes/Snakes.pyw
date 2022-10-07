#Snakes

import pygame as p,random as r,time as t,tkinter as tk,tkinter.messagebox

p.mixer.init()
p.font.init()

p.mixer.music.load("title%d.mp3"%(r.randint(1,2)))
p.mixer.music.play()

#Window
def band():
    exit()
    
def rules():
    u=tk.Tk()
    u.title("Rules")
    u.iconbitmap('icon.ico')
    f1=open("rules.txt",'r')
    d=f1.read()
    f1.close()
    ll=tk.Label(u,text=d,font=('Showcard Gothic',15)).pack()
    u.mainloop()
    
w=tk.Tk()

def rs():
    f=open("h.txt",'r')
    sc=f.read()
    f.close()
    return int(sc)

def dis_score(a):
    wi=tk.Tk()

    ss=rs()

    wi.geometry("300x200")
    wi.title("Scorecard")
    wi.iconbitmap('icon.ico')
    
    if(a==1):
        tkinter.messagebox.showinfo(title="Game Over",message="Well Played")

        l1=tk.Label(wi,text="Your Score = %d"%(score),font=('Showcard Gothic',15))
        l1.pack()
        
    l2=tk.Label(wi,text="High Score = %d"%(ss),font=('Showcard Gothic',15))
    l2.pack()

    wi.mainloop()

def display():
    dis_score(0)
    
def play():
    w.destroy() 

#Win
    
pic=tk.PhotoImage(file='back.png')
pic2=tk.PhotoImage(file='pl.png')

w.geometry("900x600")
w.title("Snakes")
w.configure(bg="#FFFFFF")
w.iconbitmap('icon.ico')

l=tk.Label(w,image=pic)
l1=tk.Label(l,text="Snakes - Retro Version",bg="#FFFFFF",font=('Mexcellent',44))

b=tk.Button(l,fg="#385B5F",bg="#00C8DE",highlightcolor="#41E2F4",activebackground="#01E2FB",text="Play",font=('Showcard Gothic',20,'bold'),command=play)
b2=tk.Button(l,fg="#385B5F",bg="#00C8DE",highlightcolor="#41E2F4",activebackground="#01E2FB",text="High Score",font=('Showcard Gothic',20,'bold'),command=display)
b3=tk.Button(l,fg="#385B5F",bg="#00C8DE",highlightcolor="#41E2F4",activebackground="#01E2FB",text="Rules",font=('Showcard Gothic',20,'bold'),command=rules)
b4=tk.Button(l,fg="#385B5F",bg="#00C8DE",highlightcolor="#41E2F4",activebackground="#01E2FB",text="Quit",font=('Showcard Gothic',20,'bold'),command=band)
             
l.place(x=0,y=0)
l1.place(x=10,y=10)
b.place(x=350,y=240)
b2.place(x=300,y=310)
b3.place(x=345,y=380)
b4.place(x=350,y=450)

w.mainloop()

#Game window
def plot(w,c,sl,si):
    for x,y in s_lst:
        p.draw.rect(w,c,[x,y,si,si])
        
s_lst=[]

screen_w=900
screen_h=600

win=p.display.set_mode((screen_w,screen_h))    #window

img=p.image.load("a.png")

#Initial pos of snake

s_x=r.randint(20,800)
s_y=r.randint(20,500)
s_size=20
s_len=1

i_v=3
v_x=0
v_y=0

f_x=r.randint(s_size,screen_w-s_size)  #s-snake f-food v-velocity
f_y=r.randint(s_size,screen_h-s_size) 
f_size=15

g_x=r.randint(s_size,screen_w-s_size)  #golden s-snake f-food v-velocity
g_y=r.randint(s_size,screen_h-s_size) 
g_size=10

score=0

fps=120

fo=p.font.SysFont(None,20)
fo2=p.font.SysFont(None,50)

def text(t,c,x,y):
    sc_text=fo.render(t,True,c)
    win.blit(sc_text,[x,y])
    

#Colours

white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
black=(0,0,0)

p.display.set_caption("Snakes")
p.display.update()

exit_game=False
game_over=False

clock=p.time.Clock()

ss=rs()

#Game loop
    
while not exit_game:

    if game_over:
        p.mixer.music.load("over.mp3")
        p.mixer.music.play()
        t.sleep(2)
        win.fill(white)
        text("Game Over",red,100,100)
        p.display.update()
        t.sleep(1)
        break

    else:    
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

                if i.key==p.K_RETURN:   #pause
                    k=True

                    while k:
                        for j in p.event.get():
                            if j.type==p.KEYDOWN:
                                if j.key==p.K_SPACE:
                                    k=False    

                if i.key==p.K_z:    #cheat mode on
                    score+=10

                if i.key==p.K_w:
                    i_v+=1

                if i.key==p.K_s:
                    i_v-=1

        s_x+=v_x
        s_y+=v_y     #velocities

        if(s_x>screen_w-20+1 or s_x<-1 or s_y<-1 or s_y>screen_h-20+1):  #boundary
            v_x=v_y=0
            game_over=True
            
        if(abs(s_x-f_x)<f_size and abs(s_y-f_y)<f_size):    #sensitivity
            score+=10
            f_x=r.randint(s_size,screen_w-s_size)  #s-snake f-food v-velocity
            f_y=r.randint(s_size,screen_h-s_size)
            s_len+=4

        if(abs(s_x-g_x)<g_size+2 and abs(s_y-g_y)<g_size+2):    #sensitivity
            score+=20
            g_x=r.randint(s_size,screen_w-s_size)  #s-snake f-food v-velocity
            g_y=r.randint(s_size,screen_h-s_size)
            s_len+=4    
           
        win.fill(white)
        win.blit(img,(0,0))
        text("Score = "+ str(score),blue,5,5) #text screen function

        p.draw.rect(win,red,[f_x,f_y,f_size,f_size])    #food

        if(score%50==0 and score!=0):
             p.draw.rect(win,yellow,[g_x,g_y,g_size,g_size])    #golden food
             
        plot(win,black,s_lst,s_size)
        
        head=[]
        head.append(s_x)
        head.append(s_y)
        s_lst.append(head)

        if(len(s_lst)>s_len):   #cutting head length
            del s_lst[0]

        if(head in s_lst[:-1]):     #collison
            game_over=True    
            
    p.display.update()
        
    clock.tick(fps) #setting fps 

if(score>ss):
    f=open("h.txt",'w')
    f.write(str(score))
    f.close()

#High Score window
p.mixer.music.load("game.mp3")
p.mixer.music.play()

dis_score(1)

p.quit()
