# alpha

Tento projekt představuje komplexní systém pro generování a hodnocení školních rozvrhů. Jeho hlavním cílem je efektivně vytvářet různé varianty rozvrhů a následně je hodnotit na základě předem definovaných kritérií, aby bylo možné určit, které rozvrhy jsou nejvhodnější pro použití.

Klíčové Komponenty
Generátor Rozvrhů: Tento modul je zodpovědný za vytváření různých kombinací rozvrhů. Využívá algoritmy, které berou v úvahu různé aspekty a omezení školního prostředí, aby vyprodukoval širokou škálu možností.

Hodnotitel Rozvrhů: Po vygenerování rozvrhů tento modul je analyzuje a hodnotí. Rozvrhy jsou posuzovány podle kritérií, jako jsou celková vyváženost, rozložení předmětů během týdne, a další faktory, které ovlivňují jejich praktičnost a efektivitu.

Watchdog Timer: Tato součást projektu hraje klíčovou roli v řízení časování procesu. Nastavuje časový limit pro generátor a hodnotitele, aby se zajistilo, že proces generování a hodnocení je efektivní a nezabere nadměrně dlouhou dobu.



main.py: Hlavní spouštěcí skript projektu.
Generator.py: Skript pro import potřebných knihoven a modulů, a rozdělení hodin do dnů.
Hodnotitel.py: Skript pro výpis rozvrhů a jejich skóre, zahrnuje logiku pro hodnocení rozvrhů s vyšším skóre než 5 a prochází rozvrh pro výpočet skóre.
Watchdog.py: Skript pro import potřebných knihoven a modulů, kontroluje číselný timeout a jeho validitu.

Projekt dále obsahuje tři doménově specifické moduly:

Den.py: Skript související s logikou dne.
Hodina.py: Skript související s logikou hodiny.
Rozvrh.py: Skript související s logikou rozvrhu.

A testovací skripty:

test_generator.py: Testovací skript pro Generator
test_hodnotitel.py Testovací skript pro Hodnotitel.
test_watchdog.py Testovací skript pro Watchdog

Požadavky:
Seznam požadovaných knihoven.
- random
- csv
- queue
-multiprocessing

Instalace a Spuštění

git clone https://github.com/FilipKovbljuk/alpha.git
cd alpha
python main.py