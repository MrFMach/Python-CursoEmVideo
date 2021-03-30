# playing MP3

import pygame
from time import sleep

pygame.init()

pygame.mixer.music.load('Python-CursoEmVideo/media/Powerful.mp3')
pygame.mixer.music.play(start=12)      # play music (music start point in seconds)
print("Playing Music #1")
sleep(8)
pygame.mixer.music.stop()
pygame.mixer.music.unload()

pygame.mixer.music.load('Python-CursoEmVideo/media/Trusted.mp3')
pygame.mixer.music.play()
print("Playing Music #2")
sleep(7)
pygame.mixer.music.stop()
pygame.mixer.music.unload()

print("End")