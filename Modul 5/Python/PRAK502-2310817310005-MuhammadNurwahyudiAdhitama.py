def mutlak(angka):
    if angka < 0:
        angka *= -1
    return angka

def hitung(nilai1, nilai2):
    hitung = nilai1 - nilai2
    if hitung < 0:
        hitung *= -1
    return hitung

a, c, b, d = map(int, input("").split())

hasil = hitung(a, b) + hitung(c, d)
hasil_mutlak = mutlak(hasil)

print(f"{hasil_mutlak}")
