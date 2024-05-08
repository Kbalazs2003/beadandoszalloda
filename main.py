import datetime
from fuggvenyek import foglalas, listazas, lemondas
from osztalyok import EgyagyasSzoba, Foglalas, KetagyasSzoba, Szalloda


def main():

    # Szálloda és szobák inicializálása
    szalloda = Szalloda(
        "Teszt Szálloda", 
        [
            EgyagyasSzoba("101"), 
            EgyagyasSzoba("102"), 
            KetagyasSzoba("201")
        ]
    )
    
    # Teszt foglalások inicializálása
    foglalasok = [
        Foglalas(szalloda.szobak[0], datetime.date(2024, 5, 15)),
        Foglalas(szalloda.szobak[2], datetime.date(2024, 5, 18)),
        Foglalas(szalloda.szobak[1], datetime.date(2024, 5, 20)),
        Foglalas(szalloda.szobak[0], datetime.date(2024, 5, 25)),
        Foglalas(szalloda.szobak[2], datetime.date(2024, 5, 30))
    ]


    while True:
        print("\nVálasszon egy műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Művelet kiválasztása (1/2/3/4): ")

        if valasztas == '1':

            szobaszam = input("Adja meg a foglalni kívánt szoba számát: ")
            datum = input("Adja meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            try:
                datum = datetime.datetime.strptime(datum, "%Y-%m-%d").date()
            except ValueError:
                print("Hibás dátum formátum!")
                continue

            if datum < datetime.date.today():
                print("A megadott dátum nem megfelelő! Múltbeli idő megadása nem megengedett!")
                continue

            foglalas(szalloda, szobaszam, datum, foglalasok)

        elif valasztas == '2':

            print("Lemondás menü")
            szobaszam = input("Adja meg a lemondani kívánt szoba számát: ")
            datum = input("Adja meg a lemondás dátumát (YYYY-MM-DD formátumban): ")

            try:
                datum = datetime.datetime.strptime(datum, "%Y-%m-%d").date()
            except ValueError:
                print("Hibás dátum formátum!")
                continue

            lemondas(foglalasok, szobaszam, datum)

        elif valasztas == '3':

            print("Foglalások listázása:")
            listazas(foglalasok)

        elif valasztas == '4':

            print("Kilépés")
            break
    
        else:
            print("Hibás bemenet!")


if __name__ == "__main__":
    main()