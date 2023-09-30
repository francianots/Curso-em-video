'''Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.'''
print('----------------------------------------------------------')
print('            T O C A D O R    M P 3')
print('----------------------------------------------------------')
import pygame
pygame.init()
pygame.mixer.music.load('des21.mp3')
pygame.mixer.music.play()
pygame.event.wait()