x = 12
y = 0

# deklaracja dwóch różnych wyjątkow
try:
    print(x + "!")
    print(x/y)
    print("Linijka po")
except ZeroDivisionError:
    print("Nastąpiło dzielenie przez zero")
except TypeError:
    print("Błąd typow danych")

print("Dalsze instrukcje...\n")

#scalenie dwóch wyjątkow w jeden
try:
    print( x + "!")
    print(x/y)
except (ZeroDivisionError, TypeError):
    print("WYSTĄPIŁ JEDEN Z DWÓCH BŁEDÓW")

#przechwytywanie wszystkich możliwych wyjątków
try:
    lista = []
    print(lista[0])
except:
    print("Błąd")

#Blok finally
try:
    lista = []
    print(lista[1])
except:
    print("Błąd!!")
finally:
    print("Czy bedzie wyjątek czy nie ten blok się wykona")

