print("=== mini proje ===")

def veri_filtresi(*kisiler, **ayarlar):
    min_yas = ayarlar.get("min_yas", 20)
    baslangic_harfi = ayarlar.get("baslangic_harfi", "a")
    baslangic_harfi = baslangic_harfi.lower()

    buyuk_yaslilar = []
    harfle_baslayanlar = []

    for kisi in kisiler:
        if kisi["yas"] > min_yas:
            buyuk_yaslilar.append(kisi)

    for kisi in kisiler:
        isim_kucuk_harf = kisi["isim"].lower()
        if isim_kucuk_harf.startswith(baslangic_harfi):
            harfle_baslayanlar.append(kisi)

    return buyuk_yaslilar, harfle_baslayanlar


yas_girisi = input("yaş sınırı girin = ")
harf_girisi = input("başlangıç harfi girin = ")

ayarlar = {}

if yas_girisi != "":
    ayarlar["min_yas"] = int(yas_girisi)

if harf_girisi != "":
    ayarlar["baslangic_harfi"] = harf_girisi


kisiler_listesi = [
    {"isim": "Ahmet", "yas": 22},
    {"isim": "Ömer", "yas": 56},
    {"isim": "Faruk", "yas": 19},
    {"isim": "ege", "yas": 17},
    {"isim": "Nur", "yas": 6},
    {"isim": "Okan", "yas": 41},
    {"isim": "Arda", "yas": 39},
    {"isim": "aylin", "yas": 12},
    {"isim": "atakan", "yas": 26},
    {"isim": "Ayşe", "yas": 21},
    {"isim": "Ali", "yas": 28},
    {"isim": "Zeynep", "yas": 18},
    {"isim": "aslı", "yas": 24},
    {"isim": "Mert", "yas": 20},
    {"isim": "Alper", "yas": 33},
    {"isim": "Buse", "yas": 27},
    {"isim": "arda", "yas": 14},
    {"isim": "Ece", "yas": 23},
    {"isim": "Aybüke", "yas": 97},
    {"isim": "abi bu ödevlerin hepsine teker teker bakıyor musunuz", "yas": 100}
]

buyuk_yaslilar, harfle_baslayanlar = veri_filtresi(
    *kisiler_listesi,
    **ayarlar
)

kullanilan_yas = ayarlar.get("min_yas", 20)
kullanilan_harf = ayarlar.get("baslangic_harfi", "a")
kullanilan_harf = kullanilan_harf.lower()

buyuk_yaslilar_kisa = [
    kisi
    for kisi in kisiler_listesi
    if kisi["yas"] > kullanilan_yas
]

harfle_baslayanlar_kisa = [
    kisi
    for kisi in kisiler_listesi
    if kisi["isim"].lower().startswith(kullanilan_harf)
]

print("\nkullanılan yaş sınırı =", kullanilan_yas)
print("kullanılan başlangıç harfi =", kullanilan_harf)

print("\nyaşı sınırdan büyük kişiler =")
for kisi in buyuk_yaslilar:
    print("isim =", kisi["isim"], ", yaş =", kisi["yas"])

print("\n" + kullanilan_harf + " harfi ile başlayan kişiler =")
for kisi in harfle_baslayanlar:
    print("isim =", kisi["isim"], ", yaş =", kisi["yas"])

print("\ntoplam yaş filtresine uyan kişi sayısı =", len(buyuk_yaslilar))
print("toplam harf filtresine uyan kişi sayısı =", len(harfle_baslayanlar))