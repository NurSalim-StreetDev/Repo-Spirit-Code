import pygame
class Kotak():
    
    def __init__(self,arena,posisi_awal,arah_x=1,arah_y=1,warna=(0,0,255),nama='Kotak'):
        self.nama = nama
        self.posisi = posisi_awal
        self.arah_x = arah_x
        self.arah_y = arah_y
        self.warna  = warna
        self.surface = arena.get_surface()
        self.lebar = arena.get_jarak_baris()
        self.tinggi = arena.get_jarak_kolom()
        self.arena = arena
        arena.assign(self)

    def get_posisi(self):
        return self.posisi

    def move (self,arah_x,arah_y):
        self.arah_x = arah_x
        self.arah_y = arah_y
        self.posisi = (self.posisi[0] + self.arah_x,self.posisi[1] + self.arah_y)
        # print (self.posisi)
        
        if self.posisi[0] == self.arena.get_jumlah_baris():
            self.posisi = (0,self.posisi[1])
        elif self.posisi[0] < 0:
            self.posisi = (self.arena.get_jumlah_baris()-1,self.posisi[1])
        if self.posisi[1] == self.arena.get_jumlah_kolom():
            self.posisi = (self.posisi[0],0)
        elif self.posisi[1] < 0:
            self.posisi = (self.posisi[0],self.arena.get_jumlah_kolom()-1)


    def draw(self):

        start_x = self.lebar * self.posisi[0]
        start_y = self.tinggi * self.posisi[1]

        pygame.draw.rect (self.surface,self.warna,(start_x,start_y,self.lebar,self.tinggi))

    def __repr__(self):
        return self.nama