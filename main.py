import datetime
#determináns importálása

#szoba osztály létrehozás
class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

#egyágyas szoba osztály létrehopzása
class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 5000)

#kétágyas szoba osztály létrehozása
class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 8000)

#foglalás osztály létrehozása
class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

#száloda osztály létrehozása
class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaadasa(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                for foglalas in self.foglalasok:
                    if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                        return False  # A szoba már foglalt ezen a napon
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return True, szoba.ar  # Sikeres foglalás és az ár visszaadása
        return False, None  # A megadott szoba nem található

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return True  # Sikeres lemondás
        return False  # A foglalás nem található

    def foglalasok_listazasa(self):
        foglalasok = []
        for foglalas in self.foglalasok:
            foglalasok.append({"szobaszam": foglalas.szoba.szobaszam, "datum": foglalas.datum.strftime('%Y-%m-%d')})
        return foglalasok

def main():
    szalloda = Szalloda("Pihenő Szálló")

    szalloda.szoba_hozzaadasa(EgyagyasSzoba("45"))
    szalloda.szoba_hozzaadasa(EgyagyasSzoba("165"))
    szalloda.szoba_hozzaadasa(KetagyasSzoba("209"))

    szalloda.foglalas("45", datetime.date(2024, 5, 10))
    szalloda.foglalas("165", datetime.date(2024, 7, 6))
    szalloda.foglalas("209", datetime.date(2024, 5, 9))
    szalloda.foglalas("170", datetime.date(2024, 8, 8))
    szalloda.foglalas("105", datetime.date(2024, 10, 9))

    print("Üdvözöljük a Pihenő Szálló foglalási rendszerében!")
    while True:
        print("\nVálasszon egy opcíót:")
        print("A. Szoba foglalása")
        print("B. Foglalás lemondása")
        print("C. Foglalások listázása")
        print("D. Kilépés")
        valasztas = input("Adja meg a választott opció betűjelét: ")

        if valasztas == "A":
            szobaszam = input("Adja meg a foglalni kívánt szoba számát: ")
            datum_str = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                datum = datetime.datetime.strptime(datum_str, "%Y-%m-%d").date()
                success, ar = szalloda.foglalas(szobaszam, datum)
                if success:
                    print(f"Sikeres foglalás! Ár: {ar}")
                else:
                    print("Hiba történt a foglalás során vagy a szoba már foglalt ezen a napon.")
            except ValueError:
                print("Hibás dátumformátum! Kérem, adjon meg érvényes dátumot.")

        elif valasztas == "B":
            szobaszam = input("Adja meg a lemondani kívánt foglalás szoba számát: ")
            datum_str = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                datum = datetime.datetime.strptime(datum_str, "%Y-%m-%d").date()
                if szalloda.lemondas(szobaszam, datum):
                    print("Sikeres lemondás!")
                else:
                    print("Nem található ilyen foglalás.")
            except ValueError:
                print("Hibás dátumformátum! Kérem, adjon meg érvényes dátumot.")

        elif valasztas == "C":
            print("Az aktuális foglalások:")
            foglalasok = szalloda.foglalasok_listazasa()
            if foglalasok:
                for foglalas in foglalasok:
                    print(f"Szoba: {foglalas['szobaszam']}, Dátum: {foglalas['datum']}")
            else:
                print("Nincsenek foglalások.")

        elif valasztas == "D":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás! Kérem, válasszon újra.")

if __name__ == "__main__":
    main()