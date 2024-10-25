def este_prim(numar):
    if numar <= 1:
        return False
    for i in range(2, int(numar ** 0.5) + 1):
        if numar % i == 0:
            return False
    return True

numar = int(input("Introduceți un număr: "))

if este_prim(numar):
    print("Numărul este prim.")
else:
    print("Numărul nu este prim.")7