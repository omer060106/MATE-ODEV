print("=== normal filtreleme örneği ===")

kisiler = [
    {"isim": "ahmet", "yas": 22},
    {"isim": "ömer", "yas": 56},
    {"isim": "faruk", "yas": 145},
    {"isim": "ege", "yas": 17},
    {"isim": "nur", "yas": 6},
    {"isim": "okusluk", "yas": 41},
    {"isim": "arda", "yas": 39},
    {"isim": "aylin", "yas": 12},
    {"isim": "atakan", "yas": 26},
]

buyuk_yaslilar = []
a_ile_baslayanlar = []

for kisi in kisiler:
    if kisi["yas"] > 20:
        buyuk_yaslilar.append(kisi)

for kisi in kisiler:
    if kisi["isim"].startswith("a"):
        a_ile_baslayanlar.append(kisi)

print("20'den büyük yaşlar =", buyuk_yaslilar)
print("a ile başlayanlar =", a_ile_baslayanlar)

for kisi in buyuk_yaslilar:
    print("isim =", kisi["isim"], ", yaş =", kisi["yas"])

for kisi in a_ile_baslayanlar:
    print("isim =", kisi["isim"], ", yaş =", kisi["yas"])