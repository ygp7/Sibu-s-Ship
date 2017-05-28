import pygame
import time
import random
from time import sleep

pygame.init() #initializes modules
              #dimensions of the screen
disp_width = 1000
disp_height = 500
white=(255,255,255)
red=(200,0,0)
blue = (0,0,255)
green =(0,255,0)
yellow = (255,255,0)
black=(0,0,0)
cyan = (0,255,255)
orange = (255, 43, 0)
purple = (255,51,255)
darkgreen = (0,153,0)

gamescreen = pygame.display.set_mode((disp_width,disp_height)) #Makes the screen
pygame.display.set_caption("Shibu's Ship") #name of screen window
pygame.display.update()  #//When we are completely done with all the actions then we will write this command for rendering

image = pygame.image.load("ship.png")
leaf = pygame.image.load("lead.png")
FPS = 30 #frame per second with which our screen is rendered

move_step = 10
block_size = move_step*2
clock = pygame.time.Clock() #for fps


def button(x,y,buttonwidth,buttonheight,inactivecolor,activecolor,action =None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+buttonwidth>cur[0]> x and y+buttonheight>cur[1]>y:
        pygame.draw.rect(gamescreen,activecolor,(x,y,buttonwidth,buttonheight))
        if click[0]==1:
            if action == "play":
                gameloop()
            if action == "controls":
                control()

            if action == "back":
                mainscreen()

            if action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gamescreen,inactivecolor,(x,y,buttonwidth,buttonheight))


#function for displaying the message on the screen
def message(msg,color,fontsize,widthratio,heightratio,fontname = "Arial"):
    font = pygame.font.SysFont("arial" ,fontsize)             #fonts for displaying text on screen
    screen_text = font.render(msg,True,color)
    gamescreen.blit(screen_text,[disp_width/widthratio,disp_height/heightratio])


def mainscreen():
    intro = True
    while intro ==True:

        gamescreen.fill((10,10,10))
        message("SIBU's SHIP",red,100,3.85,3)

        button(250,350,100,40,(0,175,0),green,"play")
        message("play",black,20,3.55,1.4)
        button(450,350,100,40,(175,175,0),yellow,"controls")
        message("controls",black,20,2.15,1.4)
        button(650,350,100,40,(175,0,0),red,"quit")
        message("quit",black,20,1.46,1.4)

        clock.tick(FPS)
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
def control():
    c = True
    while c == True:
        gamescreen.fill((0,40,0))
        message("OBJECTIVES:",(50,100,50),60,25,7)
        message("1.Help sibu  by collecting all the coins in the space.",(10,10,0),25,10,3)
        message("2.He needs to get richer in order to reach mars.",(10,10,0),25,10,2.5)

        message("CONTROLS:",(50,100,50),60,25,2)
        message("1.Use Up,Down,Left,Right arrow keys for the movement of ship.",(10,10,0),25,10,1.5)
        message("2.Do not touch the boundaries and stay away from the bullets.",(10,10,0),25,10,1.36)


        button(35,20,100,40,(175,175,0),yellow,"back")
        message("Main Menu",black,20,22,18)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    clock.tick(FPS/6)






def pause():
    pause = True
    while pause == True:
        #gamescreen.fill((250,250,0))
        message("PAUSED",(250,0,0),60,2.4,3.5)
        message(" Press 'P' to Proceed the game.",(0,0,0),30,2.9,1.9)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False

    clock.tick(FPS/6)



#main gameloop
def gameloop():
    x = True
    gameover = False
    xlead = disp_width/10
    ylead = disp_height/1.5
    xcont = 0
    ycont = 0
    move = 5
    bulletmove = 5
    bulletmove1 = 5
    bulletmove2 = 5
    bulletmove4 = 5
    bulletmove5 = 0
    shipsizex = 65
    shipsizey = 40
    bulletsizex = 50
    bulletsizey = 10
    score = 0


    coinsizex = 40
    coinsizey = 40


    randome1 = round(random.randrange(10,disp_height-10))
    randome2 = round(random.randrange(10,disp_height-10))
    randome3 = round(random.randrange(10,disp_height-10))
    randome4 = round(random.randrange(10,disp_height-10))
    randome5 = round(random.randrange(10,disp_height-10))
    randomvalue = random.randint(disp_width,1100)
#    randomvalue2 = random.randint(disp_width,1500)

    randomcoinx = round(random.randrange(0,disp_width-coinsizex-100))
    randomcoiny = round(random.randrange(0,disp_height-coinsizey-100))




#this while x loop works when x is true and contains the game
    while x:
        bulletmove+=20
        bulletmove1+=25
        bulletmove2+=19
        bulletmove4+=25
        #bulletmove5+=15




        while gameover == True:       #this loop is used after user out ho gayaa hai and now he wants to exit or continue
            gamescreen.fill((10,10,10))
            message("Game Over!!!",(200,10,10),70,3,10,"segoeprint")
            message("Score:" +str(score),darkgreen,50,2.3,2)
            button(650,350,100,40,(175,0,0),red,"quit")
            message("quit",black,20,1.46,1.4)
            button(250,350,100,40,(0,175,0),green,"play")
            message("play again",black,20,3.8,1.4)
            message("Click on play again or press 'c' to play again",white,20,2.9,1.2)
            pygame.display.update()

#for loop for event handeling after user out ho jaata hai
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    x = False
                    gameover = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        x = False
                        gameover = False
                        gameloop()
