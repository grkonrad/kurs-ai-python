# Przykład skryptu: gotowy program uruchamiany od początku do końca.
# Specyfikacja dla przyszłej pracy z agentem:
# Odczytaj zakupy.csv z folderu tego skryptu. Nie zmieniaj danych źródłowych.
# Oblicz koszt każdej pozycji i sumę. Wyświetl tabelę i sumę w złotych.
# Wynik kontrolny dla dołączonych danych: 5 pozycji, razem 29.60 zł.

from pathlib import Path  # Narzędzie do wskazania położenia pliku.
import pandas as pd  # Biblioteka do pracy z tabelami, pod krótką nazwą pd.

plik_danych = Path(__file__).with_name("zakupy.csv")
zakupy = pd.read_csv(plik_danych)
zakupy["koszt_zl"] = zakupy["liczba_sztuk"] * zakupy["cena_za_sztuke_zl"]
suma = zakupy["koszt_zl"].sum()
print(zakupy.to_string(index=False))
print("Suma zakupów:", round(suma, 2), "zł")
