import pygame
import os
import random
import sys

class PacManGame:
    def __init__(self):
        pygame.init()
        
        # Ekran ayarları
        self.genislik = 850
        self.yukseklik = int(self.genislik * 1.12)
        self.ekran = pygame.display.set_mode((self.genislik, self.yukseklik))
        pygame.display.set_caption("Pac-Man")
        
        # Renkler
        self.MAVI = (0, 0, 255)
        self.SIYAH = (0, 0, 0)
        self.BEYAZ = (255, 255, 255)
        
        # Oyun nesneleri
        self.saatli_cihaz = pygame.time.Clock()
        self.FPS = 60
        
        # Font
        try:
            self.font = pygame.font.Font('Assets/AlphaSmart3000.ttf', 74)
        except:
            self.font = pygame.font.Font(None, 74)
        
        # Oyun durumu değişkenleri
        self.solaGit = False
        self.sagaGit = False
        self.yukariGit = False 
        self.asagiGit = False
        
        # Harita ve duvarlar
        self.pacman_map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        
        # Sprites grupları
        self.duvarlar = pygame.sprite.Group()
        self.hayaletler = pygame.sprite.Group()
        self.yemler = pygame.sprite.Group()

        # Haritayı oluştur
        self.haritayi_olustur()
        
        # Oyuncu ve hayaletler
        self.oyuncu = self.oyuncu_olustur()
        self.hayaletleri_olustur()
        self.yemleri_olustur()
        
    def haritayi_olustur(self):
        tile_boyutu = 27
        for y, row in enumerate(self.pacman_map):
            for x, tile in enumerate(row):
                if tile == 1:
                    duvar = Duvar(x * tile_boyutu, y * tile_boyutu, tile_boyutu, tile_boyutu)
                    self.duvarlar.add(duvar)
    
    def oyuncu_olustur(self):
        return Karakter('pacman.png', 100, 430, 2)
    
    def hayaletleri_olustur(self):
        hayalet_konumlari = [(430, 430), (410, 430), (390, 430), (370, 430)]
        hayalet_resimleri = ['hayalet1.png', 'hayalet2.png', 'hayalet3.png', 'hayalet4.png']
        
        for konum, resim in zip(hayalet_konumlari, hayalet_resimleri):
            hayalet = Hayalet(resim, konum[0], konum[1], 1)
            self.hayaletler.add(hayalet)
    
    def yemleri_olustur(self):
        tile_boyutu = 27
        for y, row in enumerate(self.pacman_map):
            for x, tile in enumerate(row):
                if tile == 0:
                    yem = Yem(x * tile_boyutu + tile_boyutu // 2 - 5, y * tile_boyutu + tile_boyutu // 2 - 5)
                    self.yemler.add(yem)
            

    def oyun_dongusu(self):
        calisma = True
        while calisma:
            self.saatli_cihaz.tick(self.FPS)
            self.ekran.fill(self.SIYAH)
            
            # Olayları işle
            calisma = self.olaylari_isle()
            
            # Hareket
            self.oyuncu_hareketini_isle()
            
            # Çizim
            self.cizim_isle()
            
            # Çarpışma kontrolleri
            self.carpisma_kontrolleri()
            
            pygame.display.update()
        
        pygame.quit()
        sys.exit()
    
    def olaylari_isle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            # Tuş basma olayları
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_a, pygame.K_LEFT]:
                    self.solaGit = True
                elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                    self.sagaGit = True
                elif event.key in [pygame.K_w, pygame.K_UP]:
                    self.yukariGit = True
                elif event.key in [pygame.K_s, pygame.K_DOWN]:
                    self.asagiGit = True
                elif event.key == pygame.K_ESCAPE:
                    return False
            
            # Tuş bırakma olayları
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_a, pygame.K_LEFT]:
                    self.solaGit = False
                elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                    self.sagaGit = False
                elif event.key in [pygame.K_w, pygame.K_UP]:
                    self.yukariGit = False
                elif event.key in [pygame.K_s, pygame.K_DOWN]:
                    self.asagiGit = False
        
        return True
    
    def oyuncu_hareketini_isle(self):
        # Oyuncunun hareketini kontrol et
        self.oyuncu.hareket(
            self.solaGit, 
            self.sagaGit, 
            self.yukariGit, 
            self.asagiGit, 
            self.duvarlar
        )
    
    def cizim_isle(self):
        # Tüm nesneleri çiz
        self.oyuncu.draw(self.ekran)
        self.duvarlar.draw(self.ekran)
        self.yemler.draw(self.ekran)
        
        # Hayaletleri çiz ve hareket ettir
        for hayalet in self.hayaletler:
            hayalet.rastgele_hareket(self.duvarlar)
            hayalet.draw(self.ekran)
    
    def carpisma_kontrolleri(self):
        # Hayaletlerle çarpışma kontrolü
        if self.oyuncu_hayalet_carpisma_kontrolu():
            self.oyuncu_hayalet_carpisma_tepkisi()
        
        # Duvara çarpma kontrolü
        if not self.oyuncu.hareket_edilebilir:
            self.oyuncu_duvar_carpisma_tepkisi()

        if self.oyuncu_yem_carpisma_kontrolu():
            self.oyuncu_yem_carpisma_tepkisi()

    def oyuncu_hayalet_carpisma_kontrolu(self):
        return pygame.sprite.spritecollideany(self.oyuncu, self.hayaletler)
    
    def oyuncu_hayalet_carpisma_tepkisi(self):
        # Çarpışma mesajını ekrana yaz
        mesaj1 = self.font.render('Yandın!', True, self.BEYAZ)
        self.ekran.blit(mesaj1, (300, 155))
        pygame.display.update()
        pygame.time.delay(1000)  # 1 saniye bekle
        
        # Oyuncuyu başlangıç konumuna sıfırla
        self.oyuncu.rect.center = (100, 430)
        self.solaGit = self.sagaGit = self.yukariGit = self.asagiGit = False
    
    def oyuncu_duvar_carpisma_tepkisi(self):
        # Duvara çarpma mesajını ekrana yaz
        mesaj2 = self.font.render('Duvara Dikkat!', True, self.BEYAZ)
        self.ekran.blit(mesaj2, (200, 150))
        pygame.display.update()
        pygame.time.delay(1000)  # 1 saniye bekle
        
        # Oyuncuyu başlangıç konumuna sıfırla
        self.solaGit = self.sagaGit = self.yukariGit = self.asagiGit = False
    def oyuncu_yem_carpisma_kontrolu(self):
        return pygame.sprite.spritecollideany(self.oyuncu, self.yemler)
    
    def oyuncu_yem_carpisma_tepkisi(self):
        yem = self.oyuncu_yem_carpisma_kontrolu()
        yem.kill()

        # Yem yeme sesi
        pygame.mixer.music.load('Assets/yem2.mp3')
        pygame.mixer.music.play()

