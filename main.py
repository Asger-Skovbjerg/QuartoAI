from quarto import Quarto
import numpy as np
import pygame

q = Quarto()
q.init_pieces()
# print(q.pieces)
# print(q.board)
positions = []
for x in range(4):
    for y in range(4):
        positions.append((x, y))
for piece, position in zip(q.pieces, positions):
    q.place_piece(piece, position)
print(q.board)

def draw_grid(surface,matrix,size):
    """Draws a grid on surface given"""
    #TODO: for every matrix cell, check status and put either empty cell or image of given token


game_running = True
width = 800
height = 500
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Quarto - Asger & Annike")
clock = pygame.time.Clock()
surface = pygame.Surface((width,height))
surface.fill('White')


while game_running:
    for event in pygame.event.get(): #getting user input
        if event.type == pygame.QUIT: #if closing the window, quit.
            """#pygame.quit quits pygame we initalized in pygame.init()
             and pygame.display.update() will then throw a "video system not initialized" error. 
            A solution to this is importing from sys import exit and then call exit()
            However exit() will stop any code still going on, and we might still want to be able to run the AI 
            even when we have closed the window. """
            pygame.quit()
            game_running == False

    screen.blit(surface,(0,0))
    pygame.display.update()
    clock.tick(60) #while loop should not run faster than 60 times pr second


