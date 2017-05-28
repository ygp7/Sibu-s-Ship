import pygame

gamescreen

def button(x,y,buttonwidth,buttonheight,inactivecolor,activecolor):
    cur = pygame.mouse.get_pos()

    if buttonwidth < cur[0] < buttonwidth+x and buttonheight < cur[1] < buttonheight + y:
        pygame.draw.rect(gamescreen,activecolor,(x,y,buttonwidth,buttonheight))
    else:
        pygame.draw.rect(gamescreen,inactivecolor,(x,y,buttonwidth,buttonheight))
