a = int(input("Digit A: "))
b = int(input("Digit B: "))

kondisi1 = a >= 5
kondisi2 = b >= 5

print("Kondisi 1:", kondisi1)
print("Kondisi 2:", kondisi2)

print("NOT:", not kondisi1)
print("AND:", kondisi1 and kondisi2)
print("OR :", kondisi1 or kondisi2)
print("XOR:", kondisi1 ^ kondisi2)

# Kondisi 1: 3 >= 5 salah, jadi False.
# Kondisi 2: 4 >= 5 salah, jadi False.
# NOT: not False membalik nilai, jadi True.
# AND: baru True kalau kedua kondisi True. Keduanya False, jadi False.
# OR: True kalau minimal satu kondisi True. Keduanya False, jadi False.
# XOR: True kalau tepat satu kondisi True. Keduanya sama-sama False, jadi False.