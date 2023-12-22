class Den:
    def __init__(self, nazev, hodiny=None):
        self.nazev = nazev
        self.hodiny = hodiny if hodiny else []

    def pridej_hodinu(self, hodina):
        self.hodiny.append(hodina)

    def __repr__(self):
        return f"Den(nazev='{self.nazev}', hodiny={self.hodiny})"

    def __eq__(self, other):
        if not isinstance(other, Den):
            return False
        return self.nazev == other.nazev and self.hodiny == other.hodiny

    def __hash__(self):
        return hash((self.nazev, tuple(self.hodiny)))
