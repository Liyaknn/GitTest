import pygame

pygame.init()
sc_x = 800
sc_y = 700
screen = pygame.display.set_mode((sc_x,sc_y)) 
pygame.display.set_caption("ball")


ball_x= 600
ball_y = 400
ball_speed = 5


runnig = True
while runnig:

    screen.fill("White")
    
    ball = pygame.draw.circle(screen, "Red",(ball_x,ball_y), 25 )
   

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT ] and ball_x<sc_x-50:
        ball_x += ball_speed
    
    if keys[pygame.K_LEFT] and ball_x>40:
        ball_x -= ball_speed

    if keys[pygame.K_UP] and ball_y>50:
        ball_y -=ball_speed

    if keys[pygame.K_DOWN] and ball_y<sc_y-50:
        ball_y +=ball_speed 
    

    pygame.display.update()
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            runnig = False
            pygame.quit()

