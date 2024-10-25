def CMMDC():

    import math

    numar1 = int(input("Introduceți primul număr: "))
    numar2 = int(input("Introduceți al doilea număr: "))

    rezultat = math.gcd(numar1, numar2)
    print("Cel mai mare divizor comun este:", rezultat)

CMMDC()
