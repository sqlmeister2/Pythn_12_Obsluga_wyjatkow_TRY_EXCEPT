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

print("---")
# mimo bledu print(x/0) x = 4 sie przypisało, bo wykonała się klauzula finally
# czyli wszystko do linii błedu sie wykona, a nie cofa
try:
    x = 4
    print(f'Przed {str(x)}')
    print(x/0)
    x = 5
except:
    print("Błąd dzielenia")
finally:
    print(x)   

# dla powyższego przykładu obejście z wykorzytsaniem funkcji, aby nie wykonywac częsci kodu przed błedem
def wykonaj_kod():
    # Jeśli cała funkcja wykona się bez błędów, zwróci wartość końcową dla x
    x = 4
    print(f'Przed {str(x)}')
    print(x / 0)  # Tu wystąpi błąd
    x = 5
    return x  # Zwraca końcową wartość

x = None
try:
    x = wykonaj_kod()  # Przypisanie tylko, jeśli funkcja wykona się bez błędów
except:
    print("Błąd dzielenia")
finally:
    print(f"Wartość x: {x}")

# Taka konstrukacja wyrzuci błąd braku przypisania s, ponieważ nie wykonało
# się to po wystapienu błędu dzielelnia
try:
    print(4/0)
    s = 5
except:
    print("Błąd dzielenia")

print(s)   