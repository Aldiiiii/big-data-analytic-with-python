x = 10
y = 3.14
name = "Fualan"
is_ok = True

print(x)
print(y)
print(name)
print(is_ok)


# Array di python ada beberapa macam
# cari tahu sendiri aja 
fruits = ["apple", "orange", "papaya"]
for buah in fruits:
    print(buah)

print("ambil satu buah pertama : ", fruits[0])

print("ambil buah dengan keranjangnya : ", fruits[:1])
print("ambil beberapa buah dengan keranjangnya : ", fruits[0:2])

# Membuat List
fruits.append("campedak")

print(fruits)

# menambahkan element di index tertentu

fruits.insert(1, "anggur")

print(fruits)

# hapus pakai remove() atau pop()

fruits.remove("papaya")
# kalau pop() pakai index
removed_fruit =  fruits.pop(0)
print(fruits)
# f string
print(f'Buah yang dihapus: {removed_fruit}')

# mengiterasi list

