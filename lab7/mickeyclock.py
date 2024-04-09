import pygame 
import datetime 
 
pygame.init() 
screen = pygame.display.set_mode((500, 400)) 
running = True 
 
clock = pygame.time.Clock() 
main_clock = pygame.image.load("\\Users\\aliya\\OneDrive\\Рабочий стол\\mickeyclock.jpeg") 
minute_hand = pygame.image.load(("\\Users\\aliya\\OneDrive\\Рабочий стол\\minutes-2.png")) 
second_hand = pygame.image.load(("\\Users\\aliya\\OneDrive\\Рабочий стол\\seconds-2.png")) 
main_clock = pygame.transform.scale(main_clock, (500, 400)) 
minute_hand = pygame.transform.scale(minute_hand, (150, 190)) 
second_hand = pygame.transform.scale(second_hand, (180, 250)) 
 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
 
    screen.fill((255, 255, 255)) 
    current_time = datetime.datetime.now() 
 
    minute_angle = current_time.minute * 6 * -1 
    second_angle = current_time.second * 6 * -1 
 
    rotated_minute_hand = pygame.transform.rotate(minute_hand, minute_angle) 
    rotated_second_hand = pygame.transform.rotate(second_hand, second_angle) 
 
    screen.blit(main_clock, main_clock.get_rect(center=screen.get_rect().center)) 
    screen.blit(rotated_minute_hand, rotated_minute_hand.get_rect(center=screen.get_rect().center)) 
    screen.blit(rotated_second_hand, rotated_second_hand.get_rect(center=screen.get_rect().center)) 
    pygame.display.flip() 
    clock.tick(50) 
 
pygame.quit()