class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        
        super().__init__(szobaszam, 5000)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 8000)

class Szalloda:
    def __init__(self, nev, szobak):
        self.nev = nev
        self.szobak = szobak

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum