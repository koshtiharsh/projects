import random
import os
from tkinter import Variable
import pygame
pygame.init()

# for Music 
pygame.mixer.init() 

# colours 
 
white=(255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# creating window
  
gameWindow=pygame.display.set_mode((900, 600))
pygame.display.set_caption('Snake game by Harsh Koshti')

# some Common Variable

clock = pygame.time.Clock()

# for getting image on the background

#img = pygame.image.load('snake.jpg') 
#img = pygame.transform.scale(img, (900, 600)).convert_alpha()

# function for TEXT on SCREEN

font = pygame.font.SysFont(None, 55)
def t_s(text, colour, x, y):
    screen_text=font.render(text, True, colour)
    gameWindow.blit(screen_text, [x, y])

# fun for welcome interface

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(red)
       # gameWindow.blit(img, (0, 0))    # for getting image on the background
        t_s('PLEASE ENTER SPACE BAR TO PLAY', white, 150, 280)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game= True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        pygame.display.update()
        clock.tick(60)     

                

################ MAIN FUNTION OF GAME  ################ 
                    
def game():
    # GAME SPECIFIC VARIABLE 
    exit_game= False
    game_over = False
    s_x=55
    s_y=45
    vx=0
    vy=0
    s_size= 20
    fps=45
    score=0
    foodx=random.randint(0, 900/2)
    foody=random.randint(0, 600/2) 

    # FOR INCREMENT OF SNAKE
    snk_list = []
    snk_length = 1

    # if file not exits 
    if (not os.path.exists('highscore.txt')):
        with open('highscore.txt', 'w') as f :
            f.write(str("0"))
#    for read the hiscore 
    with open('highscore.txt', 'r') as  f:
        highscore= f.read()

# MAIN LOOP OF GAME
    while not exit_game:

# IF GAME OVER THEN LAST CONTENT
        if game_over:
            with open('highscore.txt', 'w') as f:
                f.write(str(highscore))
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    exit_game= True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN: # RETURN MEANS THE ENTER KEY 
                        welcome()

            gameWindow.fill(white)
          #  gameWindow.blit(img, (0, 0)) # for getting image on the background
            t_s('game over please press ENTER!!!!!!!!!!!!!', red, 70, 250)
#*************************************************************************************************************************************************             
        else:    
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    exit_game= True
                if event.type== pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        vx=5
                        vy=0 
                    if event.key==pygame.K_LEFT:
                        vx=-5                                                     # FOR KEYS FROM KEYBOARD
                        vy=0 
                    if event.key==pygame.K_UP:
                        vy=-5
                        vx=0                      
                    if event.key==pygame.K_DOWN:
                        vy=5
                        vx=0 
        #  CHEAT CODE                
                    if event.key== pygame.K_q:
                        score+=10
                        snk_length +=5  
# FOR MOVEMEMNT OF GAME                        
            s_x = s_x+ vx 
            s_y = s_y+ vy
# **************************************************************************************************************************************************
# FOOD OF SNAKE            
            if abs(foodx-s_x)<10 and abs(foody - s_y)<10:
                score +=10
                # pygame.mixer.music.load('beep.wav')
                # pygame.mixer.music.play()  
                foodx=random.randint(100, 900/2)
                foody=random.randint(100, 600/2) 
                snk_length +=5 
                if score>int(highscore):
                    highscore = score    
                    
            gameWindow.fill(white)
           # gameWindow.blit(img, (0, 0))      # for getting image on the background
# PRINTING OF HIGHSCORE AND SCORE ON THE SCREEN             
            t_s('score is' + str(score) +'    HIGHSCORE '+ str(highscore) , red, 5, 5 )
            pygame.draw.rect(gameWindow, red, [foodx, foody, s_size, s_size])
        # *************************************************************************    
            head = []
            head.append(s_x)
            head.append(s_y)
            snk_list.append(head)                                     # FOR INCREMENT OF SNAKE
            if len(snk_list)>snk_length:
                del snk_list[0]
            for s_x, s_y in snk_list :
                pygame.draw.rect(gameWindow, black, [s_x, s_y, s_size, s_size])  

        #    *************************************************************************       
           
        # FOR GAME OVER            
            # if head in snk_list[:-1]:
            #     game_over= True    
            if s_x < 0 or s_x> 900 or s_y < 0 or s_y> 600:
                game_over=True             
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()   