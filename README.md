# 📍 Fairy Reader

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
   - Używane słownictwo pochodzi z rzeczywistego języka.
   - Połączenie tekstu z lektorem pomaga w nauce poprawnej wymowy.

2. **Bez nudnego wkuwania**
   - Naturalna nauka w kontekście.
   - Zapamiętywanie nowych słów w realnych sytuacjach.

3. **Elastyczność**
   - Dowolny wybór książek.
   - Możliwość stosowania w wielu językach.

---

## ⚠️ **Wady metody**

- **Początkowa trudność**.
- **Skrypt może się czasem zatrzymać**.
- **Wymagana konfiguracja**.

Jednak po adaptacji metoda staje się **bardzo intuicyjna**!

---

## 🌟 **Jak działa skrypt?**

Fairy Reader **automatycznie przełącza okna** między książką w języku obcym a jej tłumaczeniem po wykryciu ciszy w narracji.

### 🔧 **Mechanizm działania:**

1. **Nasłuch dźwięku systemowego** (np. audiobooka).
2. **Wykrycie ciszy ≥ 0,35 s** powoduje sekwencję:
   ```
   SPACE → ALT+TAB → SPACE
   ```

---

## 🛠 **Instrukcja konfiguracji**

### 🔹 1. **Przygotowanie książek**

- Pobierz książki w formacie **.EPUB** lub **.MOBI**.
- Przetłumacz przez **Calibre** z wtyczką **Ebook Translator**.
- Edytuj plik HTML:
  - Usuń niemieckie cudzysłowy `» «`.
  - Zamień `Mr.`/`Mrs.` na `Mr`/`Mrs` (bez kropki).

### 🔹 2. **Instalacja oprogramowania**

- [Pobierz Calibre](https://calibre-ebook.com/)
- [Pobierz Python](https://www.python.org/)
- Zainstaluj biblioteki:
  ```sh
  pip install sounddevice numpy keyboard
  ```

### 🔹 3. **Konfiguracja audio**

- **Windows**: włącz **Stereo Mix** lub **VB-Cable**.
- **Linux**: użyj **Monitor of Output** (PulseAudio).
- **macOS**: zainstaluj **Soundflower** lub **BlackHole**.

---

## 🚀 **Jak uruchomić Fairy Reader na Windows, Linux i macOS**

### ✅ Windows 10/11

1. Włącz **Stereo Mix** lub **VB-Audio Virtual Cable**.
2. Ustaw **CABLE Input** jako domyślne urządzenie odtwarzające.
3. (Opcjonalnie) Włącz "Nasłuchuj tego urządzenia".
4. Uruchom:
   ```sh
   python fairy_reader.py
   ```

### ✅ Linux (Ubuntu i inne)

1. Korzystaj z **PulseAudio**.
2. Skrypt znajdzie "Monitor of Output".
3. Uruchom:
   ```sh
   python3 fairy_reader.py
   ```

### ✅ macOS

1. Zainstaluj **Soundflower** lub **BlackHole**.
2. Przekieruj dźwięk przez wirtualny kabel.
3. Uruchom:
   ```sh
   python3 fairy_reader.py
   ```

---

## 🔊 Skróty klawiszowe

- 🔵 **F9** — Start/Stop nasłuchu
- 🔴 **ESC** — Wyjście z programu

---

## 📺 Linki do YouTube

- **Prezentacja działania Fairy Reader**
- **Instrukcja konfiguracji i instalacji**

*(Wstaw linki tutaj)*

---

## 📌 Podsumowanie

Fairy Reader to **nowatorskie narzędzie** do nauki języków poprzez czytanie i słuchanie audiobooków z automatycznym przełączaniem treści. 🚀

- Brak wkuwania gramatyki.
- Naturalne przyswajanie języka.
- Pełna automatyzacja!