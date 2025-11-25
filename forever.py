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
