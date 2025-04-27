import sounddevice as sd
import numpy as np
import keyboard
import time
import threading
import platform

# 🌟 NAPIS POWITALNY 🌟
def display_welcome_message():
    print("""
    ==============================================
    🎧  Fairy Reader (pol. BajkoCzytacz) AUTOMATION SCRIPT PRO  🎧
    ==============================================
    📌 Autor: Piotr Słowik
    📌 Licencja: MIT
    📌 Wersja: 1.1 PRO
    📌 Opis: Automatyczne wykrywanie ciszy i reakcja klawiszowa
    ==============================================
    """)

display_welcome_message()

# Parametry nasłuchiwania
SAMPLE_RATE = 44100
DURATION = 0.35  # Czas ciszy w sekundach wymagany do aktywacji sekwencji
THRESHOLD = 0.001  # Próg wykrywania ciszy

# Flagi i zmienne kontrolujące
listening = False
stop_program = False
last_sound_time = None
sequence_executed = False

# 🔍 Automatyczne wyszukiwanie najlepszego urządzenia
DEVICE_KEYWORDS = {
    "Windows": ['stereo mix', 'miks stereo', 'stereo input', 'cable output'],
    "Linux": ['monitor'],
    "Darwin": ['soundflower', 'blackhole']
}

def find_possible_devices():
    system_os = platform.system()
    keywords = DEVICE_KEYWORDS.get(system_os, [])
    print(f"🔍 Wykryto system operacyjny: {system_os}")
    print("🔍 Dostępne urządzenia wejściowe:")
    candidates = []
    for i, device in enumerate(sd.query_devices()):
        if device['max_input_channels'] > 0:
            print(f"{i}: {device['name']}")
            name = device['name'].lower()
            if any(keyword in name for keyword in keywords):
                candidates.append((i, device['name']))
    return candidates

# Wybór urządzenia
candidates = find_possible_devices()

if candidates:
    print("\n✅ Możliwe urządzenia systemowe znalezione:")
    for idx, name in candidates:
        print(f"  {idx}: {name}")
    output_device_id = candidates[0][0]
    print(f"\nProponowane urządzenie: {output_device_id} ({candidates[0][1]})")
    choice = input("Czy chcesz użyć tego urządzenia? (T/n): ").strip().lower()
    if choice == 'n':
        output_device_id = int(input("Podaj numer urządzenia, którego chcesz użyć: "))
else:
    print("\n❌ Nie znaleziono urządzenia systemowego.")
    output_device_id = int(input("Podaj numer urządzenia, którego chcesz użyć z listy powyżej: "))

# Konfiguracja urządzenia
try:
    device_info = sd.query_devices(output_device_id)
    num_channels = max(1, min(device_info['max_input_channels'], 2))
    sd.default.device = (output_device_id, None)
except Exception as e:
    print(f"❌ Błąd wyboru urządzenia: {e}")
    exit()

def detect_silence(indata, frames, callback_time, status):
    global last_sound_time, sequence_executed
    volume_norm = np.linalg.norm(indata) / len(indata)
    if volume_norm > THRESHOLD:
        last_sound_time = time.time()
        sequence_executed = False

def execute_sequence():
    print("🔇 Cisza wykryta - wykonuję sekwencję klawiszy")
    keyboard.press_and_release("space")
    time.sleep(0.2)
    keyboard.press_and_release("alt+tab")
    time.sleep(0.2)
    keyboard.press_and_release("space")

def listen():
    global listening, last_sound_time, sequence_executed
    last_sound_time = time.time()
    sequence_executed = False
    print("🎧 Nasłuchiwanie rozpoczęte... (F9 aby zatrzymać)")
    try:
        with sd.InputStream(callback=detect_silence, samplerate=SAMPLE_RATE, channels=num_channels, device=output_device_id, dtype='float32'):
            while listening and not stop_program:
                time.sleep(0.1)
                if time.time() - last_sound_time > DURATION and not sequence_executed:
                    execute_sequence()
                    sequence_executed = True
    except Exception as e:
        print(f"❌ Błąd strumienia audio: {e}")
        stop_listening()

def start_listening():
    global listening, last_sound_time, sequence_executed
    if listening:
        print("🟡 Nasłuchiwanie już aktywne.")
        return
    listening = True
    threading.Thread(target=listen, daemon=True).start()

def stop_listening():
    global listening, last_sound_time, sequence_executed
    if not listening:
        print("🔵 Nasłuchiwanie już wyłączone.")
        return
    listening = False
    last_sound_time = None
    sequence_executed = False
    print("🛑 Nasłuchiwanie zatrzymane.")

def exit_program():
    global stop_program, listening
    stop_program = True
    listening = False
    print("🚪 Zamykanie programu...")
    time.sleep(1)
    exit()

keyboard.add_hotkey("F9", lambda: start_listening() if not listening else stop_listening())
keyboard.add_hotkey("esc", exit_program)

print("🔵 Naciśnij F9, aby rozpocząć/zatrzymać nasłuchiwanie.")
print("🔴 Naciśnij ESC, aby zamknąć program.")

while not stop_program:
    time.sleep(0.1)
