"""
Rozvrh.py - Definice třídy Rozvrh pro reprezentaci školního rozvrhu.

Tato třída slouží k reprezentaci školního rozvrhu, který obsahuje dny s jejich hodinami.

"""

class Rozvrh:
    def __init__(self, dny=None):
        """
        Inicializační metoda třídy Rozvrh.

        Parametry:
        dny (list): Seznam dnů v rozvrhu. Výchozí hodnota je prázdný seznam.

        """
        self.dny = dny if dny else []

    def pridej_den(self, den):
        """
        Metoda pro přidání dne do rozvrhu.

        Parametry:
        den: Den, který se má přidat do rozvrhu.

        """
        self.dny.append(den)

    def __repr__(self):
        """
        Přetížení metody pro textovou reprezentaci objektu třídy Rozvrh.

        Návratová hodnota:
        str: Textový popis objektu třídy Rozvrh.

        """
        return f"Rozvrh(dny={self.dny})"

    def __eq__(self, other):
        """
        Přetížení metody pro porovnání dvou objektů třídy Rozvrh na rovnost.

        Parametry:
        other (Rozvrh): Druhý objekt třídy Rozvrh, se kterým se porovnává.

        Návratová hodnota:
        bool: True, pokud jsou objekty třídy Rozvrh shodné, jinak False.

        """
        if not isinstance(other, Rozvrh):
            return False
        return self.dny == other.dny

    def __hash__(self):
        """
        Přetížení metody pro výpočet hash hodnoty objektu třídy Rozvrh.

        Návratová hodnota:
        int: Hash hodnota objektu třídy Rozvrh.

        """
        return hash(tuple(self.dny))
