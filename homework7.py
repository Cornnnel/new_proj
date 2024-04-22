# Aceasta este sarcina pentru lecția 7 legată de comentarii, continuarea liniilor și instrucțiuni condiționale.

# Creați o variabilă numită number și atribuiți-i o valoare întreagă.

# CODUL TĂU VINE MAI JOS:
number = 10
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este pozitiv și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number > 0:
    print("este un numar pozitiv")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este par și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number % 2 == 0:
    print("este numar par")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este impar și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number % 2 != 0:
    print("este numar impar")
# CODUL TĂU VINE MAI SUS:

# Creați o variabilă text și atribuiți-i un șir de caractere.

# CODUL TĂU VINE MAI JOS:
text = "hello world"
# CODUL TĂU VINE MAI SUS:
'''
Folosind o instrucțiune condițională, verificați dacă textul
conține cuvântul "Python" și afișați un mesaj corespunzător.
'''

# CODUL TĂU VINE MAI JOS:
if "phyton" in text:
    print("a fost gasit")
else:
    print("nu a fost")
# CODUL TĂU VINE MAI SUS:

''' Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul
 "Java" și afișați un mesaj corespunzător.
'''

# CODUL TĂU VINE MAI JOS:
if "java" in text:
    print("a fost gasit")
else:
    print("nu a fost")
# CODUL TĂU VINE MAI SUS:

''' Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați
un mesaj corespunzător.
# în cazul în care nu conține, verificați dacă conține cuvântul "Java" și afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.
'''
# CODUL TĂU VINE MAI JOS:
if "phyton" in text:
    print("a fost gasit phyton")
elif "java" in text:
    print("a fost gasit java")
else:
    print("nu a fost gasit nimic")

# CODUL TĂU VINE MAI SUS:

'''
# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și cuvântul
"Java" și afișați un mesaj corespunzător.
# În cazul în care conține doar unul dintre ele, afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.
'''
# CODUL TĂU VINE MAI JOS:
if "Python" in text and "Java" in text:
    print("Textul conține atât 'Python' cât și 'Java'.")
elif "Python" in text:
    print("Textul conține 'Python', dar nu și 'Java'.")
elif "Java" in text:
    print("Textul conține 'Java', dar nu și 'Python'.")
else:
    print("Textul nu conține nici 'Python', nici 'Java'.")
# CODUL TĂU VINE MAI SUS:

# Extrageți de la tastatură utilizând funcția input un număr de la 1 la 5 și atribuiți-l variabilei number.
# Folosiți o instrucțiune condițională pentru a printa un mesaj corespunzător în funcție de numărul introdus.
# pentru 1 - printați "Unu"
# pentru 2 - printați "Doi"
# pentru 3 - printați "Trei"
# pentru 4 - printați "Patru"
# pentru 5 - printați "Cinci"

# CODUL TĂU VINE MAI JOS:
number = input("introduceti un numar intreg")
number = int(number)
if number == 1:
    print("Unu")
elif number == 2:
    print("doi")
elif number == 3:
    print("trei")
elif number == 4:
    print("patru")
elif number == 5:
    print("cinci")
else:
    print("numarul nu este intre 1 si 5")

# CODUL TĂU VINE MAI SUS
