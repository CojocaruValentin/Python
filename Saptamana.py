def ziua_saptamanii(numar):
    zile = {
        1: "Luni",
        2: "Marți",
        3: "Miercuri",
        4: "Joi",
        5: "Vineri",
        6: "Sâmbătă",
        7: "Duminică"
    }
    return zile.get(numar, "Număr invalid! Introduceți un număr între 1 și 7.")

numar = int(input("Introduceți un număr de la 1 la 7: "))

print("Ziua săptămânii este:", ziua_saptamanii(numar))
