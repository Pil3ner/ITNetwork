class Pojistenec:
    def __init__(self, jmeno: str, prijmeni: str, telefon: str, vek: int):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, Věk: {self.vek}, Telefon: {self.telefon}"