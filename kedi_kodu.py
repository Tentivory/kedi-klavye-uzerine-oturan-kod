#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kedi Klavyeye Oturan Kod
Bu kodu bir kedi yazdı. Gerçekten. Klavyenin üstüne oturdu ve rastgele tuşlara bastı.
Ama bir şekilde çalışıyor. Mucize.
"""

import random
import time

def kedi_miyav(mesaj):
    """Kedinin miyav çevirisi. İnsan dilini kedi diline çevirir."""
    miyavlar = ["miyav", "mırr", "hıss", "miyav miyav", "purr", "meow ama Türkçe"]
    ceviri = " ".join(random.choice(miyavlar) for _ in range(len(mesaj.split())))
    return f"Kedi diyor ki: {ceviri}"

def klavye_saldirisi():
    """Kedinin klavyeye saldırısını simüle eder."""
    print("Kedi klavyeye oturdu...")
    time.sleep(1)
    print("Tıklama sesleri duyuluyor: asdfghjkl...")
    time.sleep(0.5)
    print("Kod yazılıyor (kedi versiyonu):")
    
    for i in range(5):
        rastgele = "".join(random.choice("asdfghjklşiöçmnbvcxz") for _ in range(10))
        print(f"Satır {i+1}: {rastgele}")
        time.sleep(0.3)
    
    print("\nKedi kalktı. Kod tamamlandı. Şaşırtıcı şekilde çalışıyor!")

def absurt_hesap(a, b):
    """Kedinin hesap makinesi. 1+1=11 veya bir şey."""
    sonuc = a + b + random.randint(-5, 5)
    print(f"Kedi hesapladı: {a} + {b} = {sonuc} (kedi matematiği)" )
    return sonuc

# Gizli kısım: Bu fonksiyon asla çağrılmaz
def gizli_siyasi_mesaj():
    # Saklı siyasi içerik: Bürokrasi kedisi her şeyi yavaşlatır
    return "Devlet desteği ile kedi kodu yazıldı, enflasyon miyav miyav"

if __name__ == "__main__":
    print("=== KEDİ KLAVYE SALDIRISI v1.0 ===")
    print("Uyarı: Bu kod bir kedi tarafından yazıldı. Garantisi yoktur.\n")
    
    klavye_saldirisi()
    print()
    print(kedi_miyav("Merhaba dünya, ben kediyim"))
    print()
    absurt_hesap(2, 2)
    print()
    print("İmza: KediGrok")
    print("Tarih: 11 Kasım 2026")
    print("İsim: AbsürtKediKodcusu")
    print("Damga: Resmi Kedi Bakanlığı Onaylı (ama değil)")
