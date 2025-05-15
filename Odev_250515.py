#Kullanıcı, çalıştırmak istediği programı seçer
secilenOdev = input(
"""Lütfen ödev numarası seçiniz:
1.Matematik İşlemleri
2.Gauss Toplamı
3.Çift Sayılar
4.Metin Çevirme
Seçiminiz: """
    )
if secilenOdev == "1" or secilenOdev == "1.":
    # Görev 1: Kullanıcıdan iki sayı alıp, aşağıdaki işlemleri yaparak ekrana yazdıran bir Python programı yazın:
    # Toplama (+)
    # Çıkarma (-)
    # Çarpma (* )
    # Bölme (/)
    # Mod alma (%)
    # Üs alma (** )

    #Kullanıcıdan sayılar alınır
    birinciSayi = float(input("Birinci sayıyı giriniz: "))
    ikinciSayi = float(input("İkinci sayıyı giriniz: "))
    
    #İşlemler yapılıp kullanıcıya sunulur
    toplama = birinciSayi + ikinciSayi
    cikarma = birinciSayi - ikinciSayi
    carpma = birinciSayi * ikinciSayi
    bolme = birinciSayi / ikinciSayi
    mod = birinciSayi % ikinciSayi
    us = birinciSayi ** ikinciSayi
    print(
f"""Toplama: {toplama}
Çıkarma: {cikarma}
Çarpma: {carpma}
Bölme: {bolme}
Mod: {mod}
Üs: {us}
""")
elif secilenOdev == "2" or secilenOdev == "2.":    
    #Görev 2: Kullanıcıdan bir sayı alarak 1’den o sayıya kadar olan sayıların toplamını hesaplayan bir Python programı yazın. (For veya While döngüsü kullanın.)
    #Kullanıcıdan sayı alınır
    alinanSayi = int(input("Lütfen pozitif bir tam sayı giriniz: "))
    #Saymaya 1 den başlanır
    x = 1
    #Kontrol için toplam'a 0 atanır
    toplam = 0
    #1 - alinanSayi arası sayma yapmak için x sayıya eşit ya da büyük oluncaya dek döngü sürer, 1 den küçük bir sayı girilmesi halinde döngüye başlamaması için büyüktür kullanılmıştır
    while x <= alinanSayi:
        toplam = toplam + x
        x = x + 1
    #Kontrol yapılır
    if toplam == 0:
        print("Lütfen tekrar deneyiniz")
    else:
        print(toplam)
elif secilenOdev == "3" or secilenOdev == "3.":   
    #Görev 3: 1 ile 100 arasındaki çift sayıları ekrana yazdıran bir Python programı yazın. 
    ciftSayilar = []
    x = 1
    #1 den başlayarak yüze kadar bütün sayıların 2 ye göre modlarını alır, 0 olanları (bunlar çifttir) listeye ekle ve kullanıcıya sunar 
    while x<=100:
        if (x%2)==0:
            ciftSayilar.append(x)
        x=x+1
    print(ciftSayilar)
elif secilenOdev == "4" or secilenOdev == "4.":  
    #Görev 4: Kullanıcıdan alınan bir metni ters çeviren ve ekrana yazdıran bir Python programı yazın. (Döngü kullanarak yapın.)
    #Kullanıcıdan metin alınır
    alinanMetin = input("Bir metin giriniz: ")
    tersMetin = ""
    #Metin içindeki karaktleri soldan sağa eklemeye başlar, selam yazılmış olsun -> 1.Adımda s + [] -> 2.Adımda e + [s] -> 3.Adımda l + [es] şeklinde devam eder
    for karakter in alinanMetin:
        tersMetin = karakter + tersMetin
    print("Ters çevrilmiş metin:", tersMetin)
else:
    #Numara dışında bir şey seçmesi halinde uyarı verir
    print("Lütfen ödev numarası seçiniz")









