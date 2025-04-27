
# Poprawianie skrótów w ebookach wielojęzycznych (PL/EN/DE/RU)

Ten plik zawiera wyrażenia regularne (regex), które umożliwiają poprawę skrótów w książkach elektronicznych w językach: angielskim, niemieckim i rosyjskim.

Pomaga to usunąć niepotrzebne kropki w skrótach, aby skrypty do wykrywania końca zdań (np. Fairy Reader) działały poprawnie.

---

## 🇬🇧 Angielski (English)

### Tytuły osób

**Znajdź:**

```regex
(Mr|Mrs|Ms|Dr|Prof|Rev|Sr|Jr)\.
```

**Zamień na:**

```regex

```

### Stopnie naukowe i zawodowe

**Znajdź:**

```regex
(M\.D\.|Ph\.D\.|B\.A\.|M\.A\.|D\.D\.S\.|J\.D\.|B\.Sc\.|M\.Sc\.)
```

**Zamień na:**

```regex

```

*(Uwaga: Po zamianie należy ręcznie usunąć kropki np. M.D. → MD)*

### Skróty adresowe

**Znajdź:**

```regex
(St|Ave|Blvd|Rd)\.
```

**Zamień na:**

```regex

```

### Skróty czasu

**Znajdź:**

```regex
(a\.m\.|p\.m\.)
```

**Zamień na:**

```regex

```

### Skróty zwrotów

**Znajdź:**

```regex
(e\.g\.|i\.e\.|etc\.)
```

**Zamień na:**

```regex

```

---

## 🇩🇪 Niemiecki (Deutsch)

### Tytuły i stopnie naukowe

**Znajdź:**

```regex
(Hr|Fr|Dr|Prof)\.
```

**Zamień na:**

```regex

```

### Powszechne skróty

**Znajdź:**

```regex
(Bsp|z\.B|u\.a|vgl)\.
```

**Zamień na:**

```regex

```

- z.B. = na przykład
- u.a. = między innymi
- vgl. = porównaj

### Uwagi dotyczące czasu

W języku niemieckim zwykle zapisuje się godziny w formacie `10:30 Uhr`, więc nie jest wymagana zmiana.

---

## 🇷🇺 Rosyjski (русский)

### Adresy i terminy geograficzne

**Znajdź:**

```regex
(г|ул|д|просп|пл|пер)\.
```

**Zamień na:**

```regex

```

- г. = miasto (город)
- ул. = ulica (улица)
- д. = dom (дом)
- просп. = aleja (проспект)
- пл. = plac (площадь)
- пер. = uliczka (переулок)

### Powszechne skróty

**Znajdź:**

```regex
(т\.д\.|т\.п\.|и\.т\.д\.|и\.т\.п\.)
```

**Zamień na:**

```regex

```

- т.д. = i tak dalej
- т.п. = i temu podobne

---

# 🔄 Wskazówki dotyczące użycia

- Zawsze włącz opcję **Wyrażenia regularne (Regex)**.
- Włącz opcję **Uwzględniaj wielkość liter** (szczególnie dla angielskich tytułów).
- W przypadku tekstu rosyjskiego upewnij się, że edytor używa kodowania UTF-8.
- Ręczne poprawki mogą być potrzebne dla stopni naukowych (np. M.D. → MD).