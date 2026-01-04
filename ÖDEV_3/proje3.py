from proje2 import sifrekontrol

def test_dogru():
    assert sifrekontrol("Omer1234.!") == True

def test_kisa():
    sonuc = sifrekontrol("Omer:1")
    assert sonuc != True
    assert "kısa" in sonuc

def test_rakamsiz():
    sonuc = sifrekontrol("Omerfaruk@")
    assert sonuc != True
    assert "rakam" in sonuc

def test_hatali_sifre_buyukharfsiz():
    sonuc = sifrekontrol("omer1234.")
    assert sonuc != True
    assert "büyük harf" in sonuc