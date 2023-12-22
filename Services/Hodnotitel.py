import queue

def hodnotitel(queue_rozvrhu, queue_vysledku, terminate_event, pocet_vyhodnocenych):
    """
    Proces hodnotitele, který vyhodnocuje rozvrhy a počítá jejich skóre.

    Args:
        queue_rozvrhu (multiprocessing.Queue): Fronta obsahující vygenerované rozvrhy.
        queue_vysledku (multiprocessing.Queue): Fronta pro uložení výsledků hodnocení.
        terminate_event (multiprocessing.Event): Událost signalizující ukončení procesu.
        pocet_vyhodnocenych (multiprocessing.Value): Celkový počet vyhodnocených rozvrhů.
    """
    while not terminate_event.is_set() or not queue_rozvrhu.empty():
        try:
            rozvrh = queue_rozvrhu.get(timeout=1)
            skore = vyhodnot_rozvrh(rozvrh)
            queue_vysledku.put((rozvrh, skore))
            # print(f"Rozvrh: {rozvrh}, Skóre: {skore}")  # Výpis rozvrhu a skóre
            with pocet_vyhodnocenych.get_lock():
                pocet_vyhodnocenych.value += 1

                if skore >= 5:
                    # Výpis nejlepších rozvrhů s vyšším skóre než 5
                    print(f"Nejlepší Rozvrhy s vyšším skóre než 5: Skóre: {skore}")
                    for den, hodiny in rozvrh.items():
                        print(f"{den}: {[h.predmet for h in hodiny]}")

        except queue.Empty:
            continue
        except Exception as e:
            print(f"Došlo k chybě při hodnocení rozvrhu: {e}")

def vyhodnot_rozvrh(rozvrh):
    """
    Vypočítá skóre pro daný rozvrh.

    Args:
        rozvrh (dict): Slovník reprezentující rozvrh pro každý den.

    Returns:
        int: Celkové skóre rozvrhu.

    Raises:
        Exception: V případě chyby ve výpočtu skóre.
    """
    try:
        skore = 0  # Počáteční skóre

        # Předměty, za které se snižuje skóre
        nezadouci_predmety = ["M", "C", "AM", "CIT", "PV", "WA", "PIS", "PSS", "DS", "A", "TV", "TP"]

        # Předměty, které zvyšují skóre, pokud jdou po sobě jako cvičení
        cviceni_predmety = ["CIT", "PV", "WA", "PIS", "PSS", "DS"]

        # Procházení rozvrhu a výpočet skóre
        for den, hodiny in rozvrh.items():
            # Kontrola 9. a 10. hodiny
            if hodiny[8].predmet in nezadouci_predmety or hodiny[9].predmet in nezadouci_predmety:
                skore -= 5

            # Kontrola cvičení stejného předmětu jdoucích po sobě
            for i in range(len(hodiny) - 1):
                if (hodiny[i].predmet == hodiny[i + 1].predmet and
                    hodiny[i].predmet in cviceni_predmety and
                    hodiny[i].typ == 'cvičení' and hodiny[i + 1].typ == 'cvičení'):
                    skore += 5

            # Kontrola první hodiny dne
            if hodiny[0].predmet in ["AM", "M", "C"]:
                skore -= 1

            # Kontrola první hodiny dne
            if hodiny[0].predmet == "Volno":
                skore -= 10

        return skore
    except Exception as e:
        print(f"Došlo k chybě při výpočtu skóre: {e}")
        return 0
