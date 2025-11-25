import random

# Looping program berjalan
while True:

    # memilih level
    level = input("Masukkan level yang anda mau [mudah/medium/sulit/sangat sulit] : ").lower()
    while level not in ["mudah", "medium", "sulit", "sangat sulit"]:
        level = input("\nMaaf inputan anda salah.\nMasukkan level yang anda mau [mudah/medium/sulit/sangat sulit] : ").lower()
    
    # menentukan batas angka dan kesempatan
    if level == "mudah":
        kesempatan = 3
        bilRandom = random.randint(1, 10)

    elif level == "medium":
        kesempatan = 5
        bilRandom = random.randint(1, 20)

    elif level == "sulit":
        kesempatan = 8
        bilRandom = random.randint(1, 50)

    elif level == "sangat sulit":
        kesempatan = 15
        bilRandom = random.randint(1, 100)

    print("Level", level, "dengan kesempatan", kesempatan, "kali")

    # looping tebak angka
    while kesempatan > 0:
        print("Kesempatan :", kesempatan)
        tebak = int(input("Masukkan angka yang ditebak : "))

        if tebak == bilRandom:
            print("Yeay! Berhasil tebak angka", bilRandom, "dengan benar!!")
            break

        elif tebak > bilRandom:
            print("Angkanya di bawah", tebak)

        else:  # tebak < bilRandom
            print("Angkanya di atas", tebak)

        kesempatan -= 1

    # jika kesempatan habis
    if kesempatan == 0 and tebak != bilRandom:
        print("Yah gagal tebak angka... :(")
        print("Jawabannya adalah:", bilRandom)

    # konfirmasi ulang
    ulang = input("Mau main lagi? (y/n): ").lower()
    while ulang not in ["y", "n"]:
        ulang = input("\nMaaf inputan anda salah.\nMau main lagi? (y/n): ").lower()

    if ulang == "y":
        print("\nSilakan main lagi!!\n")
    else:
        print("\nTerima kasih sudah bermain. Sampai jumpa lagi!!\n")
        break

