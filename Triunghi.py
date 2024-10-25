def este_triunghi(a, b, c):
    return a > 0 and b > 0 and c > 0 and (a + b + c == 180)

unghi1 = int(input("Introduceți primul unghi: "))
unghi2 = int(input("Introduceți al doilea unghi: "))
unghi3 = int(input("Introduceți al treilea unghi: "))

if este_triunghi(unghi1, unghi2, unghi3):
    print("Unghiurile pot forma un triunghi.")
else:
    print("Unghiurile nu pot forma un triunghi.")
