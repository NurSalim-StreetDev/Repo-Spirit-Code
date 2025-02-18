import sys
import random
import pygame
from pygame.locals import FULLSCREEN, QUIT, KEYDOWN, K_ESCAPE

# Inisialisasi pygame
pygame.init()

# Membuat layar dengan ukuran sesuai dengan resolusi layar penuh
screen = pygame.display.set_mode((0, 0), FULLSCREEN)

# Mendapatkan ukuran layar dan menyimpannya dalam variabel
s_width, s_height = screen.get_size()

# Membuat clock untuk mengontrol frame rate
clock = pygame.time.Clock()
FPS = 90

# Membuat grup sprite untuk manajemen objek game
sprite_group = pygame.sprite.Group()

# Kelas Background untuk sprite salju
class Background(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        # Membuat permukaan gambar dengan ukuran x, y
        self.image = pygame.Surface([x, y])
        # Mengisi permukaan dengan warna putih untuk representasi salju
        self.image.fill('White')
        self.rect = self.image.get_rect()
        
    def update(self):
        # Memindahkan sprite salju ke bawah dan ke kanan setiap frame
        self.rect.y += 1
        self.rect.x += 1
        # Jika sprite salju keluar dari batas bawah layar, atur kembali ke posisi acak di atas
        if self.rect.y > s_height:
            self.rect.y = random.randrange(-10, 0)
            self.rect.x = random.randrange(0, s_width)

# Kelas CosmicDust untuk sprite debu kosmik
class CosmicDust(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        # Membuat partikel dengan ukuran acak
        self.image = pygame.Surface([x, y])
        # Mengisi partikel dengan warna yang lebih halus, seperti abu-abu terang
        self.image.fill((200, 200, 200))  # Warna abu-abu terang
        self.rect = self.image.get_rect()
        # Menambahkan gerakan acak untuk debu kosmik
        self.speed_x = random.uniform(-0.5, 0.5)
        self.speed_y = random.uniform(0.5, 1.5)
        
    def update(self):
        # Gerakan partikel debu lebih lambat dan acak
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        # Jika partikel keluar dari layar, reset ke posisi acak di atas layar
        if self.rect.y > s_height:
            self.rect.y = random.randrange(-10, 0)
            self.rect.x = random.randrange(0, s_width)

# Kelas utama game
class Game:

    def __init__(self):
        # Memulai game dengan menjalankan metode run_game
        self.run_game()

    def create_background(self):
        # Membuat 100 sprite salju dengan ukuran acak
        for i in range(100):
            x = random.randint(1, 5)  # Ukuran acak antara 1 dan 5 piksel
            Background_Image = Background(x, x)  # Membuat sprite baru
            # Menempatkan sprite salju di lokasi acak di layar
            Background_Image.rect.x = random.randrange(0, s_width)
            Background_Image.rect.y = random.randrange(0, s_height)
            # Menambahkan sprite ke grup sprite
            sprite_group.add(Background_Image)
    
    def create_cosmic_dust(self):
        # Membuat 50 partikel debu kosmik dengan ukuran acak
        for i in range(50):
            x = random.randint(1, 3)  # Ukuran debu yang lebih kecil antara 1 dan 3 piksel
            dust = CosmicDust(x, x)  # Membuat partikel debu baru
            # Menempatkan partikel di lokasi acak di layar
            dust.rect.x = random.randrange(0, s_width)
            dust.rect.y = random.randrange(0, s_height)
            # Menambahkan partikel debu ke grup sprite
            sprite_group.add(dust)

    def run_update(self):
        # Menggambar dan memperbarui semua sprite di layar
        sprite_group.draw(screen)
        sprite_group.update()

    def run_game(self):
        # Membuat latar belakang salju
        self.create_background()
        # Membuat debu kosmik
        self.create_cosmic_dust()
        while True:
            # Mengisi layar dengan warna hitam setiap frame
            screen.fill('Black')
            # Memperbarui semua sprite
            self.run_update()
            # Memeriksa event (seperti penekanan tombol)
            for event in pygame.event.get():
                if event.type == QUIT:
                    # Keluar dari game jika event QUIT terdeteksi
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        # Keluar dari game jika tombol ESC ditekan
                        pygame.quit()
                        sys.exit()

            # Memperbarui layar dengan gambar yang baru
            pygame.display.update()
            # Mengatur kecepatan game sesuai FPS yang ditentukan
            clock.tick(FPS)

# Fungsi main untuk memulai game
def main():
    game = Game()

# Memastikan script dijalankan sebagai program utama
if __name__ == '__main__':
    main()
