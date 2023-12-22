"""
Hodina.py - Definice třídy Hodina pro reprezentaci školní hodiny.

Tato třída slouží k reprezentaci jednotlivých školních hodin s různými vlastnostmi, jako jsou předmět, typ hodiny, učitel, učebna a počet hodin.


"""

class Hodina:
    def __init__(self, predmet, typ, ucitel, ucebna, pocet):
        """
        Inicializační metoda třídy Hodina.

        Parametry:
        predmet (str): Název předmětu, který se v hodině vyučuje.
        typ (str): Typ hodiny (např. "přednáška", "cvičení", "seminář").
        ucitel (str): Jméno učitele vyučujícího hodinu.
        ucebna (str): Název učebny, kde se hodina koná.
        pocet (int): Počet hodin daného typu a předmětu v rozvrhu.

        """
        self.predmet = predmet
        self.typ = typ
        self.ucitel = ucitel
        self.ucebna = ucebna
        self.pocet = pocet

    def __repr__(self):
        """
        Přetížení metody pro textovou reprezentaci objektu třídy Hodina.

        Návratová hodnota:
        str: Textový popis objektu třídy Hodina.

        """
        return f"Hodina(predmet='{self.predmet}', typ='{self.typ}', ucitel='{self.ucitel}', ucebna='{self.ucebna}', pocet={self.pocet})"

    def __eq__(self, other):
        """
        Přetížení metody pro porovnání dvou objektů třídy Hodina na rovnost.

        Parametry:
        other (Hodina): Druhý objekt třídy Hodina, se kterým se porovnává.

        Návratová hodnota:
        bool: True, pokud jsou objekty třídy Hodina shodné, jinak False.

        """
        if not isinstance(other, Hodina):
            return False
        return (self.predmet == other.predmet and self.typ == other.typ and
                self.ucitel == other.ucitel and self.ucebna == other.ucebna)

    def __hash__(self):
        """
        Přetížení metody pro výpočet hash hodnoty objektu třídy Hodina.

        Návratová hodnota:
        int: Hash hodnota objektu třídy Hodina.

        """
        return hash((self.predmet, self.typ, self.ucitel, self.ucebna))
