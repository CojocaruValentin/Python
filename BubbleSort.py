def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

numere = input("Introduceți numerele separate prin spațiu: ")
lista_numere = list(map(int, numere.split()))

bubble_sort(lista_numere)

print("Lista sortată este:", lista_numere)
