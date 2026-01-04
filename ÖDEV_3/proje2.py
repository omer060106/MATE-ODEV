import re

def sifrekontrol(sifre):
    
    if len(sifre) < 8:
        return "şifre çok kısa en az 8 karakter olmalı"

    if not re.search(r"[A-Z]", sifre):
        return "şifrenizde en az bir büyük harf olmalı"

    if not re.search(r"[0-9]", sifre):
        return "şifrenizde en az bir rakam olmalı."
    
    if not re.search(r"[\W]", sifre):
        return "şifrenizde en az bir özel karakter olmalı"

    return True

if __name__ == "__main__":
    print("-" * 40)
    print("güvenli giriş")
    print("-" * 40)

    while True:
        kullanici_sifresi = input("lütfen yeni şifrenizi belirleyin çıkış için 'q' =  \n")
        
        if kullanici_sifresi.lower() == 'q':
            print("sistemden çıkılıyor")
            break
        
        sonuc = sifrekontrol(kullanici_sifresi)
        
        if sonuc == True:
            print(f"başarılı şifreniz kabul edildi = {kullanici_sifresi}")
            break 
        else:
            print("eksik şifre türü lütfen tekrar deneyin\n")