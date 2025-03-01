import sounddevice as sd
import numpy as np
import keyboard
import time
import threading

# Parametry nasłuchiwania
SAMPLE_RATE = 44100  # Częstotliwość próbkowania (Hz)
DURATION = 0.35  # Czas ciszy w sekundach wymagany do aktywacji sekwencji
THRESHOLD = 0.01  # Próg dźwięku uznawanego za ciszę

# Flagi i zmienne kontrolujące
listening = False
stop_program = False  # Flaga do zakończenia programu
last_sound_time = None  # Zmieniam na None, aby resetować poprawnie
sequence_executed = False  # Zapobiega wielokrotnemu wywoływaniu

# 🔍 Automatyczne wyszukiwanie "Miks stereo"
def find_stereo_mix():
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        if "Miks stereo" in device['name']:
            print(f"✅ Używam urządzenia: {device['name']} (ID: {i})")
            return i
    print("❌ Nie znaleziono 'Miks stereo'. Sprawdź ustawienia dźwięku!")
    return None

stereo_mix_id = find_stereo_mix()
if stereo_mix_id is not None:
    sd.default.device = (stereo_mix_id, None)  # Ustaw "Miks stereo" jako źródło wejściowe
else:
    exit("🔴 Skrypt zakończony: Brak 'Miks stereo'")

def detect_silence(indata, frames, callback_time, status):
    """Funkcja analizująca dźwięk w czasie rzeczywistym."""
    global last_sound_time, sequence_executed

    volume_norm = np.linalg.norm(indata)  # Obliczenie poziomu głośności
    if volume_norm > THRESHOLD:
        last_sound_time = time.time()  # Aktualizacja czasu ostatniego dźwięku
        sequence_executed = False  # Reset flagi po wykryciu dźwięku

def execute_sequence():
    """Wykonuje sekwencję klawiszy: space -> alt+tab -> space."""
    print("🔇 Cisza wykryta - wykonuję sekwencję klawiszy")
    keyboard.press_and_release("space")
    time.sleep(0.2)
    keyboard.press_and_release("alt+tab")
    time.sleep(0.2)
    keyboard.press_and_release("space")

def listen():
    """Obsługuje nasłuchiwanie dźwięków systemowych."""
    global listening, last_sound_time, sequence_executed
    last_sound_time = time.time()  # Resetowanie czasu ciszy na start
    sequence_executed = False  # Reset flagi
    print("🎧 Nasłuchiwanie rozpoczęte... (F9, aby zatrzymać)")

    with sd.InputStream(callback=detect_silence, samplerate=SAMPLE_RATE, channels=1, dtype='float32'):
        while listening and not stop_program:
            time.sleep(0.1)
            if time.time() - last_sound_time > DURATION and not sequence_executed:
                execute_sequence()
                sequence_executed = True  # Zapobiega wielokrotnemu wywoływaniu

def start_listening():
    """Rozpoczyna nasłuchiwanie w osobnym wątku, resetując wartości."""
    global listening, last_sound_time, sequence_executed
    if listening:
        print("🟡 Nasłuchiwanie już aktywne.")
        return
    listening = True
    threading.Thread(target=listen, daemon=True).start()

def stop_listening():
    """Zatrzymuje nasłuchiwanie i resetuje wartości."""
    global listening, last_sound_time, sequence_executed
    if not listening:
        print("🔵 Nasłuchiwanie już wyłączone.")
        return
    listening = False
    last_sound_time = None  # Resetowanie czasu ciszy
    sequence_executed = False  # Reset flagi
    print("🛑 Nasłuchiwanie zatrzymane.")

def exit_program():
    """Zamyka program."""
    global stop_program, listening
    stop_program = True
    listening = False
    print("🚪 Zamykanie programu...")
    time.sleep(1)
    exit()

# 🔥 Podpięcie klawiszy
keyboard.add_hotkey("F9", lambda: start_listening() if not listening else stop_listening())
keyboard.add_hotkey("esc", exit_program)

print("🔵 Naciśnij F9, aby rozpocząć/zatrzymać nasłuchiwanie.")
print("🔴 Naciśnij ESC, aby zamknąć program.")

while not stop_program:
    time.sleep(0.1)  # Pętla utrzymująca skrypt aktywny
