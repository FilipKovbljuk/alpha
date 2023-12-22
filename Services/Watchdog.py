"""
watchdog.py - Funkce pro sledování časového limitu a ukončení generátoru.

Tato funkce slouží k sledování časového limitu a automatickému ukončení generátoru v jiném procesu po uplynutí tohoto limitu.

Autor: [Filip Kovlbjuk]
Datum vytvoření: [20.12.2023]

"""

# Importování potřebných knihoven a modulů
import time
import multiprocessing

def watchdog(timeout, terminate_event):
    """
    Funkce pro sledování časového limitu a ukončení generátoru po uplynutí limitu.

    Parametry:
    timeout (int or float): Časový limit v sekundách, po jehož uplynutí bude generátor ukončen.
    terminate_event (multiprocessing.Event): Událost pro signalizaci ukončení generátoru.

    Výjimky:
    ValueError: Pokud je timeout neplatné číslo nebo menší než nebo rovno 0.

    """
    try:
        # Kontrola, zda je timeout číselný a větší než 0
        if not isinstance(timeout, (int, float)) or timeout <= 0:
            raise ValueError("Timeout musí být kladné číslo.")

        time.sleep(timeout)
        terminate_event.set()
        print("Čas vypršel, generátor bude ukončen.")
    except Exception as e:
        print(f"Chyba ve watchdog: {e}")

# Konec souboru watchdog.py
