# Dane demonstracyjne LPBF

Dwanaście rekordów utworzonych na potrzeby nauki Pythona. **Dane są sztuczne.** Nie stanowią zbioru 256 próbek prowadzącego ani fizycznie zwalidowanego modelu procesu.

| Kolumna | Znaczenie | Jednostka |
|---|---|---|
| sample_id | Unikalny identyfikator rekordu | — |
| P_W | Moc lasera | W |
| v_mm_s | Prędkość skanowania | mm/s |
| h_mm | Odstęp ścieżek | mm |
| t_mm | Założona grubość warstwy | mm |
| porosity_pct | Wartość demonstracyjna porowatości | % |
| source | DEMO_SYNTHETIC — pochodzenie demonstracyjne | tekst |

CSV: UTF-8, separator przecinek, kropka dziesiętna. Puste pole oznacza brak danych. Wartość 0.50% odpowiada udziałowi 0.005. W polu liczbowym nie ma znaku procenta.

Grubość 0.04 mm jest założeniem ćwiczenia. S11 nie ma wyniku porowatości, a S12 zawiera zerową prędkość. Te dwa problemy są celowe. Surowego pliku nie nadpisujemy. Wyłączenia dokumentujemy w osobnej tabeli.

Wyliczane wskaźniki: `E_J_mm3 = P_W / (v_mm_s * h_mm * t_mm)` i `Q_mm3_s = v_mm_s * h_mm * t_mm`. Q pomija nakładanie warstw i inne przerwy. E nie jest samodzielnym modelem porowatości. Progi 0.50%, 0.40% i 0.20% wybrano dydaktycznie.

Po otrzymaniu danych rzeczywistych należy ponownie sprawdzić schemat kolumn, zakresy, jednostki, identyfikatory i definicję odpowiedzi. Nie wolno traktować rozwiązania wzorcowego jako zwalidowanego narzędzia do kwalifikacji procesu.
