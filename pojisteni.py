from pojistenec import Pojistenec


class Pojistenci:
    def __init__(self):
        self.pojistenci = {}

    def pridej_pojistence(self):
        jmeno = input("Zadejte jméno pojištěného: ")
        prijmeni = input("Zadejte příjmení: ")
        telefon = input("Zadejte telefonní číslo: ")
        vek = int(input("Zadejte věk: "))

        klic = jmeno + ' ' + prijmeni
        pojistenec = Pojistenec(jmeno, prijmeni, telefon, vek)
        self.pojistenci[klic] = pojistenec
        print(f"{jmeno} {prijmeni} byl přidán do seznamu pojištěnců.")

    def seznam_pojistencu(self):
        for klic in self.pojistenci:
            print(self.pojistenci[klic])

    def najdi_pojistence(self, jmeno: str, prijmeni: str):
        klic = jmeno + " " + prijmeni
        pojistenec = self.pojistenci.get(klic)
        if pojistenec:
            return pojistenec
        else:
            return None

