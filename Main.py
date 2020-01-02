import pygame #mengimport module yang diperlukan
import random
import sys

pygame.display.init() #membuat jendela pygame

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE) #supaya fullscreen
#screen = pygame.display.set_mode((640, 480)) #pengembangan

lebar_layar = pygame.display.get_surface().get_width() #mendapatkan ukuran layar untuk mengatur ukuran assets
tinggi_layar = pygame.display.get_surface().get_height() #mendapatkan ukuran layar untuk mengatur ukuran assets
ukuran_player = int(tinggi_layar/100*36)
ukuran_player_pilih = int(tinggi_layar/100*70)

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', int(tinggi_layar/16))


#sprite player================================================================================================================================================================================
viking_1 = [["Karakter/Viking 1/Diam/0.png", "Karakter/Viking 1/Diam/1.png", "Karakter/Viking 1/Diam/2.png", "Karakter/Viking 1/Diam/3.png", "Karakter/Viking 1/Diam/4.png", "Karakter/Viking 1/Diam/5.png", "Karakter/Viking 1/Diam/6.png", "Karakter/Viking 1/Diam/7.png", "Karakter/Viking 1/Diam/8.png", "Karakter/Viking 1/Diam/9.png"],
            
            ["Karakter/Viking 1/Jalan/0.png", "Karakter/Viking 1/Jalan/1.png", "Karakter/Viking 1/Jalan/2.png", "Karakter/Viking 1/Jalan/3.png", "Karakter/Viking 1/Jalan/4.png", "Karakter/Viking 1/Jalan/5.png", "Karakter/Viking 1/Jalan/6.png", "Karakter/Viking 1/Jalan/7.png", "Karakter/Viking 1/Jalan/8.png", "Karakter/Viking 1/Jalan/9.png"],
            
            ["Karakter/Viking 1/Lompat/0.png", "Karakter/Viking 1/Lompat/1.png", "Karakter/Viking 1/Lompat/2.png", "Karakter/Viking 1/Lompat/3.png", "Karakter/Viking 1/Lompat/4.png", "Karakter/Viking 1/Lompat/5.png", "Karakter/Viking 1/Lompat/6.png", "Karakter/Viking 1/Lompat/7.png", "Karakter/Viking 1/Lompat/8.png", "Karakter/Viking 1/Lompat/9.png"],
            
            ["Karakter/Viking 1/Mati/0.png", "Karakter/Viking 1/Mati/1.png", "Karakter/Viking 1/Mati/2.png", "Karakter/Viking 1/Mati/3.png", "Karakter/Viking 1/Mati/4.png", "Karakter/Viking 1/Mati/5.png", "Karakter/Viking 1/Mati/6.png", "Karakter/Viking 1/Mati/7.png", "Karakter/Viking 1/Mati/8.png", "Karakter/Viking 1/Mati/9.png"],
            
            ["Karakter/Viking 1/Serang/0.png", "Karakter/Viking 1/Serang/1.png", "Karakter/Viking 1/Serang/2.png", "Karakter/Viking 1/Serang/3.png", "Karakter/Viking 1/Serang/4.png", "Karakter/Viking 1/Serang/5.png", "Karakter/Viking 1/Serang/6.png", "Karakter/Viking 1/Serang/7.png", "Karakter/Viking 1/Serang/8.png", "Karakter/Viking 1/Serang/9.png"]]

#=====================================================================================================================================================================

viking_2 = [["Karakter/Viking 2/Diam/0.png", "Karakter/Viking 2/Diam/1.png", "Karakter/Viking 2/Diam/2.png", "Karakter/Viking 2/Diam/3.png", "Karakter/Viking 2/Diam/4.png", "Karakter/Viking 2/Diam/5.png", "Karakter/Viking 2/Diam/6.png", "Karakter/Viking 2/Diam/7.png", "Karakter/Viking 2/Diam/8.png", "Karakter/Viking 2/Diam/9.png"],
            
        ["Karakter/Viking 2/Jalan/0.png", "Karakter/Viking 2/Jalan/1.png", "Karakter/Viking 2/Jalan/2.png", "Karakter/Viking 2/Jalan/3.png", "Karakter/Viking 2/Jalan/4.png", "Karakter/Viking 2/Jalan/5.png", "Karakter/Viking 2/Jalan/6.png", "Karakter/Viking 2/Jalan/7.png", "Karakter/Viking 2/Jalan/8.png", "Karakter/Viking 2/Jalan/9.png"],
        
        ["Karakter/Viking 2/Lompat/0.png", "Karakter/Viking 2/Lompat/1.png", "Karakter/Viking 2/Lompat/2.png", "Karakter/Viking 2/Lompat/3.png", "Karakter/Viking 2/Lompat/4.png", "Karakter/Viking 2/Lompat/5.png", "Karakter/Viking 2/Lompat/6.png", "Karakter/Viking 2/Lompat/7.png", "Karakter/Viking 2/Lompat/8.png", "Karakter/Viking 2/Lompat/9.png"],
        
        ["Karakter/Viking 2/Mati/0.png", "Karakter/Viking 2/Mati/1.png", "Karakter/Viking 2/Mati/2.png", "Karakter/Viking 2/Mati/3.png", "Karakter/Viking 2/Mati/4.png", "Karakter/Viking 2/Mati/5.png", "Karakter/Viking 2/Mati/6.png", "Karakter/Viking 2/Mati/7.png", "Karakter/Viking 2/Mati/8.png", "Karakter/Viking 2/Mati/9.png"],
        
        ["Karakter/Viking 2/Serang/0.png", "Karakter/Viking 2/Serang/1.png", "Karakter/Viking 2/Serang/2.png", "Karakter/Viking 2/Serang/3.png", "Karakter/Viking 2/Serang/4.png", "Karakter/Viking 2/Serang/5.png", "Karakter/Viking 2/Serang/6.png", "Karakter/Viking 2/Serang/7.png", "Karakter/Viking 2/Serang/8.png", "Karakter/Viking 2/Serang/9.png"]]

#=======================================================================================================================================================================

