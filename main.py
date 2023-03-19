import sys
import ctypes

a = 300
b = 300
print(a)
print(id(a))
print(b)
print(id(b))

a = "cos"

sys.getrefcount(a)
print(sys.getrefcount(a))
print(ctypes.c_long.from_address(id(a)).value)

# zadanie1

zmienna1 = "Python 2023"
zmienna2 = "Python 2023"
zmienna3 = "Python 2023"

print(zmienna1 == zmienna2)
print(zmienna3 == zmienna2)

print("Zmienna 1: ", type(zmienna1), hex(id(zmienna1)))
print("Zmienna 2: ", type(zmienna2), hex(id(zmienna2)))
print("Zmienna 3: ", type(zmienna3), hex(id(zmienna3)))
zmienna3 = "Java 11"

print(zmienna1 == zmienna2)
print(zmienna3 == zmienna2)

print("Zmienna 1: ", type(zmienna1), hex(id(zmienna1)))
print("Zmienna 2: ", type(zmienna2), hex(id(zmienna2)))
print("Zmienna 3: ", type(zmienna3), hex(id(zmienna3)))

# zadanie2
liczba1 = input("Podaj pierwszą liczbę: ")
liczba2 = input("Podaj drugą liczbę: ")
operator = input("Podaj operator: ")

if (operator == '+'):
    print((int)(liczba2) + (int)(liczba1))
elif (operator == '-'):
    print((int)(liczba1) - (int)(liczba2))
elif (operator == '*'):
    print((int)(liczba2) * (int)(liczba1))
elif (operator == '/'):
    print((int)(liczba1) / (int)(liczba2))
elif (operator == '%'):
    print((int)(liczba1) % (int)(liczba2))
else:
    print("Brak")

# zadanie3
print("Jak masz na imię oraz nazwisko?")
odpowiedz1 = input()

print("W jakich okolicznościach czytasz książki najczęściej?")
print("Podczas podróży-wpisz 1")
print("W czasie wolnym-wpisz 2")
print("Nie czytam-wpisz 3")
odpwiedz2 = input()

print("Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?")
print("To moje hobby-wpisz 1")
print("Relaksuje mnie-wpisz 2")
print("Chęć poszerzenia wiedzy-wpisz 3")
odpwoiedz3 = input()

print("Po książki w jakiej formie sięgasz najczęściej?")
print("Papierowej-wpisz 1")
print("E-book na tablecie/telefonie-wpisz 2")
print("E-book na komputerze-wpisz 3")
odpiowiedz4 = input()

print("Ile książek czytasz średnio w ciągu roku? ")
print("0-wpisz 1")
print("żadnej w całości jedynie fragmenty-wpisz 2")
print("2-3 lub wiecej -wpisz 3")
odpiowiedz5 = input()

print("Jak często średnio czytasz książki?")
print("Codziennie-wpisz 1")
print("Raz w tygodniu-wpisz 2")
print("raz na miesiac-wpisz 3")
print("raz na kilka miesiecy -wpisz 4")
print("wcale-wpisz 5")
odpowiedz6 = input()

print("Po jakie gatunki książek sięgasz najczęściej?")
print("Kryminał/Thriller/horror-wpisz 1")
print("Fantastyka-wpisz 2")
print("Przygodowe-wpisz 3")
print("Romanse -wpisz 4")
print("Historyczne-wpisz 5")
odpowiedz7 = input()

print("W jakim języku książki czytasz?")
print("Polskim-wpisz 1")
print("Angielskim-wpisz 2")
print("Niemieckim-wpisz 3")
print("Francuskim -wpisz 4")
odpowiedz8 = input()

print("Jak często wypożyczasz książki w bibliotece?")
print("nigdy-wpisz 1")
print("raz w roku-wpisz 2")
print("raz na tydzien-wpisz 3")
print("raz na miesiac -wpisz 4")


print("Dziękujęmy za udzielnie odpowiedzi!")