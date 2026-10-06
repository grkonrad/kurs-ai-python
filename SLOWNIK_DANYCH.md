# Dane do zajęć nr 1 — koszyk zakupów

`zakupy.csv` zawiera **5 fikcyjnych pozycji i 3 kolumny**, bez danych osobowych.
Ceny są przykładowe, nie są aktualną ofertą sklepu. Każdy produkt liczony jest na sztuki.

| Kolumna | Znaczenie | Przykład |
|---|---|---|
| produkt | Nazwa produktu | Mleko |
| liczba_sztuk | Ile sztuk kupujemy | 2 |
| cena_za_sztuke_zl | Cena jednej sztuki w złotych | 3.20 |

Plik używa kodowania UTF-8, przecinka do rozdzielania kolumn i kropki dziesiętnej.
Pierwszy wiersz jest nagłówkiem. Pięć kolejnych wierszy to dane.

Notatnik tworzy w pamięci czwartą kolumnę `koszt_zl` (liczba sztuk × cena).
Nie nadpisuje CSV. Koszty pozycji: 5.50, 6.40, 4.50, 4.80, 8.40 zł. Suma: **29.60 zł**.
Wykres przedstawia koszt całej pozycji, a nie cenę jednej sztuki.
