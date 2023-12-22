"""
Generator.py - Generátor náhodných rozvrhů na základě kombinací hodin.

Tento skript umožňuje generovat náhodné rozvrhy pro školní hodiny na základě předem definovaných kombinací hodin. Výsledné rozvrhy jsou ukládány do fronty pro další zpracování.

"""

# Importování potřebných knihoven a modulů
from DataModels.Hodina import Hodina  # Importujeme třídu Hodina
import random
import csv
import copy

def nacti_kombinace_z_csv(soubor):
    """
    Načte kombinace hodin z CSV souboru a vytvoří seznam objektů třídy Hodina.

    Parametry:
    soubor (str): Cesta k CSV souboru s kombinacemi hodin.

    Návratová hodnota:
    list: Seznam objektů třídy Hodina reprezentujících kombinace hodin.
    """
    kombinace = []
    with open(soubor, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for radek in reader:
            predmet = radek['Predmet']
            typ = radek['Typ'] if radek['Typ'] != 'None' else None
            ucitel = radek['Ucitel'] if radek['Ucitel'] != 'None' else None
            ucebna = radek['Ucebna'] if radek['Ucebna'] != 'None' else None
            pocet = int(radek['Pocet']) if radek['Pocet'].isdigit() else None
            kombinace.append(Hodina(predmet, typ, ucitel, ucebna, pocet))
    return kombinace

def generator_rozvrhu(queue, terminate_event, pocet_vygenerovanych, soubor_csv):
    """
    Generuje náhodné rozvrhy a ukládá je do fronty pro další zpracování.

    Parametry:
    queue (Queue): Fronta pro ukládání vygenerovaných rozvrhů.
    terminate_event (Event): Událost signalizující ukončení generování rozvrhů.
    pocet_vygenerovanych (Value): Sdílená hodnota uchovávající počet vygenerovaných rozvrhů.
    soubor_csv (str): Cesta k CSV souboru s kombinacemi hodin.
    """
    kombinace = nacti_kombinace_z_csv(soubor_csv)
    celkove_hodiny = []
    for hodina in kombinace:
        celkove_hodiny.extend([hodina] * hodina.pocet)

    try:
        while not terminate_event.is_set():
            rozvrh = {}
            random.shuffle(celkove_hodiny)  # Zamíchání hodin pro každý nový rozvrh

            index = 0
            for den in ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek"]:
                # Rozdělení hodin do dnů
                den_rozvrhu = celkove_hodiny[index:index+10]
                index += 10
                rozvrh[den] = den_rozvrhu

            queue.put(rozvrh)
            with pocet_vygenerovanych.get_lock():
                pocet_vygenerovanych.value += 1

    except Exception as e:
        print(f"Došlo k chybě v generátoru: {e}")


