from pojistenec import Pojistenec
from pojisteni import Pojistenci

class Menu:
    def __init__(self):
        self.pojistenci = Pojistenci()
        self.volby = {
            "1": self.pojistenci.pridej_pojistence,
            "2": self.pojistenci.seznam_pojistencu,
            "3": self.pojistenci.najdi_pojistence,
            "4": self.konec
        }

    def konec(self):
        exit()

    def zobraz_menu(self):
        print("-----------------------------")
        print("Evidence pojištěných")
        print("-----------------------------")
        print("Vyberte si akci: ")
        print("1: Přidat nového pojištěnce")
        print("2: Vypsat všechny pojistěné")
        print("3: Vyhledat pojištěného")
        print("4: Konec")

    def run(self):
        while True:
            self.zobraz_menu()
            volba = input("Zadejte možnost: ")
            akce = self.volby.get(volba)
            if akce:
                if akce == self.pojistenci.pridej_pojistence:
                    self.pojistenci.pridej_pojistence()
                elif akce == self.pojistenci.seznam_pojistencu:
                    self.pojistenci.seznam_pojistencu()
                elif akce == self.pojistenci.najdi_pojistence:
                    jmeno = input("Zadejte jméno: ")
                    prijmeni = input("Zadejte příjmení: ")
                    pojistenec = akce(jmeno, prijmeni)
                    if pojistenec:
                        print(pojistenec)
                    else:
                        print(f"Pojištěnce {jmeno} {prijmeni} neevidujeme.")
                elif akce == self.konec:
                    break
                else:
                    print("Neplatná volba. Zkuste to znovu.")
            else:
                print("Neplatná volba. Zkuste to znovu.")



