import random
import json

NAZWA_PLIKU_SLOWA = "trudne_slowa.json"
NAZWA_PLIKU_DEFINICJE = "trudne_slowa_definicje.json"

# Funkcja wczytywania słów z pliku
def wczytaj_slowa():
    try:
        with open(NAZWA_PLIKU_SLOWA, "r", encoding="utf-8") as f:
            slownik_slow = json.load(f)
            return list(slownik_slow.values())
    except FileNotFoundError:
        return []

# Funkcja wczytywania definicji z pliku
def wczytaj_definicje():
    try:
        with open(NAZWA_PLIKU_DEFINICJE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Funkcja zapisywania słów do pliku
def zapisz_slowa(slowa):
    slownik_slow = {i+1: slowo for i, slowo in enumerate(slowa)}
    with open(NAZWA_PLIKU_SLOWA, "w", encoding="utf-8") as f:
        json.dump(slownik_slow, f, ensure_ascii=False)

# Funkcja zapisywania definicji do pliku
def zapisz_definicje(definicje):
    with open(NAZWA_PLIKU_DEFINICJE, "w", encoding="utf-8") as f:
        json.dump(definicje, f, ensure_ascii=False)

# Wczytaj słowa i definicje przy starcie programu
trudne_slowa = wczytaj_slowa()
trudne_slowa_definicje = wczytaj_definicje()

while True:
    losowe_slowo = random.choice(trudne_slowa)
    dlugosc = len(losowe_slowo)

    print(f"Słowo: {losowe_slowo} ({dlugosc} liter)")

    # Zapytanie o definicję
    decyzja_definicja = input("Czy chcesz zobaczyć definicję? (t/n): ")
    if decyzja_definicja.lower() == 't':
        if losowe_slowo in trudne_slowa_definicje:
            print(f"Definicja: {trudne_slowa_definicje[losowe_slowo]}")
        else:
            print("Definicja dla tego słowa nie jest dostępna.")

    # Zapytanie o dodanie nowego słowa
    decyzja_slowo = input("Czy chcesz dodać własne słowo? (t/n/k): ")

    if decyzja_slowo.lower() == 't':
        while True:
            nowe_slowo = input("Podaj nowe słowo (minimum 12 liter): ")
            if len(nowe_slowo) >= 12:
                definicja = input("Podaj krótką definicję (minimum 50 znaków): ")
                if len(definicja) >= 50:
                    trudne_slowa.append(nowe_slowo)
                    trudne_slowa_definicje[nowe_slowo] = definicja
                    zapisz_slowa(trudne_slowa)
                    zapisz_definicje(trudne_slowa_definicje)
                    print("Słowo i definicja dodane!")
                    break
                else:
                    print("Definicja musi mieć co najmniej 50 znaków. Spróbuj ponownie.")
            else:
                print("Słowo musi mieć co najmniej 12 liter. Spróbuj ponownie.")

    elif decyzja_slowo.lower() == 'k':
        print("Zakończono działanie programu.")
        break