viking_3 = [["Karakter/Viking 3/Diam/0.png", "Karakter/Viking 3/Diam/1.png", "Karakter/Viking 3/Diam/2.png", "Karakter/Viking 3/Diam/3.png", "Karakter/Viking 3/Diam/4.png", "Karakter/Viking 3/Diam/5.png", "Karakter/Viking 3/Diam/6.png", "Karakter/Viking 3/Diam/7.png", "Karakter/Viking 3/Diam/8.png", "Karakter/Viking 3/Diam/9.png"],
            
        ["Karakter/Viking 3/Jalan/0.png", "Karakter/Viking 3/Jalan/1.png", "Karakter/Viking 3/Jalan/2.png", "Karakter/Viking 3/Jalan/3.png", "Karakter/Viking 3/Jalan/4.png", "Karakter/Viking 3/Jalan/5.png", "Karakter/Viking 3/Jalan/6.png", "Karakter/Viking 3/Jalan/7.png", "Karakter/Viking 3/Jalan/8.png", "Karakter/Viking 3/Jalan/9.png"],
        
        ["Karakter/Viking 3/Lompat/0.png", "Karakter/Viking 3/Lompat/1.png", "Karakter/Viking 3/Lompat/2.png", "Karakter/Viking 3/Lompat/3.png", "Karakter/Viking 3/Lompat/4.png", "Karakter/Viking 3/Lompat/5.png", "Karakter/Viking 3/Lompat/6.png", "Karakter/Viking 3/Lompat/7.png", "Karakter/Viking 3/Lompat/8.png", "Karakter/Viking 3/Lompat/9.png"],
        
        ["Karakter/Viking 3/Mati/0.png", "Karakter/Viking 3/Mati/1.png", "Karakter/Viking 3/Mati/2.png", "Karakter/Viking 3/Mati/3.png", "Karakter/Viking 3/Mati/4.png", "Karakter/Viking 3/Mati/5.png", "Karakter/Viking 3/Mati/6.png", "Karakter/Viking 3/Mati/7.png", "Karakter/Viking 3/Mati/8.png", "Karakter/Viking 3/Mati/9.png"],
        
        ["Karakter/Viking 3/Serang/0.png", "Karakter/Viking 3/Serang/1.png", "Karakter/Viking 3/Serang/2.png", "Karakter/Viking 3/Serang/3.png", "Karakter/Viking 3/Serang/4.png", "Karakter/Viking 3/Serang/5.png", "Karakter/Viking 3/Serang/6.png", "Karakter/Viking 3/Serang/7.png", "Karakter/Viking 3/Serang/8.png", "Karakter/Viking 3/Serang/9.png"]]




#init untuk game loop=================================================================================================================================================================================
background = pygame.transform.scale(pygame.image.load("background/game_background_3.1.png"), (lebar_layar, tinggi_layar)).convert()
tanah = pygame.transform.scale(pygame.image.load("background/Ground.png"), (lebar_layar, int(tinggi_layar/50))).convert_alpha()
game_over= pygame.transform.scale(pygame.image.load("background/game_over.png"), (lebar_layar, tinggi_layar))
game_over.fill((255, 255, 255, 10), None, pygame.BLEND_RGBA_MULT)

tanah1=[0, int(tinggi_layar/4)-5] #pos dari semua gambar ground
tanah2=[0, int(tinggi_layar/4)*2-5]
tanah3=[0, int(tinggi_layar/4)*3-5]
tanah4=[0, int(tinggi_layar/4)*4-5]

acak_posisi=random.randint(10, 100)

#=================================================================================================================================================================
#memilih karater
karakter_diam = None #variabel ini kosong, tapi akan di isi dengan scrip untuk panggil animasi supaya karakternya bisa berubah. scrip di tulis dengan string tapi akan di ubah dengan eval()
karakter_jalan = None
karakter_lompat = None
karakter_mati = None
karakter_serang = None

karakter = 1
panah= pygame.transform.scale(pygame.transform.flip(pygame.image.load("karakter/panah.png"), True, False), (ukuran_player, ukuran_player)).convert_alpha()
if karakter == 1:
    karakter_diam = "viking_1[0][frame]"
    karakter_jalan = "viking_1[1][frame]"
    karakter_lompat = "viking_1[2][frame]"
    karakter_mati = "viking_1[3][frame_mati]"
    karakter_serang = "viking_1[4][frame]"
if karakter == 2:
    karakter_diam = "viking_2[0][frame]"
    karakter_jalan = "viking_2[1][frame]"
    karakter_lompat = "viking_2[2][frame]"
    karakter_mati = "viking_2[3][frame_mati]"
    karakter_serang = "viking_2[4][frame]"
if karakter == 3:
    karakter_diam = "viking_3[0][frame]"
    karakter_jalan = "viking_3[1][frame]"
    karakter_lompat = "viking_3[2][frame]"
    karakter_mati = "viking_3[3][frame_mati]"
    karakter_serang = "viking_3[4][frame]"
    
#memilih musuh
musuh_1_diam = None
musuh_1_jalan = None
musuh_1_lompat = None
musuh_1_mati = None
musuh_1_serang = None

musuh_1 = random.randint(1, 3)
if musuh_1 == 1:
    musuh_1_diam = "viking_1[0][musuh_1frame]"
    musuh_1_jalan = "viking_1[1][musuh_1frame]"
    musuh_1_lompat = "viking_1[2][musuh_1frame]"
    musuh_1_mati = "viking_1[3][musuh_1frame]"
    musuh_1_serang = "viking_1[4][musuh_1frame]"
if musuh_1 == 2:
    musuh_1_diam = "viking_2[0][musuh_1frame]"
    musuh_1_jalan = "viking_2[1][musuh_1frame]"
    musuh_1_lompat = "viking_2[2][musuh_1frame]"
    musuh_1_mati = "viking_2[3][musuh_1frame]"
    musuh_1_serang = "viking_2[4][musuh_1frame]"
if musuh_1 == 3:
    musuh_1_diam = "viking_3[0][musuh_1frame]"
    musuh_1_jalan = "viking_3[1][musuh_1frame]"
    musuh_1_lompat = "viking_3[2][musuh_1frame]"
    musuh_1_mati = "viking_3[3][musuh_1frame]"
    musuh_1_serang = "viking_3[4][musuh_1frame]"
    
    
musuh_2_diam = None
musuh_2_jalan = None
musuh_2_lompat = None
musuh_2_mati = None
musuh_2_serang = None

musuh_2 = random.randint(1, 3)
if musuh_2 == 1:
    musuh_2_diam = "viking_1[0][musuh_2frame]"
    musuh_2_jalan = "viking_1[1][musuh_2frame]"
    musuh_2_lompat = "viking_1[2][musuh_2frame]"
    musuh_2_mati = "viking_1[3][musuh_2frame]"
    musuh_2_serang = "viking_1[4][musuh_2frame]"
if musuh_2 == 2:
    musuh_2_diam = "viking_2[0][musuh_2frame]"
    musuh_2_jalan = "viking_2[1][musuh_2frame]"
    musuh_2_lompat = "viking_2[2][musuh_2frame]"
    musuh_2_mati = "viking_2[3][musuh_2frame]"
    musuh_2_serang = "viking_2[4][musuh_2frame]"
if musuh_2 == 3:
    musuh_2_diam = "viking_3[0][musuh_2frame]"
    musuh_2_jalan = "viking_3[1][musuh_2frame]"
    musuh_2_lompat = "viking_3[2][musuh_2frame]"
    musuh_2_mati = "viking_3[3][musuh_2frame]"
    musuh_2_serang = "viking_3[4][musuh_2frame]"
    
    
musuh_3_diam = None
musuh_3_jalan = None
musuh_3_lompat = None
musuh_3_mati = None
musuh_3_serang = None

