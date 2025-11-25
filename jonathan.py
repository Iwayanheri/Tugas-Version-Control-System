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
