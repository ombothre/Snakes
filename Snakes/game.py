import pygame as p

win=p.display.set_mode((1200,500))

exit_game=False

while not exit_game:
    
    for i in p.event.get():

        print(i)

        if i.type==p.QUIT:
            exit_game=True

        if i.type==p.KEYDOWN:
            if i.key==p.K_RIGHT:
                print("HI")

p.quit()