musuh_3 = random.randint(1, 3)
if musuh_3 == 1:
    musuh_3_diam = "viking_1[0][musuh_3frame]"
    musuh_3_jalan = "viking_1[1][musuh_3frame]"
    musuh_3_lompat = "viking_1[2][musuh_3frame]"
    musuh_3_mati = "viking_1[3][musuh_3frame]"
    musuh_3_serang = "viking_1[4][musuh_3frame]"
if musuh_3 == 2:
    musuh_3_diam = "viking_2[0][musuh_3frame]"
    musuh_3_jalan = "viking_2[1][musuh_3frame]"
    musuh_3_lompat = "viking_2[2][musuh_3frame]"
    musuh_3_mati = "viking_2[3][musuh_3frame]"
    musuh_3_serang = "viking_2[4][musuh_3frame]"
if musuh_3 == 3:
    musuh_3_diam = "viking_3[0][musuh_3frame]"
    musuh_3_jalan = "viking_3[1][musuh_3frame]"
    musuh_3_lompat = "viking_3[2][musuh_3frame]"
    musuh_3_mati = "viking_3[3][musuh_3frame]"
    musuh_3_serang = "viking_3[4][musuh_3frame]"
    

musuh_4_diam = None
musuh_4_jalan = None
musuh_4_lompat = None
musuh_4_mati = None
musuh_4_serang = None

musuh_4 = random.randint(1, 3)
if musuh_4 == 1:
    musuh_4_diam = "viking_1[0][musuh_4frame]"
    musuh_4_jalan = "viking_1[1][musuh_4frame]"
    musuh_4_lompat = "viking_1[2][musuh_4frame]"
    musuh_4_mati = "viking_1[3][musuh_4frame]"
    musuh_4_serang = "viking_1[4][musuh_4frame]"
if musuh_4 == 2:
    musuh_4_diam = "viking_2[0][musuh_4frame]"
    musuh_4_jalan = "viking_2[1][musuh_4frame]"
    musuh_4_lompat = "viking_2[2][musuh_4frame]"
    musuh_4_mati = "viking_2[3][musuh_4frame]"
    musuh_4_serang = "viking_2[4][musuh_4frame]"
if musuh_4 == 3:
    musuh_4_diam = "viking_3[0][musuh_4frame]"
    musuh_4_jalan = "viking_3[1][musuh_4frame]"
    musuh_4_lompat = "viking_3[2][musuh_4frame]"
    musuh_4_mati = "viking_3[3][musuh_4frame]"
    musuh_4_serang = "viking_3[4][musuh_4frame]"
#==============================================================================================================================================================================================

#init variabel untuk player
playerpos=[random.randint(0, lebar_layar), random.randint(1, 4)] #init posisi player. posisi player saat game di mulai adalah acak
frame=0
arah="kanan"
momentum="diam"
pertarungan="diam"
step= int(lebar_layar/100*3) #agar kecepatannya sama di ukuran layar yang berbeda. tiap 1 milidetik player bisa berjalan sejauh 1,5% dari panjang layar. formatnya harus interger karena kita gak bisa bergerak kurang dari 1 pixel(float)
nyawa=100
score=0
frame_mati=0

#init variabel untuk musuh
musuh_1pos=[random.randint(0, lebar_layar), random.randint(1, 4)] #init posisi player. posisi player saat game di mulai adalah acak
musuh_1frame=0
musuh_1arah="kanan"
musuh_1pertarungan="diam"
musuh_1step= int(lebar_layar/100*3)
musuh_1hitung=random.randint(1, 30)
musuh_1nyawa = 100
musuh_1jeda_sebelum_serang=0 #jeda waktu dari pertama kali player dan musuh berbenturan sampai musuh memutuskan untuk menyerang atau tidak(biar gak op)
musuh_1jeda_sebelum_respawn=0

musuh_2pos=[random.randint(0, lebar_layar), random.randint(1, 4)] #init posisi player. posisi player saat game di mulai adalah acak
musuh_2frame=0
musuh_2arah="kanan"
musuh_2pertarungan="diam"
musuh_2step= int(lebar_layar/100*3)
musuh_2hitung=random.randint(1, 30)
musuh_2nyawa = 100
musuh_2jeda_sebelum_serang=0 #jeda waktu dari pertama kali player dan musuh berbenturan sampai musuh memutuskan untuk menyerang atau tidak(biar gak op)
musuh_2jeda_sebelum_respawn=0

musuh_3pos=[random.randint(0, lebar_layar), random.randint(1, 4)] #init posisi player. posisi player saat game di mulai adalah acak
musuh_3frame=0
musuh_3arah="kanan"
musuh_3pertarungan="diam"
musuh_3step= int(lebar_layar/100*3)
musuh_3hitung=random.randint(1, 30)
musuh_3nyawa = 100
musuh_3jeda_sebelum_serang=0 #jeda waktu dari pertama kali player dan musuh berbenturan sampai musuh memutuskan untuk menyerang atau tidak(biar gak op)
musuh_3jeda_sebelum_respawn=0

musuh_4pos=[random.randint(0, lebar_layar), random.randint(1, 4)] #init posisi player. posisi player saat game di mulai adalah acak
musuh_4frame=0
musuh_4arah="kanan"
musuh_4pertarungan="diam"
musuh_4step= int(lebar_layar/100*3)
musuh_4hitung=random.randint(1, 30)
musuh_4nyawa = 100
musuh_4jeda_sebelum_serang=0 #jeda waktu dari pertama kali player dan musuh berbenturan sampai musuh memutuskan untuk menyerang atau tidak(biar gak op)
musuh_4jeda_sebelum_respawn=0


mencetak_score=0
#=====================================================================================================================================================================================

#init untuk menu loop=================================================================================================================================================================
background_menu=pygame.transform.scale(pygame.image.load("background/menu.png"), (lebar_layar, tinggi_layar)).convert()
my_file = open("score.txt", "r")
highscore = int(my_file.read())
my_file.close()



#init tombol
kiri=pygame.transform.scale(pygame.image.load("tombol/shadedDark24.png"), (int((tinggi_layar/100*25)/2), int((tinggi_layar/100*25)/2))).convert_alpha()
kanan=pygame.transform.scale(pygame.image.load("tombol/shadedDark25.png"), (int((tinggi_layar/100*25)/2), int((tinggi_layar/100*25)/2))).convert_alpha()
play_button=pygame.transform.scale(pygame.image.load("tombol/shadedDark42.png"), (int(lebar_layar/100*25), int(tinggi_layar/100*10))).convert_alpha()
attack=pygame.transform.scale(pygame.image.load("tombol/shadedDark48.png"), (int((tinggi_layar/100*25)/2), int((tinggi_layar/100*25)/2))).convert_alpha()


#############################
menu=True
play=False
pilih_karakter=False
game_over_screen=False
WTW=True
#############################

