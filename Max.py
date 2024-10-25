numere = input("Introduceți numerele separate prin spațiu: ")
lista_numere = list(map(int, numere.split()))

maxim = max(lista_numere)
print("Valoarea maximă este:", maxim)
