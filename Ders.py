isim = input("Adınızı girin: ")
yas = input("Yaşınızı girin: ")

with open("kullanici.txt","a",encoding="utf-8") as dosya:
    dosya.write(f"Kullanıcının adı {isim}, yaşı {yas}")