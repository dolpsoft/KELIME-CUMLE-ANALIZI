#---------------------Modüller--------------------------# 
import os
from time import sleep

#--------------Sınıf, Metotlar ve Nitelikler-----------# 
class kelimeCumleAnaliz:
#-------------------Örnek Nitelikleri-------------------# 
      def __init__(self):
        self.sesli_harfler= "aeıioöuüAEIİOÖUÜ"
        self.sessiz_harfler= "bcçdfgğhjklmnprsştvyzBCÇDFGĞHJKLMNPRSŞTVYZ"
        self.turkceKarakterler= "ğĞçÇşŞüÜöÖıİ"
        self.yabancıKarakterler="xwqXWQ"
#--------------Sesli Harf Kontrol Metodu-------------#         
      def sesliMi(self,giris):             
            sesliler= [ ]            
            for i in giris:
                  if i in self.sesli_harfler:
                     sesliler.append(i)            
            print(  "\n\n\n",  "-"*50, sep="")
            print("Kelimedeki/Cümledeki sesli harfler:")
            for i in sesliler:                
                print(i, end= " ")
            print(f'\nSesli Harf Sayısı:{len(sesliler)}')
            if len(sesliler)== 0:
                print("(Girilen kelimede veya cümlede herhangi bir sessli harf bulunmuyor.)")
            print( "\n", "-"*50, sep= "")
         
 
 #---------Türkçe Karakter Kontrol Metodu---------#            
      def turkceKarakter(self,giris):
          kelimedekiTurkceKarakterler=[]
          for i in giris:
                if i in self.turkceKarakterler:
                     kelimedekiTurkceKarakterler.append(i)
          print("-"*50)            
          print("Kelimedeki/Cümledeki türkçe karakterler:")
          for i in kelimedekiTurkceKarakterler:
                print(i , end= ' ')          
          print(f'\nTürkçe Karakter Sayısı:{len(kelimedekiTurkceKarakterler)}')
          if len(kelimedekiTurkceKarakterler)== 0:
             print("(Girilen kelimede veya cümlede herhangi bir Türkçe karakter bulunmuyor.)")
         
          print( "\n", "-"*50, sep= "")

#------------Sessiz Harf Kontrol Metodu------------#             
      def sessizMi(self,giris):             
            sessizler= [ ]            
            for i in giris:
                  if i in self.sessiz_harfler:
                     sessizler.append(i)
           
            print("Kelimedeki/Cümledeki sessiz harfler:")      
                            
            for i in sessizler:                
                print(i, end= " ")
            print(f'\nSessiz Harf Sayısı:{len(sessizler)}')
            if len(sessizler)== 0:
                print("(Girilen kelimede veya cümlede herhangi bir sessiz harf bulunmuyor.)")
            print( "\n", "-"*50, sep= "")
                
#- Harf ve Karakter Sayısını Hesaplama Metodu-#                 
      def harfSayısı(self, giris):
            print ("-"*50)
            harfler=[]
            İsaretler= ' . , ? - _ : ; / < > * + - = \ @ # $ % ! { } [ ] ( ) & | \'  \'\'  '
            for i in giris:
                harfler.append(i)
                
                if i in İsaretler:
                      harfler.remove(i)   
            print('Kelimedeki/Cümledeki tüm harflerin sayısı : {}' .format(len(harfler))) 
            print('Kelimedeki/Cümledeki tüm karakterlerin sayısı : {}' .format(len(giris)))

#--------Kelime Sayısını Hesaplama Metodu-------# 
      def kelimeSayısı(self, giris):
              kelimeler= giris
              kelimeSayi=kelimeler.split(' ')
              if len (giris)== 0:
                  print("Kelime sayısı: 0 \n(Hiçbir değer girilmediği için herhangi bir kelime bulunamıyor.)")
                  return
              else:
                  print('Kelime Sayısı: {}'.format(len(kelimeSayi)))
            
#---------Yabancı Karakter Kontrol Metodu---------#               
      def yabanciKarakter(self, giris):
           yabancilar= []
           print("Kelimedeki/Cümledeki yabancı karakterler:")   
           for i in giris:        
                 if i in self.yabancıKarakterler:        
                  yabancilar.append(i)
           for i in yabancilar:
                 print (i, end= " ")
           print(f"\nKelimedeki/Cümledeki yabancı harflerin sayısı: {len(yabancilar)}")
           if len(yabancilar)== 0:
                 print("(Girilen kelimede veya cümlede herhangi bir yabancı karakter bulunmuyor.)")
                 
             
#-------------Kelime-Cümle Girişi Metodu-----------#  
      def kelimeCumleSor(self):    
             print("KELİME-CÜMLE ANALİZ PROGRAMI")
             print ("⸻"*20)
             giris= input("Lütfen analizi yapılması istenen kelimeyi veya cümleyi giriniz: ")
             sleep(0.1)
             kontrol= kelimeCumleAnaliz() 
             sleep(0.1)
             kontrol.sesliMi(giris)
             sleep(0.1)
             kontrol.sessizMi(giris)
             sleep(0.1)
             kontrol.yabanciKarakter(giris)       
             sleep(0.1)      
             kontrol.turkceKarakter(giris)
             sleep(0.1)      
             kontrol.kelimeSayısı(giris)
             sleep(0.1)      
             kontrol.harfSayısı(giris)
             sleep(0.1)      
#-------------------Tekrar Metodu---------------------#                               
             soru= input("\n\n\n>>> Başka bir cümle veya kelime analizi yapmak ister misiniz? (E/H): ")
             if soru== "E" or soru== "e":
                    if os.name == 'nt': 
                       os.system('cls')
                    else:
                       os.system('clear')
             else:
                   print ("Programdan çıktınız.")
                   exit()
             
#-----------------------Döngü---------------------------#  
             
while True:
        
        obje= kelimeCumleAnaliz()
        obje.kelimeCumleSor()
               
#-----------------------Bitiş------------------------------#       

#Github: github.com/dolpsoft
#Twitter: twitter.com/dolpsoft
#İletişim: rekld26@gmail.com