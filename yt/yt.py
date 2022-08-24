import time
from pytube import YouTube
import os      
def display_list(veri):
    veri = str(veri)
    a = veri.index("res")
    b = veri.index("fps")
    veri = veri[a:b-2].split('"')
    del veri[0]
    return veri
def dosya_kontrol():
    sonuc = False
    main_dizin = os.getcwd()
    for i in os.listdir(main_dizin):
        if i == "Videolar":
            sonuc = True
    if sonuc == False:
        os.mkdir("Videolar")        
def main():
    dosya_kontrol()
    display_liste = []
    link = input("Video Linki: ")
    yt = YouTube(link)
    video_isim = yt.title
    print(video_isim)
    yt.title = yt.title + time.strftime('%Y'+"-"+'%m'+"-"+'%d'+"-"+'%H'+"-"+'%M'+"-"+'%S')
    for i,j in enumerate(yt.streams.filter(file_extension="mp4",progressive=True)):
        print(i+1,display_list(j))
        display_liste.append(display_list(j))
    n = int(input("Hangisini İndirmek istiyorsun: "))
    mp4s = yt.streams.filter(progressive=True,file_extension="mp4")
    mp4s[n-1].download("Videolar")
main()