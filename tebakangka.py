import random

def main():
    print("tebak satu angka antara 1 sampai 100")

    angkaacak = random.randint(1, 100)

    skor = 100

    ketemu = False

    while not ketemu:
        tebak = input("tebakkan mu: ")
        tebak = int(tebak)

        if tebak == angkaacak:
            print("tebakan mu benar !!!")
            ketemu = True
        elif tebak > angkaacak:
            print("terlalu besar")
            skor -= 3
        else:
            print("terlalu kecil")
            skor -= 4

    print("skor kamu : ", skor)
    print("terima kasih sudah bermain :)")

if __name__ == "__main__":
    main()
