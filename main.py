num1 = float(input("Podaj pierwszą liczbę: "))
num2 = float(input("Podaj drugą liczbę: "))

akcja = input("Jaką operację chcesz wykonać?:\n"
              "1. Dodawanie\n"
              "2. Odejmowanie\n"
              "3. Mnożenie\n"
              "4. Dzielenie\n")

if akcja == "1":
    print("Wynik dodawania: ",num1 + num2)

elif akcja == "2":
    print("\nWynik odejmowania: ",num1 - num2)

elif akcja == "3":
    print("\nWynik mnożenia: ",num1 * num2)

elif akcja == "4":
    print("\nWynik dzielenia: ",num1 / num2)