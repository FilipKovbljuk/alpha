import multiprocessing
from Services.Generator import generator_rozvrhu
from Services.Hodnotitel import hodnotitel
from Services.Watchdog import watchdog

def zpracuj_a_vypis_nejlepsi_rozvrhy(queue_vysledku):
    """
    Zpracuje výsledky hodnocení a vypíše nejlepší rozvrhy.

    Args:
        queue_vysledku (multiprocessing.Queue): Fronta obsahující páry (rozvrh, skóre).

    Výstup:
        Vypíše nejlepší rozvrhy a jejich skóre.
    """
    nejlepsi_skore = float('-inf')
    nejlepsi_rozvrhy = []

    while not queue_vysledku.empty():
        rozvrh, skore = queue_vysledku.get()
        if skore > nejlepsi_skore:
            nejlepsi_skore = skore
            nejlepsi_rozvrhy = [rozvrh]
        elif skore == nejlepsi_skore:
            nejlepsi_rozvrhy.append(rozvrh)

    # Výpis nejlepších rozvrhů
    print(f"Nejlepší rozvrhy s skóre {nejlepsi_skore}:")
    for rozvrh in nejlepsi_rozvrhy:
        for den, hodiny in rozvrh.items():
            print(f"{den}: {[h.predmet for h in hodiny]}")
        print()  # Prázdný řádek pro oddělení rozvrhů


if __name__ == "__main__":
    """
    Hlavní skript pro spuštění generátorů rozvrhů, hodnotitelů a watchdog procesu.
    Na konci zpracovává výsledky a vypisuje nejlepší rozvrhy.
    """
    queue_rozvrhu = multiprocessing.Queue()
    queue_vysledku = multiprocessing.Queue()
    terminate_event = multiprocessing.Event()
    pocet_vygenerovanych = multiprocessing.Value('i', 0)
    pocet_vyhodnocenych = multiprocessing.Value('i', 0)

    # Spuštění generátorů
    pocet_procesu = 2
    procesy_generatoru = []
    for _ in range(pocet_procesu):
        proc = multiprocessing.Process(target=generator_rozvrhu, args=(queue_rozvrhu, terminate_event, pocet_vygenerovanych, 'kombinace.csv'))
        procesy_generatoru.append(proc)
        proc.start()

    # Spuštění hodnotitelů
    pocet_procesu_hodnotitelu = 2
    procesy_hodnotitele = []
    for _ in range(pocet_procesu_hodnotitelu):
        proc = multiprocessing.Process(target=hodnotitel, args=(queue_rozvrhu, queue_vysledku, terminate_event, pocet_vyhodnocenych))
        procesy_hodnotitele.append(proc)
        proc.start()

    # Spuštění watchdog
    watchdog_proc = multiprocessing.Process(target=watchdog, args=(10, terminate_event))
    watchdog_proc.start()

    # Čekání na ukončení watchdog procesu
    watchdog_proc.join()

    # Signalizace ukončení generátorů
    terminate_event.set()

    # Ukončení generátorů
    for proc in procesy_generatoru:
        proc.terminate()
        proc.join()

    # Ukončení hodnotitelů
    for proc in procesy_hodnotitele:
        proc.terminate()
    for proc in procesy_hodnotitele:
        proc.join()

    # Zpracování a výpis nejlepších rozvrhů
    zpracuj_a_vypis_nejlepsi_rozvrhy(queue_vysledku)

    print(f"Celkový počet vygenerovaných rozvrhů: {pocet_vygenerovanych.value}")
    print(f"Celkový počet vyhodnocených rozvrhů: {pocet_vyhodnocenych.value}")
