print("=== sözlük örneği ===")

kisi = {
    "isim": "ömer",
    "soyisim": "okuşluk",
    "yas": 20,
    "bolum": "bilgisayar mühendisliği"
}

print("kişi bilgileri =", kisi)

print("isim =", kisi["isim"])
print("soyisim =", kisi["soyisim"])
print("yaş =", kisi["yas"])
print("bölüm =", kisi["bolum"])

kisi["sehir"] = "istanbul"
print("güncel kişi bilgileri =", kisi)
print("şehir =", kisi["sehir"])

kisi["yas"] = 21

print("yaşı güncellenmiş kişi bilgileri =", kisi)
print("yeni yaş =", kisi["yas"])