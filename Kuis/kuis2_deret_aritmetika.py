print("Deret Aritmetika")
a = float(input("Suku pertama (a): "))
d = float(input("beda (d): "))
n = int(input("Jumlah suku (n): "))

while n <= 0:
    print("n harus bilangan bulat positif.")
    n = int(input("Jumlah suku (n): "))

total = 0
for i in range(n):
    suku = a + i * d
    total += suku
    print(f"Suku ke-{i + 1}: {suku}")

print(f"Jumlah deret aritmetika: {total}")