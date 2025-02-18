import pygame
from permainan import Kotak

class Ular():

    def __init__(self,arena,start,arah_x=1,arah_y=0,warna=(0,0,0)):
        self.body = []
        self.belokan = {}
        self.arah_x = arah_x
        self.arena = arena
        self.arah_y = arah_y
        self.kepala = Kotak(arena,start,arah_x,arah_y,warna,nama="Kotak")
        self.body.append(self.kepala)
    

    def tambah_kotak(self,posisi,nama):
        badan_baru = Kotak(self.arena,posisi,nama=nama)
        self.body.append(badan_baru)

    def move(self):
        print (self.body)
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_RIGHT]:
                self.arah_x = 1
                self.arah_y = 0
                self.belokan[self.kepala.posisi] = [self.arah_x,self.arah_y]
            elif keys[pygame.K_LEFT]:
                self.arah_x = -1
                self.arah_y = 0
                self.belokan[self.kepala.posisi] = [self.arah_x,self.arah_y]
            elif keys[pygame.K_UP]:
                self.arah_y = -1
                self.arah_x = 0
                self.belokan[self.kepala.posisi] = [self.arah_x,self.arah_y]
            elif keys[pygame.K_DOWN]:
                self.arah_x = 0
                self.arah_y = 1
                self.belokan[self.kepala.posisi] = [self.arah_x,self.arah_y]

        for posisi in self.belokan:
            print(f'Posisi{posisi} Arah{self.belokan[posisi]} \n  ')

        for kotak in self.body:
            posisi_kotak = kotak.get_posisi()
            if posisi_kotak in self.belokan:
                arah = self.belokan[posisi_kotak]
                arah_x = [0]
                arah_y = [1]
                kotak.move(arah_x,arah_y)
    def draw(self):
        for anggota_badan in self.body:
            anggota_badan.draw()