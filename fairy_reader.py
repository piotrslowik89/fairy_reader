import sounddevice as sd
import numpy as np
import keyboard
import time
import threading

# 🌟 NAPIS POWITALNY 🌟
def display_welcome_message():
    print("""
    ==============================================
    🎧  Fairy Reader (pol. BajkoCzytacz) AUTOMATION SCRIPT  🎧
    ==============================================
    📌 Autor: Piotr Słowik
    📌 Licencja: MIT
    📌 Wersja: 1.0
    📌 Opis: Automatyczne wykrywanie ciszy i reakcja klawiszowa
    ==============================================
    """)

display_welcome_message()

# Parametry nasłuchiwania
SAMPLE_RATE = 44100  # Częstotliwość próbkowania (Hz)
DURATION = 2  # Czas ciszy w sekundach wymagany do aktywacji sekwencji
THRESHOLD = 0.001  # Obniżony próg wykrywania ciszy

# Flagi i zmienne kontrolujące
listening = False    
stop_program = False
last_sound_time = None
sequence_executed = False

# 🔍 Automatyczne wyszukiwanie najlepszego urządzenia
def find_best_device():
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        if device['max_input_channels'] > 0 and "Stereo Mix" in device['name']:
            print(f"✅ Używam urządzenia: {device['name']} (ID: {i})")
            return i
    print("❌ Nie znaleziono odpowiedniego urządzenia dźwięku systemowego! Wybieram pierwsze dostępne.")
    for i, device in enumerate(devices):
        if device['max_input_channels'] > 0:
            print(f"✅ Używam urządzenia: {device['name']} (ID: {i})")
            return i
    return None

output_device_id = find_best_device()
if output_device_id is None:
    exit("🔴 Skrypt zakończony: Brak odpowiedniego urządzenia audio!")

device_info = sd.query_devices(output_device_id)
num_channels = max(1, min(device_info['max_input_channels'], 2))

sd.default.device = (output_device_id, None)

def detect_silence(indata, frames, callback_time, status):
    """Funkcja analizująca dźwięk w czasie rzeczywistym."""
    global last_sound_time, sequence_executed

    volume_norm = np.linalg.norm(indata) / len(indata)  # Normalizacja poziomu głośności
    if volume_norm > THRESHOLD:
        last_sound_time = time.time()
        sequence_executed = False

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
    last_sound_time = time.time()
    sequence_executed = False
    print("🎧 Nasłuchiwanie rozpoczęte... (F9, aby zatrzymać)")

    with sd.InputStream(callback=detect_silence, samplerate=SAMPLE_RATE, channels=num_channels, device=output_device_id, dtype='float32'):
        while listening and not stop_program:
            time.sleep(0.1)
            if time.time() - last_sound_time > DURATION and not sequence_executed:
                execute_sequence()
                sequence_executed = True

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
    last_sound_time = None
    sequence_executed = False
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
    time.sleep(0.1)
