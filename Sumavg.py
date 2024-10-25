def citeste_numere():
    numere = input("Introduceți numerele separate prin spațiu: ")
    return list(map(int, numere.split()))

def calculeaza_suma(lista_numere):
    return sum(lista_numere)

def calculeaza_media(lista_numere):
    return calculeaza_suma(lista_numere) / len(lista_numere) if lista_numere else 0

lista_numere = citeste_numere()
suma_numere = calculeaza_suma(lista_numere)
media_numere = calculeaza_media(lista_numere)

print("Suma numerelor este:", suma_numere)
print("Media numerelor este:", media_numere)
