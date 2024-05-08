from osztalyok import Foglalas, Szalloda


def foglalas(szalloda, szobaszam, datum, foglalasok):

    ar = None
    foglalas = None

    for szoba in szalloda.szobak:
        if szoba.szobaszam == szobaszam:

            for foglalas in foglalasok:

                if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                    print(f"A {szobaszam} számú szoba foglalt a {datum} napon")
                    return None, None
                
            ar = szoba.ar
            foglalas = Foglalas(szoba, datum)
            break
        
    

    if ar != None and foglalas != None:
        megerosites = input(f"A szoba ára: {ar}. Biztosan lefoglalja? (I,N)")

        if megerosites == 'I' or megerosites == 'i':
            foglalasok.append(foglalas)
            print(f"A foglalás sikeres!")
            
        else:
            print("A foglalás visszavonásra került!")
    else:
        print("Nem található ilyen szoba!")

def lemondas(foglalasok, lemondasSzobaszam, lemondasDatum):

    eredmeny = False
    lemondandoFoglalas = None

    for foglalas in foglalasok:
        if foglalas.datum == lemondasDatum and foglalas.szoba.szobaszam == lemondasSzobaszam:
            lemondandoFoglalas = foglalas
            eredmeny = True
        
    if eredmeny:
        megerosites = input(f"Biztosan lemondja a {lemondasSzobaszam} szobaszámú szobát a {lemondasDatum} napra? (I,N)")

        if megerosites == 'I' or megerosites == 'i':
            foglalasok.remove(lemondandoFoglalas)
            print("Sikeres lemondás!")
            
        else:
            print("A lemondás visszavonásra került!")
    else:
        print("Sikeretelen lemondás. Erre napra nem található foglalás a megadott szobára!")


def listazas(foglalasok):
    for foglalas in foglalasok:
        print(f"Szoba szám: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")