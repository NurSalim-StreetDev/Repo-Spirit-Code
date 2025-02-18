import pygame

class Arena():
    
    def __init__(self,lebar_arena,panjang_arena,jumlah_X_pixel,jumlah_Y_pixel):
        pygame.init()
        self.lebar_arena    = lebar_arena
        self.panjang_arena  = panjang_arena
        self.jumlah_X_pixel = jumlah_X_pixel
        self.jumlah_Y_pixel = jumlah_Y_pixel
        self.sisi_X_pixel = self.lebar_arena // self.jumlah_X_pixel
        self.sisi_Y_pixel = self.panjang_arena // self.jumlah_Y_pixel
        self.object = []
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((self.lebar_arena,self.panjang_arena))
    
    def assign(self,object):
        self.object.append(object)

    def get_surface(self):
        return self.surface
    
    def get_jarak_baris(self):
        return self.sisi_X_pixel

    def get_jarak_kolom(self):
        return self.sisi_Y_pixel
    
    def get_jumlah_baris(self):
        return self.jumlah_X_pixel

    def get_jumlah_kolom(self):
        return self.jumlah_Y_pixel

    def draw_line(self):
        for limit_pixel in range(self.jumlah_X_pixel):
            x = self.sisi_X_pixel * limit_pixel   
            y = self.sisi_Y_pixel * limit_pixel
            pygame.draw.line(self.surface,(0,0,0),(x,0),(x,self.panjang_arena))
            pygame.draw.line(self.surface,(0,0,0),(0,y),(self.lebar_arena,y))

    def render(self,fps):
        self.surface.fill((255,255,255))
        for OB in self.object:
            OB.draw()
        self.draw_line()
        pygame.display.update()
        pygame.time.delay(50)
        self.clock.tick(fps)