#for loop for event handeling for movement and quitting the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                x = False
                gameover = False
            #print event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    xcont =15
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    xcont = -15
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    ycont = -15
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    ycont = 15




            if event.type == pygame.KEYUP :
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    xcont = 0

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    xcont = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    ycont = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    ycont = 0


            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_l:
                    xcont= 15
                    ycont = 0

                if event.key == pygame.K_j:
                    xcont = -15
                    ycont = 0
                if event.key == pygame.K_i:
                    ycont = -15
                    xcont = 0

                if event.key == pygame.K_k:
                    ycont = 15
                    xcont = 0




        gamescreen.fill((10,10,50))
        #pygame.draw.rect(gamescreen,(255,0,0),[randomecoinx,randomecoiny,coinsize,coinsize])
        gamescreen.blit(image, (xlead,ylead))
        message("Score:" + str(score),(255,0,0),20,100,400,"comicsansms")
        #pygame.draw.rect(gamescreen,red,[randomcoinx,randomcoiny,coinsizex,coinsizey])
        gamescreen.blit(leaf,(randomcoinx,randomcoiny))
        if randomcoinx<xlead+shipsizex and randomcoinx >xlead or randomcoinx+coinsizex>xlead and randomcoinx+coinsizex<xlead+shipsizex :
            if ylead<randomcoiny+coinsizey and ylead>randomcoiny or ylead+shipsizey<randomcoiny+coinsizey and ylead+shipsizey>randomcoiny:
                randomcoinx = round(random.randrange(10,disp_width-100))
                randomcoiny = round(random.randrange(10,disp_height-100))
                score +=10


        pygame.draw.rect(gamescreen,purple,[disp_width - bulletmove,randome1,50,10])
        if bulletmove>disp_width:
             pygame.draw.rect(gamescreen,red,[disp_width - bulletmove,randome1,50,10])
             randome1 = round(random.randrange(0,disp_height))
             bulletmove=0

        pygame.draw.rect(gamescreen,yellow,[randomvalue - bulletmove1,randome2,50,10])
        if bulletmove1>disp_width+randomvalue:
             pygame.draw.rect(gamescreen,yellow,[randomvalue - bulletmove1,randome2,50,10])
             randome2 = round(random.randrange(0,disp_height))
             bulletmove1=0

        pygame.draw.rect(gamescreen,orange,[disp_width - bulletmove2,randome3,50,10])
        if bulletmove2>disp_width:
             pygame.draw.rect(gamescreen,green,[disp_width - bulletmove2,randome3,50,10])
             randome3 = round(random.randrange(0,disp_height))
             bulletmove2 = 0

        pygame.draw.rect(gamescreen,cyan,[disp_width - bulletmove4,randome4,50,10])
        if bulletmove4>disp_width:
             pygame.draw.rect(gamescreen,cyan,[disp_width - bulletmove4,randome4,50,10])
             randome4 = round(random.randrange(0,disp_height-10))
             bulletmove4 = 0

#        pygame.draw.rect(gamescreen,black,[randomvalue2 - bulletmove5,randome5,75,15])
#        if bulletmove5>disp_width+randomvalue2:
#            pygame.draw.rect(gamescreen,black,[randomvalue2-bulletmove5,randome5,75,15])
#            randome5 = round(random.randrange(10,disp_height-10))
#            bulletmove5 = 0

        if disp_width-bulletmove<xlead+shipsizex and disp_width-bulletmove>xlead or \
           disp_width-bulletmove+bulletsizex>xlead and disp_width-bulletmove+bulletsizex< xlead + shipsizex:
            if randome1>ylead and randome1<ylead + shipsizey or\
               randome1+bulletsizey>ylead and randome1<ylead:
                gameover = True

        if randomvalue-bulletmove1<xlead+shipsizex and randomvalue-bulletmove1>xlead or \
           randomvalue-bulletmove1+bulletsizex>xlead and randomvalue-bulletmove1+bulletsizex< xlead + shipsizex:
            if randome2>ylead and randome2<ylead + shipsizey or\
               randome2+bulletsizey>ylead and randome2<ylead:
                gameover = True

        if disp_width-bulletmove2<xlead+shipsizex and disp_width-bulletmove2>xlead or \
           disp_width-bulletmove2+bulletsizex>xlead and disp_width-bulletmove2+bulletsizex< xlead + shipsizex:
            if randome3>ylead and randome3<ylead + shipsizey or\
               randome3+bulletsizey>ylead and randome3<ylead:
                gameover = True

        if disp_width-bulletmove4<xlead+shipsizex and disp_width-bulletmove4>xlead or \
           disp_width-bulletmove4+bulletsizex>xlead and disp_width-bulletmove4+bulletsizex< xlead + shipsizex:
            if randome4>ylead and randome4<ylead + shipsizey or\
               randome4+bulletsizey>ylead and randome4<ylead:
                gameover = True










        pygame.display.update()

        xlead+=xcont
        ylead+=ycont
       # gameover = True
        if ylead > disp_height - shipsizey:
            ylead = 0
        if ylead < 0:
            ylead = disp_height - shipsizey
        if xlead > disp_width - shipsizex :
            xlead = 0
        if xlead < 0:
            xlead = disp_width - shipsizex

# #Modified apple colission code
#         if xlead > randomecoinx and xlead < randomecoinx + coinsize or xlead + block_size > randomecoinx and xlead + block_size < randomecoinx + coinsize:
#             if ylead > randomecoiny and ylead < randomecoiny + coinsize or ylead + block_size > randomecoiny and ylead + block_size < randomecoiny + coinsize:
#                 randomecoinx = round(random.randrange(0,disp_width-coinsize))# /10.0)*10.0
#                 randomecoiny = round(random.randrange(0,disp_height-coinsize))# /10.0)*10.0
#                 snakelength += 1
#                 score += 10




        clock.tick(FPS)

    pygame.quit()
    quit()

mainscreen()
