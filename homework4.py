# Aceasta este prima ta sarcină a lecției legată de float în python

# Creează o variabilă numită `age` și seteaz-o la vârsta ta

# CODUL TĂU VINE MAI JOS:
age = 18
# CODUL TĂU VINE MAI SUS:

# Acum afișează tipul variabilei `age` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(type(age))
# CODUL TĂU VINE MAI SUS:

# Acum asigură-te că variabila `age` este de tipul float.

# CODUL TĂU VINE MAI JOS:
age = float(age)
print(type(age))
# CODUL TĂU VINE MAI SUS:

# Creează două variabile numite `age2` și `age3` și setează-le la vârsta prietenilor tăi, ambele variabile trebuie să fie de tipul float.

# CODUL TĂU VINE MAI JOS:
age2 = 20.0
age3 = 20.0
# CODUL TĂU VINE MAI SUS:

# Acum afișează suma vârstelor voastre folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age2 + age3)
# CODUL TĂU VINE MAI SUS:

# Acum afișează diferența vârstelor voastre folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age2 - age3)
# CODUL TĂU VINE MAI SUS:

# Acum afișează produsul vârstelor voastre folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age2 * age3)
# CODUL TĂU VINE MAI SUS:

# Acum afișează împărțirea vârstelor voastre folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age2 / age3)
# CODUL TĂU VINE MAI SUS:

# Acum afișează restul împărțirii vârstelor voastre folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age2 % age3)
# CODUL TĂU VINE MAI SUS:

# Acum afișează rezultatul vârstei tale ridicată la puterea vârstei primului prieten folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age ** age2)
# CODUL TĂU VINE MAI SUS:

# Acum afișează rezultatul vârstei primului prieten împărțită la puterea vârstei celui de-al doilea prieten folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age2 / age3)
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot pentru această sarcină

# TTASK 2

# Aceasta este a doua ta sarcină legată a leciei legate de stringuri în python

# Creează o variabilă numită `name` și seteaz-o la numele tău

# CODUL TĂU VINE MAI JOS:
name = 'cornel'
# CODUL TĂU VINE MAI SUS:

# Acum afișează valoarea variabilei `name` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(name)
# CODUL TĂU VINE MAI SUS:

# Acum creează o nouă variabilă numită `name2` și seteaz-o la valoarea variabilei `name` și afișează valoarea variabilei `name2` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
name2=name
print(name2)
# CODUL TĂU VINE MAI SUS:

# Acum printează ultimul caracter al variabilei `name` folosind indexarea

# CODUL TĂU VINE MAI JOS:
print(name2[5:6])
# CODUL TĂU VINE MAI SUS:

# Acum printează primele 3 caractere ale variabilei `name` folosind slicing

# CODUL TĂU VINE MAI JOS:
print(name2[0:3])
# CODUL TĂU VINE MAI SUS:

# Acum printează valoarea variabilei `name` în majuscule folosind metoda `upper`

# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

# Acum printează valoarea variabilei `name` în minuscule folosind metoda `lower`

# CODUL TĂU VINE MAI JOS:
print(name2.lower())
# CODUL TĂU VINE MAI SUS:

# Acum printează concatenarea variabilelor `name` și `name2`

# CODUL TĂU VINE MAI JOS:
print(name + name2)
# CODUL TĂU VINE MAI SUS:

# Creează o variabilă `text` și setează-i un text la alegere, cu restricția ca acesta să conțină mai multe rânduri

# CODUL TĂU VINE MAI JOS:
text= ('lorem ipsum dolor sit\n' 'lorem ipsum dolor')
print(text)
# CODUL TĂU VINE MAI SUS:

# Verifică dacă variabila `text` conține cuvântul `python`

# CODUL TĂU VINE MAI JOS:
print("phyton" in text)
# CODUL TĂU VINE MAI SUS:

# Folosește metoda replace pentru a înlocui litera `a` din variabila `text` cu litera `e`

# CODUL TĂU VINE MAI JOS:
print(text.replace('l','e'))
# CODUL TĂU VINE MAI SUS:

# Folosește metoda split pentru a transforma variabila `text` într-o listă de cuvinte

# CODUL TĂU VINE MAI JOS:
print(text.split())
# CODUL TĂU VINE MAI SUS:

# Creează un f-string care să conțină variabilele `name` și `name2`

# CODUL TĂU VINE MAI JOS:
mesaj=f"Ma numesc {name} si am un prieten {name2}!"
# CODUL TĂU VINE MAI SUS:

# Verifică dacă string-ul creat se termină cu `!`

# CODUL TĂU VINE MAI JOS:
print(mesaj.endswith('!'))
# CODUL TĂU VINE MAI SUS:

# Verifică dacă string-ul creat începe cu `Hello`

# CODUL TĂU VINE MAI JOS:
print('Hello' in mesaj[0:5])
# CODUL TĂU VINE MAI SUS:

# Identifică indexul unde se află `!` în string-ul creat

# CODUL TĂU VINE MAI JOS:
print(mesaj.index('!'))
# CODUL TĂU VINE MAI SUS:

# Identifică indexul unde se află `o` în string-ul creat folosind altă metodă

# CODUL TĂU VINE MAI JOS:
print(mesaj.find('o'))
# CODUL TĂU VINE MAI SUS:

# Utilizând format string-uri, creează un string care să conțină variabilele `name` și `name2`

# CODUL TĂU VINE MAI JOS:
mesaj_2=f"Ma numesc {name} si am un prieten {name2}"
# CODUL TĂU VINE MAI SUS:

# Concatenează string-ul creat cu string-ul `text`

# CODUL TĂU VINE MAI JOS:
print(mesaj + mesaj_2)
# CODUL TĂU VINE MAI SUS:

# Afișează lungimea string-ului creat

# CODUL TĂU VINE MAI JOS:
print(len(mesaj_2))
# CODUL TĂU VINE MAI SUS:

# Aceasta a fost tot pentru această sarcină

# TASK 3

# Aceasta este a treia ta sarcină a lecției legată de type conversion și input-ul user-ului în python

# Creează o variabilă numită `number` și atribuie-i valoarea `10`

# CODUL TĂU VINE MAI JOS:
number = 10
# CODUL TĂU VINE MAI SUS:

# Acum afișează valoarea variabilei `number` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(number)
# CODUL TĂU VINE MAI SUS:

# Acum cere user-ului să introducă un număr și atribuie acea valoare variabilei `number` și afișeaz-o folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
number = int(input("Adauga numarul"))
# CODUL TĂU VINE MAI SUS:

# Acum afișează tipul variabilei `number` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(type(number))
# CODUL TĂU VINE MAI SUS:

# Convertește variabila `number` la tipul `float` și afișează tipul variabilei `number` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
number = float(number)
print(type(number))
# CODUL TĂU VINE MAI SUS:

# Convertește variabila `number` la tipul `str` și afișează tipul variabilei `number` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
number = str(number)
print(type(number))
# CODUL TĂU VINE MAI SUS:

# Convertește variabila `number` la tipul `bool` și afișează tipul variabilei `number` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
number = bool(number)
print(type(number))
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot pentru această sarcină