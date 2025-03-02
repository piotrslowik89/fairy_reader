# **Fairy Reader** 📖🎧
## (pol. "Baśniowy Czytelnik" , "Bajkoczytacz") ##

> **Nauka języka poprzez naturalne przyswajanie – bez gramatyki, bez wkuwania.**

## 📌 **Idea**

Fairy Reader to metoda nauki języków inspirowana sposobem, w jaki uczą się małe dzieci – **przez immersję, kontekst i kojarzenie**. Zamiast mechanicznej nauki gramatyki, użytkownik poznaje język poprzez **czytanie książek i słuchanie ich wymowy**, co pozwala na szybkie przyswajanie nowych słów i struktur językowych.

### ⏳ **Szacowany czas nauki (przy założeniu 1h dziennie):**

1. **Poziom B2** – ~600 godzin (~1,6 roku)
2. **Poziom C2** – dodatkowe ~600 godzin (~1,6 roku)

Jednak dzięki **interesującym książkom i zaangażowaniu** nauka może być znacznie szybsza i bardziej efektywna! 🚀

---

## ✅ **Zalety metody Fairy Reader**

1. **Aktywna nauka poprzez kontekst**

   - Czytanie pobudza wyobraźnię, tworząc **"teatr wyobraźni"**.
   - Używane słownictwo pochodzi z rzeczywistego języka, co pozwala lepiej go zrozumieć.
   - Połączenie tekstu z lektorem pomaga w nauce poprawnej wymowy.

2. **Bez nudnego wkuwania**

   - Brak sztucznego powtarzania i list słówek – zamiast tego naturalna nauka w kontekście.
   - Nowe słowa zapamiętywane są w **realnych sytuacjach**, co zwiększa ich trwałość w pamięci.

3. **Łatwość dostosowania do własnych potrzeb**

   - Możliwość wyboru dowolnej książki.
   - Elastyczna metoda, którą można stosować w różnych językach.

---

## ⚠️ **Wady metody**

- **Początkowa trudność** – na początku może wydawać się to trudne lub nużące.
- **Skrypt nie jest idealny** – może niekiedy zatrzymać się w niewłaściwym miejscu.
- **Wymaga konfiguracji** – konieczne jest przygotowanie książek i uruchomienie skryptu.

Jednak po krótkim okresie adaptacji metoda staje się **intuicyjna i efektywna**!

---

## 🎯 **Jak działa skrypt?**

Fairy Reader **automatycznie przełącza okna** między książką w języku obcym a jej tłumaczeniem po wykryciu ciszy w narracji.

### 🔧 **Mechanizm działania:**

1. **Nasłuchiwanie dźwięku systemowego** (np. audiobooka) przy użyciu **Stereo Mix**.
2. Po wykryciu **ciszy ≥ 0,35 s** po kropce, skrypt wykonuje sekwencję:
   ```
   SPACE → ALT+TAB → SPACE
   ```
3. Dzięki temu książki w dwóch językach **automatycznie się przełączają**, umożliwiając porównanie treści.

---

## 🛠 **Instrukcja konfiguracji**

### 🔹 **1. Przygotowanie książki**

1. Pobierz książkę w formacie **.EPUB** lub **.MOBI**.

2. Przetłumacz ją automatycznie w **Calibre**:

   - **Ustawienia → Wtyczki → Pobierz nowe wtyczki** → Wyszukaj **Ebook Translator**.
   - Po instalacji:     **Prawym na książkę → Wtyczki → Ustawienia → Content → "With no original"**.

3. **Edycja książki**:

   - Kliknij **prawym na książkę** → **Edycja książki**.
   - Otwórz pierwszy plik HTML i dokonaj **niezbędnych poprawek**:
     - Zamień niemieckie cudzysłowy `» «` na spacje.
     - Zamień skróty w języku angielskim np. `Mr.`, `Mrs.` na `Mr`, `Mrs`. Kropka po Pan i Pani będzie traktowana jako koniec zdania.

---

### 🔹 **2. Instalacja wymaganych programów**

1. **Zainstaluj Calibre** 📚   👉 [Pobierz Calibre](https://calibre-ebook.com/)

2. **Skonfiguruj syntezę mowy (TTS)**

   - **Prawym na książkę → "Czytaj na głos"**
   - **Z menu na dole wybierz → Skonfiguruj Czytanie na głos**
   - **Wybierz Silnik neuronowy Piper**.     ⚠️ **Uwaga:** Niektóre głosy najwyższej jakości mogą zużywać dużo zasobów systemowych.

3. **Ustawienie pauzy po zdaniu (0,70 s)**

   - Przejdź do ustawień **TTS** w Calibre.

---

### 🔹 **3. Instalacja Pythona i wymaganych bibliotek**

1. **Zainstaluj Pythona** 🐍   👉 [Pobierz Python](https://www.python.org/)
2. **Zainstaluj wymagane biblioteki**   Otwórz terminal (cmd / PowerShell) i wpisz:
   ```sh
   pip install sounddevice numpy keyboard
   ```
3. **Aktywuj Stereo Mix**
   - **Kliknij prawym** na ikonę dźwięku w Windows.
   - **Dźwięki → Zakładka "Nagrywanie"**.
   - **Pokaż wyłączone urządzenia** i włącz **Stereo Mix**.

---

### 🔹 **4. Uruchomienie skryptu**

Po przygotowaniu książek i ustawieniu lektora:

1. Otwórz dwa okna **Calibre** z książką w języku obcym i tłumaczeniem.
2. Ustaw ich **automatyczne czytanie**.
3. **Spauzuj lektora** w obu oknach.
4. **Uruchom skrypt**:
   ```sh
   python fairy_reader.py
   ```
5. **Sterowanie skryptem**:
   - 🔵 **F9** – Rozpocznij/zatrzymaj nasłuchiwanie.
   - 🔴 **ESC** – Zamknij program.

---

## 🎥 **Linki do YouTube**

📽 **Prezentacja działania Fairy Reader**📽 **Instrukcja konfiguracji i instalacji**

*(Podaj tutaj linki do filmów, jeśli są dostępne)*

---

## 📌 **Podsumowanie**

Fairy Reader to **nowatorskie narzędzie** do nauki języków poprzez czytanie i słuchanie audiobooków. Dzięki automatycznemu przełączaniu między książką w języku obcym a jej tłumaczeniem, metoda ta pozwala na szybkie i przyjemne przyswajanie nowego słownictwa. 🚀

🔹 **Brak gramatyki** – naturalne przyswajanie języka.🔹 **Szybsza nauka** – realne teksty i kontekst.🔹 **Pełna automatyzacja** – skrypt zarządza przełączaniem.

---