import pygame
import os


pygame.init()


screen = pygame.display.set_mode((1500, 750))
pygame.display.set_caption("musics")
fon = pygame.image.load("\\Users\\aliya\\OneDrive\\Рабочий стол\\lab7\\fon.jpg")

music_dir = "\\Users\\aliya\\OneDrive\\Рабочий стол\\lab7"


music_files = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]


musics = 0
pygame.mixer.init()

def play_music():
    pygame.mixer.music.load(os.path.join(music_dir, music_files[musics]))
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def play_next_track():
    global musics
    musics = (musics + 1) % len(music_files)
    play_music()

def play_previous_track():
    global musics
    musics = (musics - 1) % len(music_files)
    play_music()


running = True
while running:
    screen.blit(fon, (0,0))
    pygame.display.update() 

    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:  # Play
                play_music()
            elif event.key == pygame.K_DOWN:  # Stop
                stop_music()
            elif event.key == pygame.K_RIGHT:  # Next
                play_next_track()
            elif event.key == pygame.K_LEFT:  # Previous
                play_previous_track()
        elif event.type == pygame.QUIT:
            running = False
   
pygame.quit()
