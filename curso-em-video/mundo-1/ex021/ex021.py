import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('Ex. 21 - Tocando um MP3/Undertale - Megalovania.mp3')
pygame.mixer.music.play()
pygame.event.wait()