class Karakter(pygame.sprite.Sprite):
    def __init__(self, oyuncuTürü, x, y, hiz):
        super().__init__()
        # Resmi yükle ve ölçeklendir
        try:
            img = pygame.image.load(os.path.join("Assets", oyuncuTürü))
            self.orijinal_img = pygame.transform.scale(img, (30, 30))
        except:
            # Eğer resim yüklenemezse, basit bir kare çiz
            self.orijinal_img = pygame.Surface((30, 30))
            self.orijinal_img.fill((255, 255, 0))  # Sarı renk
        self.image = self.orijinal_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hiz = hiz
        self.yonverme = 0
        self.hareket_edilebilir = True
    
    def hareket(self, solaGit, sagaGit, yukariGit, asagiGit, duvarlar):
        hx = hy = 0
        
        # Hareket yönlerini belirle
        if solaGit:
            hx -= self.hiz
            self.yonverme = 180
        if sagaGit:
            hx += self.hiz
            self.yonverme = 0
        if yukariGit:
            hy -= self.hiz
            self.yonverme = 90
        if asagiGit:
            hy += self.hiz
            self.yonverme = 270
        
        # Çarpışma kontrolü
        hx, hy, self.hareket_edilebilir = carpisma_kontrol(self, duvarlar, hx, hy)
        
        # Hareketi uygula
        self.rect.x += hx
        self.rect.y += hy
        
        # Ekran sınırları içinde tut
        self.rect.x = max(0, min(self.rect.x, 900 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 990 - self.rect.height))
        
        # Resmi döndür
        self.image = pygame.transform.rotate(self.orijinal_img, self.yonverme)
    
    def draw(self, ekran):
        ekran.blit(self.image, self.rect)

class Hayalet(Karakter):
    def __init__(self, oyuncuTürü, x, y, hiz):
        super().__init__(oyuncuTürü, x, y, hiz)
        self.hareket_yonu = random.choice(['sol', 'sag', 'yukari', 'asagi'])
        self.yon_suresi = random.randint(30, 60)
        self.zamanlayici = 0
    
    def rastgele_hareket(self, duvarlar):
        # Yön değiştirme mantığı
        if self.zamanlayici >= self.yon_suresi:
            self.hareket_yonu = random.choice(['sol', 'sag', 'yukari', 'asagi'])
            self.yon_suresi = random.randint(30, 60)
            self.zamanlayici = 0
        
        # Hareket parametrelerini ayarla
        solaGit = sagaGit = yukariGit = asagiGit = False
        if self.hareket_yonu == 'sol':
            solaGit = True
        elif self.hareket_yonu == 'sag':
            sagaGit = True
        elif self.hareket_yonu == 'yukari':
            yukariGit = True
        elif self.hareket_yonu == 'asagi':
            asagiGit = True
        
        # Hareketi gerçekleştir
        self.hareket(solaGit, sagaGit, yukariGit, asagiGit, duvarlar)
        
        self.zamanlayici += 1

class Duvar(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 255))  # Mavi duvar
        self.rect = self.image.get_rect(topleft=(x, y))

class Yem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 0))  # Sarı yem
        self.rect = self.image.get_rect(topleft=(x, y))

def carpisma_kontrol(oyuncu, duvarlar, hx, hy):
    # Yatay hareket kontrolü
    oyuncu.rect.x += hx
    hareket_edilebilir = True
    for duvar in duvarlar:
        if oyuncu.rect.colliderect(duvar.rect):
            hareket_edilebilir = True
            if hx > 0:  # Sağa hareket
                oyuncu.rect.right = duvar.rect.left
            elif hx < 0:  # Sola hareket
                oyuncu.rect.left = duvar.rect.right
            hx = 0
    
    # Dikey hareket kontrolü
    oyuncu.rect.y += hy
    for duvar in duvarlar:
        if oyuncu.rect.colliderect(duvar.rect):
            hareket_edilebilir = True
            if hy > 0:  # Aşağı hareket
                oyuncu.rect.bottom = duvar.rect.top
            elif hy < 0:  # Yukarı hareket
                oyuncu.rect.top = duvar.rect.bottom
            hy = 0
    
    return hx, hy, hareket_edilebilir

def main():
    oyun = PacManGame()
    oyun.oyun_dongusu()

if __name__ == "__main__":
    main()