import random
import string
# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
lista = [x for x in range(1, 11)]

# lista = []
#
# for i in range(1, 11):
#     if i % 2 == 0:
#         lista.append(i)

# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
# lista_2 = [x for x in lista if x % 2 == 0]
# print(lista)

[print(x) for x in lista if x % 2 == 0]

# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1
# și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i: int = 1
while i <= 5:
    print(i)
    i += 1
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age'
# și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
person = {'name': "john", 'age': 25, 'city': "New York"}
for key, value in person.items():
    print(key, value)

# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
liste = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
         ]
for item in liste:
    print(item)
# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range()
# și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
[print(x) for x in range(1, 11)]
# for x in range(1,11):
#     print(x)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
for index, value in enumerate(person):
    print(f"index {index}, value {value}")

# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
for item1, item2 in zip(lista, liste):
    print(f"item1: {item1}, item2: {item2}")
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
numbers = [x for x in range(1, 11)]
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
# while(i <= 50):


while numbers[0] <= 50:
    numbers = [i * 2 for i in numbers]
    print(numbers[0])

# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
perfect_squares = []

for num in range(1, 101):
    if (num ** 0.5).is_integer():
        perfect_squares.append(num)

print(perfect_squares)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
tabla_inmultirii = []
i = 1
while i <= 10:
    tabla_inmultirii.append(i * 7)
    i += 1
print(tabla_inmultirii)
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi
# (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
pairs_list = []
i = 1
for i in range(1, 6):
    sub_list = []
    for j in range(1, 6):
        sub_list.append((i, j))
    pairs_list.append(sub_list)

for sub_list in pairs_list:
    print(sub_list)
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
for i in range(len(pairs_list)):
    for j in range(len(pairs_list[i])):
        if i < j:
            print(pairs_list[i][j], end=' ')
print("\n")

# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare
# care este mai mare decât 10 dintr-o listă cu numere random creată de tine.
# Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
numb = [random.randint(1, 20) for _ in range(10)]
found = False
i = 0

while i < len(numb):
    if numb[i] > 10:
        print(f"Prima valoare mai mare decit zice este: {numb[i]}")
        found = True
        break
    i += 1

if not found:
    print(" Nu este gasita o valoare mai mare ca 10")
# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele (*) folosind bucle încadrate.
# Dimensiunea pătratului va fi citită de la utilizator.

# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
n = int(input("Introduceti marimea patratului"))
for i in range(n):
    for j in range(n):
        print("*", end=' ')
    print()
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
for i in range(1, 7):
    for j in range(1, i + 1):
        print(j, end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
for i in range(5, 0, -1):
    for j in range(5, 5 - i, -1):
        print(j, end="")
    print()  # trecere la o nouă linie

# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:

letters = string.ascii_lowercase[:7]
for i in range(len(letters)):
    print(letters[i:])

# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
for i in range(8):
    if i % 2 == 0:
        print('+-' * 7 + '+')
    else:
        print('-+' * 7 + '-')

# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:


powers_of_three = [3**i for i in range(1, 6)]

for start in range(len(powers_of_three) + 1):
    for num in powers_of_three[:start]:
        print(num, end=' ')
    print()

for end in range(1, len(powers_of_three)):
    for num in powers_of_three[end:]:
        print(num, end=' ')
    print()

# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.
