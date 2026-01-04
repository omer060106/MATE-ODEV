import re

def veri_temizle(girisdosyasi, cikisdosyasi):

    print(f" {girisdosyasi} İşleniyor ")
    
    try:

        with open(girisdosyasi, "r", encoding="utf-8") as dosya:
            icerik = dosya.read()

        
        emaildegisken = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        bulunanmailler = re.findall(emaildegisken, icerik)

        teldegisken = r"(?:\+?\d{1,3}[ -]?)?\(?\d{3}\)?[ -.]?\d{3}[ -.]?\d{2,4}(?:[ -.]?\d{2})?"
        
        karmasiktelefon = re.findall(teldegisken, icerik)
        temiztelefon = []
        
        for tel in karmasiktelefon:
            
            rakamsayisi = len(re.sub(r"\D", "", tel)) 
            if 10 <= rakamsayisi <= 12:
                temiztelefon.append(tel)


        with open(cikisdosyasi, "w", encoding="utf-8") as temiz_dosya:
            temiz_dosya.write(f"{girisdosyasi} rapor\n\n")
            
            temiz_dosya.write(f"bulunan e posta sayısı ={len(bulunanmailler)}\n")
            temiz_dosya.write("-" * 30 + "\n")
            for mail in bulunanmailler:
                temiz_dosya.write(f"{mail}\n")
            
            temiz_dosya.write("\n")
            
            temiz_dosya.write(f"bulunan telefon numara sayısı = {len(temiztelefon)}\n")
            temiz_dosya.write("-" * 30 + "\n")
            for tel in temiztelefon:
                temiz_dosya.write(f"{tel.strip()}\n") 

    except FileNotFoundError:
        print(f" hata '{girisdosyasi}' bulunamadı lütfen dosya adını kontrol edin\n")

if __name__ == "__main__":
    veri_temizle("lvl1_bozuk_veri.txt", "lvl1_temiz_rehber.txt")
    veri_temizle("lvl2_bozuk_veri.txt", "lvl2_temiz_rehber.txt")