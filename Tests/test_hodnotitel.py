import unittest
from Services.Hodnotitel import vyhodnot_rozvrh
from DataModels.Hodina import Hodina

class TestHodnotitel(unittest.TestCase):
    """
        Třída TestHodnotitel pro testování funkčnosti hodnotícího systému rozvrhů.

        Metody:
        test_skore_za_cviceni_vedle_sebe: Testuje, zda systém správně přidá skóre, když jsou dva cvičení stejného předmětu vedle sebe.
        test_skore_za_nezadouci_predmety: Testuje, zda systém správně odečte skóre, když jsou nežádoucí předměty umístěny na 9. a 10. hodinu.
        test_skore_za_prvni_hodinu: Testuje, zda systém správně odečte skóre, když nežádoucí předměty jsou na první hodině.
        """
    def test_skore_za_cviceni_vedle_sebe(self):
        """
        Testuje, zda systém přidá 5 bodů, když jsou dvě cvičení stejného předmětu vedle sebe.
        """
        rozvrh = {
            "Pondělí": [Hodina("CIT", "cvičení", "ucitel", "ucebna", 0), Hodina("CIT", "cvičení", "ucitel", "ucebna", 0)] + [Hodina("Volno", None, None, None, 0)] * 8,
            "Úterý": [Hodina("Volno", None, None, None, 0)] * 10,
            "Středa": [Hodina("Volno", None, None, None, 0)] * 10,
            "Čtvrtek": [Hodina("Volno", None, None, None, 0)] * 10,
            "Pátek": [Hodina("Volno", None, None, None, 0)] * 10,
        }
        skore = vyhodnot_rozvrh(rozvrh)
        self.assertEqual(skore, 5)

    def test_skore_za_nezadouci_predmety(self):
        """
        Testuje, zda systém správně odečte 10 bodů, když jsou nežádoucí předměty na 9. a 10. hodině.
        """
        rozvrh = {
            "Pondělí": [Hodina("Volno", None, None, None, 0)] * 8 + [Hodina("M", "teorie", "ucitel", "ucebna", 0), Hodina("C", "teorie", "ucitel", "ucebna", 0)],
            "Úterý": [Hodina("Volno", None, None, None, 0)] * 10,
            "Středa": [Hodina("Volno", None, None, None, 0)] * 10,
            "Čtvrtek": [Hodina("Volno", None, None, None, 0)] * 10,
            "Pátek": [Hodina("Volno", None, None, None, 0)] * 10,
        }
        skore = vyhodnot_rozvrh(rozvrh)
        self.assertEqual(skore, -10)

    def test_skore_za_prvni_hodinu(self):
        """
        Testuje, zda systém správně odečte 1 bod, když je nežádoucí předmět jako první hodina.
        """
        rozvrh = {
            "Pondělí": [Hodina("AM", "teorie", "ucitel", "ucebna", 0)] + [Hodina("Volno", None, None, None, 0)] * 9,
            "Úterý": [Hodina("Volno", None, None, None, 0)] * 10,
            "Středa": [Hodina("Volno", None, None, None, 0)] * 10,
            "Čtvrtek": [Hodina("Volno", None, None, None, 0)] * 10,
            "Pátek": [Hodina("Volno", None, None, None, 0)] * 10,
        }
        skore = vyhodnot_rozvrh(rozvrh)
        self.assertEqual(skore, -1)



if __name__ == '__main__':
    unittest.main()
