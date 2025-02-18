import pygame
from permainan import Arena,Kotak,Ular

arena = Arena(500,500,20,20)
ular = Ular(arena,(10,10))
ular.tambah_kotak((9,10),nama='Tubuh 1')
ular.tambah_kotak((8,10),nama='Tubuh 2')
ular.tambah_kotak((7,10),nama='Tubuh 3') 
run = True

while run:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    ular.move()
    arena.render(5)

pygame.QUIT()