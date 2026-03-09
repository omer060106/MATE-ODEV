print("=== listede sözlükler örneği ===")

kisiler = [
    {"isim": "ahmet", "yas": 22},
    {"isim": "ömer", "yas": 56},
    {"isim": "faruk", "yas": 145},
    {"isim": "ege", "yas": 24},
    {"isim": "nur", "yas": 6},
    {"isim": "okusluk", "yas": 41},
    {"isim": "arda", "yas": 39},
]

print("tüm kişiler =", kisiler)

for kisi in kisiler:
    print(kisi)

print("büyükler=")
for kisi in kisiler:
  if kisi["yas"] > 40:      
      print("isim =", kisi["isim"])
      print("yaş =", kisi["yas"])
      
print("tüm isimler")
for kisi in kisiler:
    print("isim =", kisi["isim"])