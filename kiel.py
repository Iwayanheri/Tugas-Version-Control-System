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
