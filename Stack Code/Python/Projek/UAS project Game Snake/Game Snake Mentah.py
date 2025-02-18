import pygame

'''Akan terdapat berapa tahap garis besar dari proses pembuatan Game Snake'''

# Membuat init
pygame.init()
# ini adalah vairabel
Run = True
# Next adalah Object
# Ukuran
panjang = 10 ; lebar = 10
# Speed
speed = 2
# Posisi
x = 250
y = 250
# ukuran display
# Kelupaan membuat Display surface object
window_lebar = 500 ; window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))
while Run:
# User Input atau DataBase
    pygame.time.delay(20)
    for event in pygame.event.get():
        print('Ruun')
        if event.type == pygame.QUIT:
            Run = False
# Keyboard Impressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and x < window_lebar - lebar:
        x += speed
    elif keys[pygame.K_LEFT] and x > 0:
        x -= speed
    elif keys[pygame.K_UP] and y > 0:
        y -= speed
    elif keys[pygame.K_DOWN] and y < window_panjang - panjang:
        y += speed
# Update aset
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,120,0),(x,y,panjang,lebar))
# Renderieng
    pygame.display.update()
pygame.quit()