import unittest
from Services.Generator import generator_rozvrhu
import multiprocessing
import queue

class TestGenerator(unittest.TestCase):
    """
    Třída TestGenerator pro testování funkčnosti generátoru rozvrhů.

    Metody:
    setUp: Příprava prostředí pro každý test.
    test_generator_vytvori_rozvrh: Testuje, zda generátor vytvoří rozvrh.
    test_generator_vytvori_spravny_pocet_hodin: Testuje, zda má každý den v rozvrhu správný počet hodin.
    test_generator_zvysi_pocet_vygenerovanych: Testuje, zda se po vygenerování rozvrhu zvýší celkový počet vygenerovaných rozvrhů.
    """

    def setUp(self):
        """
        Nastaví proměnné a prostředí potřebné pro testy.
        """
        self.queue = multiprocessing.Queue()
        self.terminate_event = multiprocessing.Event()
        self.pocet_vygenerovanych = multiprocessing.Value('i', 0)

    def test_generator_vytvori_rozvrh(self):
        """
        Testuje, zda generátor úspěšně vytvoří rozvrh a umístí jej do fronty.
        """
        generator_rozvrhu(self.queue, self.terminate_event, self.pocet_vygenerovanych)
        self.assertFalse(self.queue.empty())

    def test_generator_vytvori_spravny_pocet_hodin(self):
        """
        Testuje, zda každý den v rozvrhu obsahuje správný počet hodin.
        """
        generator_rozvrhu(self.queue, self.terminate_event, self.pocet_vygenerovanych)
        rozvrh = self.queue.get()
        for den in rozvrh:
            self.assertEqual(len(rozvrh[den]), 10)

    def test_generator_zvysi_pocet_vygenerovanych(self):
        """
        Testuje, zda se po vygenerování nového rozvrhu zvýší počet vygenerovaných rozvrhů.
        """
        pocatecni_pocet = self.pocet_vygenerovanych.value
        generator_rozvrhu(self.queue, self.terminate_event, self.pocet_vygenerovanych)
        self.assertGreater(self.pocet_vygenerovanych.value, pocatecni_pocet)



if __name__ == '__main__':
    unittest.main()
