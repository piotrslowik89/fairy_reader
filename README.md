# fairy_reader

# Idea

Nauka języka w sposób jaki uczą się małe dzieci. Bez gramatyki i wkuwania ale przez korzystanie i kojarzenie.

Chciałem przedstawić mój pomysł szybkiej nauki języków.

Średni szacowany czas nauki dla języków łatwych (przy złożeniu 1h dziennie):
1. Do poziomu B2 600h (1.6 roku)
2. Z B2 do C2 600 h (1.6 roku)

Myślę, że można szybciej w zależności od ilości ciekawych książek :)

# Zalety czytania w ten sposób:
1. Nauka aktywna
Czytanie jest procesem twórczym gdyż cała historia generowana jest w wyobraźni (teatr wyobraźni).
Słowa używane w książkach są takimi z jakich naprawdę korzystają ludzie z innych krajów.
Widzimy tekst i słyszymy wymowę lektora. Poznajemy prawdziwe reakcje.

2. Nauka ciekawa (oczywiście dla ludzi lubiących czytać książki).
Nie ma powtarzania ani wkuwania. Jest korzystanie z języka. Nowo poznane słowa są zakorzenione w kontekście danej sytuacji w książce. 

# Wady
Przestawienie się.
Początkowo wydaje się to trudne i nudne.
Skrypt nie jest idealny. Czasami zatrzyma się w niewłaściwym miejscu.
Można to wysterować za pomocą F9 (które pauzuje wykonywanie skryptu).

# Jak to działa skrypt

Skrypt nasłuchuje wyjście audio z stereo miksera. Po zanotowaniu ciszy o długości 0,35s po kropce wywołuję sekwencję space alt+tab space

Należy uruchomić książkę po Angielsku i po Polsku. W dwóch oknach obok siebie.
Ustawić czytanie w obu instancjach (przez odpowiedniego lektora).
Spauzować.
Uruchomić skrypt fairy_reader.py
Okienka będą się przełączać aktywność miedzy dwoma ostatnio otwartymi.
🔵 Naciśnij F9, aby rozpocząć/zatrzymać nasłuchiwanie.
🔴 Naciśnij ESC, aby zamknąć program.

1. Przygotowanie książki.
Pobranie książki w formacie .EPUB lub . MOBI

translacja
Ustawienia-> wtyczki -> pobierz nowe wtyczki Ebook Translator

Wtyczka->prawym->settings->content-> with no original

2. Edycja książki
Prawym -> Edycja książki
kliknięcie na pierwszy HTML po lewej.

# 
W niemieckich używają francuskich cudzysłowu
» «
Trzeba je wyszukać w dokumencie i zamienić na space we wszystkich przypadkach.

MR. MRS.
W angielskim używa się skróty. 
trzeba je wyszukać i zamienić odpowiednio na MR. MRS. bez kropek

# Instalacja
- pobranie calibre
https://calibre-ebook.com/ 
- dociągnięcie tts
Obecnie Calibre korzysta z Pipera
Prawym-> czytać na głos -> z menu na dole wybrać Skonfiguruj Czytać na głos->Silnik neuronowy Piper.
Polecam nie pobierać głosów najwyższej jakości mogą zużywać dużo zasobów

## Ustawienie pauzy po zdaniu na 0,70 sekund
- instalacja Pythona 
https://www.python.org/

- instalacja bibliotek

- aktywacja miks stereo

- uruchomienie skryptu

# Linki do YouTube
Film z prezentacją
Film z konfiguracją