while (WTW==True):
    
    if menu==True:
        playpos=(int(lebar_layar/2)-int(lebar_layar/100*25/2), int(tinggi_layar-(tinggi_layar/3.5)))
        play_rect=play_button.get_rect()
        play_rect.top=playpos[1]
        play_rect.left=playpos[0]
        
        
        screen.blit(background_menu, (0, 0))
        screen.blit(play_button, playpos)
        
        mencetak_highscore = myfont.render(str(highscore), False, (1, 1, 1))
        text = myfont.render("Highscore kamu:", False, (1, 1, 1))
        screen.blit(text, (int(lebar_layar/20), 0))
        screen.blit(mencetak_highscore,(int(lebar_layar/2),0))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                WTW=False
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN: #apa yang terjadi jika kita klik area layar
                mouse_pos= pygame.mouse.get_pos() #mengambil koordinat mouse saat klik terjadi
                if play_rect.collidepoint(mouse_pos): #mengecek apakah posisi klik mouse ada di dalam objek rect tombol
                    menu=False
                    play=False
                    pilih_karakter=True
                    
    
    if pilih_karakter==True:
        if karakter==4:
            karakter=1
        if karakter==0:
            karakter=3
        
        if karakter == 1:
            karakter_diam = "viking_1[0][frame]"
            karakter_jalan = "viking_1[1][frame]"
            karakter_lompat = "viking_1[2][frame]"
            karakter_mati = "viking_1[3][frame_mati]"
            karakter_serang = "viking_1[4][frame]"
        if karakter == 2:
            karakter_diam = "viking_2[0][frame]"
            karakter_jalan = "viking_2[1][frame]"
            karakter_lompat = "viking_2[2][frame]"
            karakter_mati = "viking_2[3][frame_mati]"
            karakter_serang = "viking_2[4][frame]"
        if karakter == 3:
            karakter_diam = "viking_3[0][frame]"
            karakter_jalan = "viking_3[1][frame]"
            karakter_lompat = "viking_3[2][frame]"
            karakter_mati = "viking_3[3][frame_mati]"
            karakter_serang = "viking_3[4][frame]"
        player=pygame.transform.scale(pygame.transform.flip(pygame.image.load(eval(karakter_jalan)), True, False), (ukuran_player_pilih, ukuran_player_pilih)).convert_alpha()
        
        screen.fill((0,0,0))
        screen.blit(kanan, (int(lebar_layar/100*75)-int((tinggi_layar/100*25)/4), int(tinggi_layar-(tinggi_layar/5))))
        screen.blit(kiri, (int(lebar_layar/100*25-int((tinggi_layar/100*25)/4)), int(tinggi_layar-(tinggi_layar/5))))
        screen.blit(play_button, (int(lebar_layar/2-(lebar_layar/100*25)/2), int(tinggi_layar-(tinggi_layar/5))))
        
        screen.blit(player, (int(lebar_layar/2-(ukuran_player_pilih/2)), int(tinggi_layar/2-(ukuran_player_pilih/2))))
        
        
        kanan_rect = kanan.get_rect()
        kanan_rect.top = int(tinggi_layar-(tinggi_layar/5))
        kanan_rect.left = int(lebar_layar/100*75)-int((tinggi_layar/100*25)/4)
        
        kiri_rect = kiri.get_rect()
        kiri_rect.top = int(tinggi_layar-(tinggi_layar/5))
        kiri_rect.left = int(lebar_layar/100*25-int((tinggi_layar/100*25)/4))
        
        play_button_rect = play_button.get_rect()
        play_button_rect.top = int(tinggi_layar-(tinggi_layar/5))
        play_button_rect.left = int(lebar_layar/2-(lebar_layar/100*25)/2)
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                WTW=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    WTW=False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos= pygame.mouse.get_pos()
                    if kiri_rect.collidepoint(mouse_pos):
                        karakter-=1
                    if kanan_rect.collidepoint(mouse_pos):
                        karakter+=1
                    if play_button_rect.collidepoint(mouse_pos):
                        pilih_karakter=False
                        play=True
                        background =random.randint(1, 3)
                        if background==1:
                            background = pygame.transform.scale(pygame.image.load("background/game_background_1.png"), (lebar_layar, tinggi_layar)).convert()
                        if background==2:
                            background = pygame.transform.scale(pygame.image.load("background/game_background_3.1.png"), (lebar_layar, tinggi_layar)).convert()
                        if background==3:
                            background = pygame.transform.scale(pygame.image.load("background/game_background_4.png"), (lebar_layar, tinggi_layar)).convert()
                        
                        
    if game_over_screen==True:
        screen.blit(game_over, (0, 0))
        
        
        text=myfont.render("skor kamu adalah", False, (0, 0, 0))
        mencetak_score = myfont.render(str(score), False, (0, 0, 0))
        
        screen.blit(text, (0, 0))
        screen.blit(mencetak_score,(int(lebar_layar/2),0))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_over_screen=False
                pilih_karakter=True
                score=0
            if event.type == pygame.KEYDOWN:
                game_over_screen=False
                pilih_karakter=True
                score=0
            if event.type==pygame.QUIT:
                pygame.quit()
                WTW=False
    
    
    if play==True:
        #mengatur player=======================================================================================
            #animasi player
            if momentum=="bergerak":
                frame+=1
                if frame>9:
                    frame=0
                if arah=="kanan":
                    player=pygame.transform.scale(pygame.image.load(eval(karakter_jalan)), (ukuran_player, ukuran_player)).convert_alpha()
                else:
                    player=pygame.transform.scale(pygame.transform.flip(pygame.image.load(eval(karakter_jalan)), True, False), (ukuran_player, ukuran_player)).convert_alpha()
                    
            elif momentum=="diam":
                frame+=1
                if frame>9:
                    frame=0
                if arah=="kanan":
                    player=pygame.transform.scale(pygame.image.load(eval(karakter_diam)), (ukuran_player, ukuran_player)).convert_alpha()
                else:
                    player=pygame.transform.scale(pygame.transform.flip(pygame.image.load(eval(karakter_diam)), True, False), (ukuran_player, ukuran_player)).convert_alpha()
                    
            if pertarungan=="serang" or pertarungan=="serang1":
                frame+=1
                if pertarungan=="serang":
                    frame=0
                    pertarungan="serang1"
                if frame==8:
                    pertarungan="diam"
                if arah=="kanan":
                    player=pygame.transform.scale(pygame.image.load(eval(karakter_serang)), (ukuran_player, ukuran_player)).convert_alpha()
                else:
                    player=pygame.transform.scale(pygame.transform.flip(pygame.image.load(eval(karakter_serang)), True, False), (ukuran_player, ukuran_player)).convert_alpha()
                    
            #kontrol player(gerakan, serang, dan posisi player, dll)==============================================================================================
            
            if momentum=="bergerak":
                if arah=="kanan":
                    playerpos[0] += step
                else:
                    playerpos[0] -= step
                    
            if playerpos[1]==1:  #mengatur posisi player tiap tingkat tanah
                playerpos[1]=int(tinggi_layar/4) - int(tinggi_layar/100*30)
            if playerpos[1]==2:
                playerpos[1]=int(tinggi_layar/4)*2 - int(tinggi_layar/100*30)
            if playerpos[1]==3:
                playerpos[1]=int(tinggi_layar/4)*3 - int(tinggi_layar/100*30)
            if playerpos[1]==4:
                playerpos[1]=int(tinggi_layar/4)*4 - int(tinggi_layar/100*30)
            
            
            #mengatur posisi player dan musuh
            acak_posisi-=1
            if acak_posisi==0: #mengacak posisi player dan musuh
                playerpos[0] = random.randint(0, lebar_layar)
                playerpos[1] = random.randint(1, 4)
                
                musuh_1pos[0] = random.randint(0, lebar_layar)
                musuh_1pos[1] = random.randint(1, 4)
                musuh_2pos[0] = random.randint(0, lebar_layar)
                musuh_2pos[1] = random.randint(1, 4)
                musuh_3pos[0] = random.randint(0, lebar_layar)
                musuh_3pos[1] = random.randint(1, 4)
                musuh_4pos[0] = random.randint(0, lebar_layar)
                musuh_4pos[1] = random.randint(1, 4)
                
                acak_posisi=random.randint(10, 100)
                
            if playerpos[0] > lebar_layar/100*89: #jika player pos==89% dari lebar layar(sisi paling kanan yang kita lihat), player akan dikembalikan ke sisi kiri layar
                playerpos[0] = -(ukuran_player-(ukuran_player/100*38))
            elif playerpos[0] < -(ukuran_player-(ukuran_player/100*38)): #sebaliknya
                playerpos[0] = lebar_layar/100*89
                
            if musuh_1pos[0] > lebar_layar/100*89: #setiap karakter harus diberi kode ini agar tidak keluar batas
                musuh_1pos[0] = -(ukuran_player-(ukuran_player/100*38))
            elif musuh_1pos[0] < -(ukuran_player-(ukuran_player/100*38)):
                musuh_1pos[0] = lebar_layar/100*89
            if musuh_2pos[0] > lebar_layar/100*89: #setiap karakter harus diberi kode ini agar tidak keluar batas
                musuh_2pos[0] = -(ukuran_player-(ukuran_player/100*38))
            elif musuh_2pos[0] < -(ukuran_player-(ukuran_player/100*38)):
                musuh_2pos[0] = lebar_layar/100*89
            if musuh_3pos[0] > lebar_layar/100*89: #setiap karakter harus diberi kode ini agar tidak keluar batas
                musuh_3pos[0] = -(ukuran_player-(ukuran_player/100*38))
            elif musuh_3pos[0] < -(ukuran_player-(ukuran_player/100*38)):
                musuh_3pos[0] = lebar_layar/100*89
            if musuh_4pos[0] > lebar_layar/100*89: #setiap karakter harus diberi kode ini agar tidak keluar batas
                musuh_4pos[0] = -(ukuran_player-(ukuran_player/100*38))
            elif musuh_4pos[0] < -(ukuran_player-(ukuran_player/100*38)):
                musuh_4pos[0] = lebar_layar/100*89
            
            #membuat musuh====================================================================================================
            musuh_1frame+=1
            if musuh_1frame==10:
                if musuh_1nyawa>0:
                    musuh_1frame=0
                else:
                    musuh_1frame=9
            musuh_1hitung -= 1
                
            if musuh_1pos[1]==1:
                musuh_1pos[1]=int(tinggi_layar/4) - int(tinggi_layar/100*30)
            if musuh_1pos[1]==2:
                musuh_1pos[1]=int(tinggi_layar/4)*2 - int(tinggi_layar/100*30)
            if musuh_1pos[1]==3:
                musuh_1pos[1]=int(tinggi_layar/4)*3 - int(tinggi_layar/100*30)
            if musuh_1pos[1]==4:
                musuh_1pos[1]=int(tinggi_layar/4)*4 - int(tinggi_layar/100*30)
                
                #mengatur arah gerakan musuh
            if musuh_1hitung<0:
                musuh_1arah=random.randint(1, 2)
                if musuh_1arah==1:
                    musuh_1arah="kiri"
                else:
                    musuh_1arah="kanan"
                musuh_1hitung=random.randint(1, 30)
            
                #animasi musuh
            if musuh_1arah=="kiri":
                musuh_1 = pygame.transform.scale(pygame.transform.flip(pygame.image.load(eval(musuh_1_jalan)), True, False), (ukuran_player, ukuran_player)).convert_alpha()
                musuh_1pos[0] -= musuh_1step
                
            if musuh_1arah=="kanan":
                musuh_1=pygame.transform.scale(pygame.image.load(eval(musuh_1_jalan)), (ukuran_player, ukuran_player)).convert_alpha()
                musuh_1pos[0] += musuh_1step
            
            if musuh_1nyawa<0 and musuh_1nyawa>-11: #animasi mati 1
                musuh_1step = 0 #membuat musuh tidak bisa bergerak kalau mati
                musuh_1jeda_sebelum_respawn=60
                musuh_1frame=0
                musuh_1nyawa=-12
                score+=1
            if musuh_1jeda_sebelum_respawn>0: #animasi mati 2
                musuh_1jeda_sebelum_respawn-=1
                musuh_1=pygame.transform.scale(pygame.image.load(eval(musuh_1_mati)), (ukuran_player, ukuran_player))
                if musuh_1jeda_sebelum_respawn==1:
                    musuh_1step = int(lebar_layar/100*3) #membuat musuh bisa bergerak lagi
                    musuh_1nyawa=100 #mengembalikan nyawa musuh
                    musuh_1jeda_sebelum_respawn=0
                    musuh_1pos[0]=random.randint(0,640)#respawn di tempat baru
                    musuh_1pos[1]=random.randint(1, 4)
            
            if musuh_1pertarungan=="serang" or musuh_1pertarungan=="serang1":
                if musuh_1pertarungan=="serang":
                    musuh_1frame=-1
                    if musuh_1_rect.colliderect(player_rect):
                        nyawa-=random.randint(1,10)
                    if musuh_1_rect.colliderect(musuh_2_rect):
                        musuh_2nyawa-=random.randint(1,10)
                    if musuh_1_rect.colliderect(musuh_3_rect):
                        musuh_3nyawa-=random.randint(1,10)
                    if musuh_1_rect.colliderect(musuh_4_rect):
                        musuh_4nyawa-=random.randint(1,10)
                    musuh_1pertarungan="serang1"
                else:
                    musuh_1frame+=1
                    if musuh_1frame>9:
                        musuh_1pertarungan="diam"
                    else:
                        if musuh_1arah=="kanan":
                            musuh_1=pygame.transform.scale(pygame.image.load(eval(musuh_1_serang)), (ukuran_player, ukuran_player))
                        elif musuh_1arah=="kiri":
                            musuh_1=pygame.transform.scale(pygame.transform.flip(pygame.image.load(eval(musuh_1_serang)), True, False), (ukuran_player, ukuran_player))
                            
            #2
            musuh_2frame+=1
            if musuh_2frame==10:
                if musuh_2nyawa>0:
                    musuh_2frame=0
                else:
                    musuh_2frame=9
            musuh_2hitung -= 1
                
            if musuh_2pos[1]==1:
                musuh_2pos[1]=int(tinggi_layar/4) - int(tinggi_layar/100*30)
            if musuh_2pos[1]==2:
                musuh_2pos[1]=int(tinggi_layar/4)*2 - int(tinggi_layar/100*30)
            if musuh_2pos[1]==3:
                musuh_2pos[1]=int(tinggi_layar/4)*3 - int(tinggi_layar/100*30)
            if musuh_2pos[1]==4:
                musuh_2pos[1]=int(tinggi_layar/4)*4 - int(tinggi_layar/100*30)
                
                #mengatur arah gerakan musuh
            if musuh_2hitung<0:
                musuh_2arah=random.randint(1, 2)
                if musuh_2arah==1:
                    musuh_2arah="kiri"
                else:
                    musuh_2arah="kanan"
                musuh_2hitung=random.randint(1, 30)
            
                #animasi musuh
            if musuh_2arah=="kiri":
                musuh_2 = pygame.transform.scale(pygame.transform.flip(pygame.image.load(eval(musuh_2_jalan)), True, False), (ukuran_player, ukuran_player)).convert_alpha()
                musuh_2pos[0] -= musuh_2step
                
            if musuh_2arah=="kanan":
                musuh_2=pygame.transform.scale(pygame.image.load(eval(musuh_2_jalan)), (ukuran_player, ukuran_player)).convert_alpha()
                musuh_2pos[0] += musuh_2step
            
            if musuh_2nyawa<0 and musuh_2nyawa>-11: #animasi mati 1
                musuh_2step = 0 #membuat musuh tidak bisa bergerak kalau mati
                musuh_2jeda_sebelum_respawn=60
                musuh_2frame=0
                musuh_2nyawa=-12
                score+=1
            if musuh_2jeda_sebelum_respawn>0: #animasi mati 2
                musuh_2jeda_sebelum_respawn-=1
                musuh_2=pygame.transform.scale(pygame.image.load(eval(musuh_2_mati)), (ukuran_player, ukuran_player))
                if musuh_2jeda_sebelum_respawn==1:
                    musuh_2step = int(lebar_layar/100*3) #membuat musuh bisa bergerak lagi
                    musuh_2nyawa=100 #mengembalikan nyawa musuh
                    musuh_2jeda_sebelum_respawn=0
                    musuh_2pos[0]=random.randint(0,640)#respawn di tempat baru
                    musuh_2pos[1]=random.randint(1, 4)
            
            if musuh_2pertarungan=="serang" or musuh_2pertarungan=="serang1":
                if musuh_2pertarungan=="serang":
                    musuh_2frame=-1
                    if musuh_2_rect.colliderect(player_rect):
                        nyawa-=random.randint(1,10)
                    if musuh_2_rect.colliderect(musuh_1_rect):
                        musuh_1nyawa-=random.randint(1,10)
                    if musuh_2_rect.colliderect(musuh_3_rect):
                        musuh_3nyawa-=random.randint(1,10)
                    if musuh_2_rect.colliderect(musuh_4_rect):
                        musuh_4nyawa-=random.randint(1,10)
                    musuh_2pertarungan="serang1"
                else:
                    musuh_2frame+=1
                    if musuh_2frame>9:
                        musuh_2pertarungan="diam"
                    else:
                        if musuh_2arah=="kanan":
                            musuh_2=pygame.transform.scale(pygame.image.load(eval(musuh_2_serang)), (ukuran_player, ukuran_player))
                        elif musuh_2arah=="kiri":
                            musuh_2=pygame.transform.scale(pygame.transform.flip(pygame.image.load(eval(musuh_2_serang)), True, False), (ukuran_player, ukuran_player))
            
            #3
            musuh_3frame+=1
            if musuh_3frame==10:
                if musuh_3nyawa>0:
                    musuh_3frame=0
                else:
                    musuh_3frame=9
            musuh_3hitung -= 1
                
            if musuh_3pos[1]==1:
                musuh_3pos[1]=int(tinggi_layar/4) - int(tinggi_layar/100*30)
            if musuh_3pos[1]==2:
                musuh_3pos[1]=int(tinggi_layar/4)*2 - int(tinggi_layar/100*30)
            if musuh_3pos[1]==3:
                musuh_3pos[1]=int(tinggi_layar/4)*3 - int(tinggi_layar/100*30)
            if musuh_3pos[1]==4:
                musuh_3pos[1]=int(tinggi_layar/4)*4 - int(tinggi_layar/100*30)
                
                #mengatur arah gerakan musuh
            if musuh_3hitung<0:
                musuh_3arah=random.randint(1, 2)
                if musuh_3arah==1:
                    musuh_3arah="kiri"
                else:
                    musuh_3arah="kanan"
                musuh_3hitung=random.randint(1, 30)
            
                #animasi musuh
            if musuh_3arah=="kiri":
                musuh_3 = pygame.transform.scale(pygame.transform.flip(pygame.image.load(eval(musuh_3_jalan)), True, False), (ukuran_player, ukuran_player)).convert_alpha()
                musuh_3pos[0] -= musuh_3step
                
            if musuh_3arah=="kanan":
                musuh_3=pygame.transform.scale(pygame.image.load(eval(musuh_3_jalan)), (ukuran_player, ukuran_player)).convert_alpha()
                musuh_3pos[0] += musuh_3step
            
            if musuh_3nyawa<0 and musuh_3nyawa>-11: #animasi mati 1
                musuh_3step = 0 #membuat musuh tidak bisa bergerak kalau mati
                musuh_3jeda_sebelum_respawn=60
                musuh_3frame=0
                musuh_3nyawa=-12
                score+=1
            if musuh_3jeda_sebelum_respawn>0: #animasi mati 2
                musuh_3jeda_sebelum_respawn-=1
                musuh_3=pygame.transform.scale(pygame.image.load(eval(musuh_3_mati)), (ukuran_player, ukuran_player))
                if musuh_3jeda_sebelum_respawn==1:
                    musuh_3step = int(lebar_layar/100*3) #membuat musuh bisa bergerak lagi
                    musuh_3nyawa=100 #mengembalikan nyawa musuh
                    musuh_3jeda_sebelum_respawn=0
                    musuh_3pos[0]=random.randint(0,640)#respawn di tempat baru
                    musuh_3pos[1]=random.randint(1, 4)
            
            if musuh_3pertarungan=="serang" or musuh_3pertarungan=="serang1":
                if musuh_3pertarungan=="serang":
                    musuh_3frame=-1
                    if musuh_3_rect.colliderect(player_rect):
                        nyawa-=random.randint(1,10)
                    if musuh_3_rect.colliderect(musuh_1_rect):
                        musuh_1nyawa-=random.randint(1,10)
                    if musuh_3_rect.colliderect(musuh_2_rect):
                        musuh_2nyawa-=random.randint(1,10)
                    if musuh_3_rect.colliderect(musuh_4_rect):
                        musuh_4nyawa-=random.randint(1,10)
                    musuh_3pertarungan="serang1"
                else:
                    musuh_3frame+=1
                    if musuh_3frame>9:
                        musuh_3pertarungan="diam"
                    else:
                        if musuh_3arah=="kanan":
                            musuh_3=pygame.transform.scale(pygame.image.load(eval(musuh_3_serang)), (ukuran_player, ukuran_player))
                        elif musuh_3arah=="kiri":
                            musuh_3=pygame.transform.scale(pygame.transform.flip(pygame.image.load(eval(musuh_3_serang)), True, False), (ukuran_player, ukuran_player))
                            
                            
            #4
            musuh_4frame+=1
            if musuh_4frame==10:
                if musuh_4nyawa>0:
                    musuh_4frame=0
                else:
                    musuh_4frame=9
            musuh_4hitung -= 1
                
            if musuh_4pos[1]==1:
                musuh_4pos[1]=int(tinggi_layar/4) - int(tinggi_layar/100*30)
            if musuh_4pos[1]==2:
                musuh_4pos[1]=int(tinggi_layar/4)*2 - int(tinggi_layar/100*30)
            if musuh_4pos[1]==3:
                musuh_4pos[1]=int(tinggi_layar/4)*3 - int(tinggi_layar/100*30)
            if musuh_4pos[1]==4:
                musuh_4pos[1]=int(tinggi_layar/4)*4 - int(tinggi_layar/100*30)
                
                #mengatur arah gerakan musuh
            if musuh_4hitung<0:
                musuh_4arah=random.randint(1, 2)
                if musuh_4arah==1:
                    musuh_4arah="kiri"
                else:
                    musuh_4arah="kanan"
                musuh_4hitung=random.randint(1, 30)
            
                #animasi musuh
            if musuh_4arah=="kiri":
                musuh_4 = pygame.transform.scale(pygame.transform.flip(pygame.image.load(eval(musuh_4_jalan)), True, False), (ukuran_player, ukuran_player)).convert_alpha()
                musuh_4pos[0] -= musuh_4step
                
            if musuh_4arah=="kanan":
                musuh_4=pygame.transform.scale(pygame.image.load(eval(musuh_4_jalan)), (ukuran_player, ukuran_player)).convert_alpha()
                musuh_4pos[0] += musuh_4step
            
            if musuh_4nyawa<0 and musuh_4nyawa>-11: #animasi mati 1
                musuh_4step = 0 #membuat musuh tidak bisa bergerak kalau mati
                musuh_4jeda_sebelum_respawn=60
                musuh_4frame=0
                musuh_4nyawa=-12
                score+=1
            if musuh_4jeda_sebelum_respawn>0: #animasi mati 2
                musuh_4jeda_sebelum_respawn-=1
                musuh_4=pygame.transform.scale(pygame.image.load(eval(musuh_4_mati)), (ukuran_player, ukuran_player))
                if musuh_4jeda_sebelum_respawn==1:
                    musuh_4step = int(lebar_layar/100*3) #membuat musuh bisa bergerak lagi
                    musuh_4nyawa=100 #mengembalikan nyawa musuh
                    musuh_4jeda_sebelum_respawn=0
                    musuh_4pos[0]=random.randint(0,640)#respawn di tempat baru
                    musuh_4pos[1]=random.randint(1, 4)
            
            if musuh_4pertarungan=="serang" or musuh_4pertarungan=="serang1":
                if musuh_4pertarungan=="serang":
                    musuh_4frame=-1
                    if musuh_4_rect.colliderect(player_rect):
                        nyawa-=random.randint(1,10)
                    if musuh_4_rect.colliderect(musuh_1_rect):
                        musuh_1nyawa-=random.randint(1,10)
                    if musuh_4_rect.colliderect(musuh_2_rect):
                        musuh_2nyawa-=random.randint(1,10)
                    if musuh_4_rect.colliderect(musuh_3_rect):
                        musuh_3nyawa-=random.randint(1,10)
                    musuh_4pertarungan="serang1"
                else:
                    musuh_4frame+=1
                    if musuh_4frame>9:
                        musuh_4pertarungan="diam"
                    else:
                        if musuh_4arah=="kanan":
                            musuh_4=pygame.transform.scale(pygame.image.load(eval(musuh_4_serang)), (ukuran_player, ukuran_player))
                        elif musuh_4arah=="kiri":
                            musuh_4=pygame.transform.scale(pygame.transform.flip(pygame.image.load(eval(musuh_4_serang)), True, False), (ukuran_player, ukuran_player))    
                
                
            #mengatur benturan antar objek
                #membuat rect
            player_rect = player.get_rect()
            player_rect.inflate_ip(-(int(ukuran_player/100*70)), -(int(ukuran_player/100*33.5))) #mengecilkan rectnya. lebarnya di kurang 70% dari ukuran gambar, tingginya 33,5% ukuran gambar(gambarnya bujursangkar/sisinya sama)
            player_rect.top = playerpos[1]
            player_rect.left = playerpos[0]
            
            musuh_1_rect=musuh_1.get_rect()
            musuh_1_rect.inflate_ip(-(int(ukuran_player/100*70)), -(int(ukuran_player/100*33.5)))
            musuh_1_rect.top = musuh_1pos[1]
            musuh_1_rect.left = musuh_1pos[0]
            
            musuh_2_rect=musuh_2.get_rect()
            musuh_2_rect.inflate_ip(-(int(ukuran_player/100*70)), -(int(ukuran_player/100*33.5)))
            musuh_2_rect.top = musuh_2pos[1]
            musuh_2_rect.left = musuh_2pos[0]
            
            musuh_3_rect=musuh_3.get_rect()
            musuh_3_rect.inflate_ip(-(int(ukuran_player/100*70)), -(int(ukuran_player/100*33.5)))
            musuh_3_rect.top = musuh_3pos[1]
            musuh_3_rect.left = musuh_3pos[0]
            
            musuh_4_rect=musuh_4.get_rect()
            musuh_4_rect.inflate_ip(-(int(ukuran_player/100*70)), -(int(ukuran_player/100*33.5)))
            musuh_4_rect.top = musuh_4pos[1]
            musuh_4_rect.left = musuh_4pos[0]
            
            kanan_rect = kanan.get_rect()
            kanan_rect.top = int(tinggi_layar-(tinggi_layar/5))
            kanan_rect.left = int(lebar_layar/100*25/1.5)
            
            kiri_rect = kiri.get_rect()
            kiri_rect.top = int(tinggi_layar-(tinggi_layar/5))
            kiri_rect.left = int(lebar_layar/100*25/6)
            
            attack_rect = attack.get_rect()
            attack_rect.top = int(tinggi_layar-(tinggi_layar/5))
            attack_rect.left = int(lebar_layar-(lebar_layar/7))         
            
                #saat terjadi benturan
            if (player_rect.colliderect(musuh_1_rect) or player_rect.colliderect(musuh_2_rect) or player_rect.colliderect(musuh_3_rect) or player_rect.colliderect(musuh_4_rect)) and nyawa>0:
                if player_rect.colliderect(musuh_1_rect):
                    if pertarungan == "serang1":
                        musuh_1nyawa -= random.randint(0, 10)
                if player_rect.colliderect(musuh_2_rect):
                    if pertarungan == "serang1":
                        musuh_2nyawa -= random.randint(0, 10)
                if player_rect.colliderect(musuh_3_rect):
                    if pertarungan == "serang1":
                        musuh_3nyawa -= random.randint(0, 10)
                if player_rect.colliderect(musuh_4_rect):
                    if pertarungan == "serang1":
                        musuh_4nyawa -= random.randint(0, 10)
                    
            if (musuh_1_rect.colliderect(player_rect) or musuh_1_rect.colliderect(musuh_2_rect) or musuh_1_rect.colliderect(musuh_3_rect) or musuh_1_rect.colliderect(musuh_4_rect)) and musuh_1nyawa>-11:
                musuh_1jeda_sebelum_serang+=1
                if musuh_1jeda_sebelum_serang>2:
                    musuh_1pertarungan=random.randint(1, 2)
                    if musuh_1pertarungan==1:
                        musuh_1pertarungan="serang"
                    musuh_1jeda_sebelum_serang=0
            else: # kalo gak ada ini, saat posisi==serang dan musuh tidak berbenturan lagi dengan player, musuh akan terus menyerang
                musuh_1pertarungan="diam"
                
            if (musuh_2_rect.colliderect(player_rect) or musuh_2_rect.colliderect(musuh_1_rect) or musuh_2_rect.colliderect(musuh_3_rect) or musuh_2_rect.colliderect(musuh_4_rect)) and musuh_2nyawa>-11:
                musuh_2jeda_sebelum_serang+=1
                if musuh_2jeda_sebelum_serang>2:
                    musuh_2pertarungan=random.randint(1, 2)
                    if musuh_2pertarungan==1:
                        musuh_2pertarungan="serang"
                    musuh_2jeda_sebelum_serang=0
            else: # kalo gak ada ini, saat posisi==serang dan musuh tidak berbenturan lagi dengan player, musuh akan terus menyerang
                musuh_2pertarungan="diam"
                
            if (musuh_3_rect.colliderect(player_rect) or musuh_3_rect.colliderect(musuh_1_rect) or musuh_3_rect.colliderect(musuh_2_rect) or musuh_3_rect.colliderect(musuh_4_rect)) and musuh_3nyawa>-11:
                musuh_3jeda_sebelum_serang+=1
                if musuh_3jeda_sebelum_serang>2:
                    musuh_3pertarungan=random.randint(1, 2)
                    if musuh_3pertarungan==1:
                        musuh_3pertarungan="serang"
                    musuh_3jeda_sebelum_serang=0
            else: # kalo gak ada ini, saat posisi==serang dan musuh tidak berbenturan lagi dengan player, musuh akan terus menyerang
                musuh_3pertarungan="diam"
                
            if (musuh_4_rect.colliderect(player_rect) or musuh_4_rect.colliderect(musuh_1_rect) or musuh_4_rect.colliderect(musuh_2_rect) or musuh_4_rect.colliderect(musuh_3_rect)) and musuh_4nyawa>-11:
                musuh_4jeda_sebelum_serang+=1
                if musuh_4jeda_sebelum_serang>2:
                    musuh_4pertarungan=random.randint(1, 2)
                    if musuh_4pertarungan==1:
                        musuh_4pertarungan="serang"
                    musuh_4jeda_sebelum_serang=0
            else: # kalo gak ada ini, saat posisi==serang dan musuh tidak berbenturan lagi dengan player, musuh akan terus menyerang
                musuh_4pertarungan="diam"
            
            #menggambar semua objek ke layar======================================================================================
            
            if nyawa<1:
                step=0
                frame_mati+=1
                if frame_mati>9:
                    frame_mati=9
                player=pygame.transform.scale(pygame.image.load(eval(karakter_mati)), (ukuran_player, ukuran_player)) 
            
            screen.blits(((background, (0, 0)), (tanah, tanah1), (tanah, tanah2), (tanah, tanah3), (tanah, tanah4), (player, playerpos), (musuh_1, musuh_1pos), (musuh_2, musuh_2pos), (musuh_3, musuh_3pos), (musuh_4, musuh_4pos)))
            
            mencetak_score = myfont.render(str(score), False, (0, 0, 0))
            screen.blit(mencetak_score,(int(lebar_layar/2),0))
            
            screen.blit(kanan, (int(lebar_layar/100*25/1.5), int(tinggi_layar-(tinggi_layar/5))))
            screen.blit(kiri, (int(lebar_layar/100*25/6), int(tinggi_layar-(tinggi_layar/5))))
            screen.blit(attack, (int(lebar_layar-(lebar_layar/7)), int(tinggi_layar-(tinggi_layar/5))))
            screen.blit(panah, playerpos)
            
            if nyawa<1 and frame_mati==9:
                pygame.time.wait(200)
                if score>highscore:
                    my_file = open("score.txt", "w")
                    my_file.write(str(score))
                    my_file.close()
                    highscore=score
                nyawa=100
                step= int(lebar_layar/100*3)
                frame_mati=0
                game_over_screen=True
                play=False
            
            pygame.display.update()
            
            
            #kontrol game==============================================================================================================
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    WTW=False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        WTW=False
                    if event.key == pygame.K_LEFT:
                        arah="kiri"
                        momentum="bergerak"
                    if event.key == pygame.K_RIGHT:
                        arah="kanan"
                        momentum="bergerak"
                    if event.key == pygame.K_SPACE:
                        pertarungan="serang"
                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        momentum="diam"
                    if event.key == pygame.K_RIGHT:
                        momentum="diam"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos= pygame.mouse.get_pos()
                    if kiri_rect.collidepoint(mouse_pos):
                        arah="kiri"
                        momentum="bergerak"
                    if kanan_rect.collidepoint(mouse_pos):
                        arah="kanan"
                        momentum="bergerak"
                    if attack_rect.collidepoint(mouse_pos):
                        pertarungan="serang"
                        
                if event.type == pygame.MOUSEBUTTONUP:
                    momentum="diam"
                
                
                
#musuh terlalu cepat mati. kemungkinan karena pake if pertarungan == "serang1": jadinya player nyerang sampai pertarungan="diam". kita pakai if pertarungan == "serang1": karena id pertarungan=="serang" ada di atasnya, jadi udah berubah dan gak akan mengurangu nyawa musuh.