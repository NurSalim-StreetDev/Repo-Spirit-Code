import sys
import random
import pygame
from pygame.locals import FULLSCREEN, QUIT, KEYDOWN, K_ESCAPE

# Inisialisasi pygame
pygame.init()

Palyer_Ship = 'playship.png'

# Membuat layar dengan ukuran sesuai dengan resolusi layar penuh
screen = pygame.display.set_mode((0, 0), FULLSCREEN)

# Mendapatkan ukuran layar dan menyimpannya dalam variabel
s_width, s_height = screen.get_size()

# Membuat clock untuk mengontrol frame rate
clock = pygame.time.Clock()
FPS = 90

# Membuat dua grup sprite untuk manajemen objek game
Background_Group = pygame.sprite.Group()
sprite_group = pygame.sprite.Group()

# Kelas Background untuk sprite latar belakang
class Background(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        # Membuat permukaan gambar dengan ukuran x, y
        self.image = pygame.Surface([x, y])
        # Mengisi permukaan dengan warna putih
        self.image.fill('White')
        # Menetapkan warna hitam sebagai transparan (tidak ditampilkan)
        self.image.set_colorkey('Black')
        # Mendapatkan persegi panjang (rect) untuk gambar
        self.rect = self.image.get_rect()
        
    def update(self):
        # Memindahkan sprite ke bawah dan ke kanan setiap frame
        self.rect.y += 1
        self.rect.x += 1
        # Jika sprite keluar dari batas bawah layar, atur kembali ke posisi acak di atas
        if self.rect.y > s_height:
            self.rect.y = random.randrange(-10, 0)
            self.rect.x = random.randrange(-400, s_width)
class Player(pygame.sprite.sprite):
    def __init__(self.img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.image.set_colorkey('black')
    
    def update(self):
        mouse = pygame.mouse.get_pos()
        self.rect.x = mouse[0]
        self.rect.y = mouse[1]


# Kelas utama game
class Game:

    def __init__(self):
        # Memulai game dengan menjalankan metode run_game
        self.run_game() 

    def create_background(self):
        # Membuat 20 sprite latar belakang dengan ukuran acak
        for i in range(40):
            x = random.randint(1, 5)
            Background_Image = Background(x, x)
            # Menempatkan sprite di lokasi acak di layar
            Background_Image.rect.x = random.randrange(0, s_width)
            Background_Image.rect.y = random.randrange(0, s_height)
            # Menambahkan sprite ke grup
            Background_Group.add(Background_Image)
            sprite_group.add(Background_Image)
    
    def run_update(self):
        # Menggambar dan memperbarui semua sprite di layar
        sprite_group.draw(screen)
        sprite_group.update()

    def run_game(self):
        # Membuat latar belakang
        self.create_background()
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
