import pygame
from time import sleep

pygame.init()

pygame.mixer.music.load('media/Powerful.mp3')
pygame.mixer.music.play(start=12)      # play music (music start point in seconds)
sleep(8)
pygame.mixer.music.stop()
pygame.mixer.music.unload()

pygame.mixer.music.load('media/Trusted.mp3')
pygame.mixer.music.play()
sleep(7)
pygame.mixer.music.stop()
pygame.mixer.music.unload()

print("End")