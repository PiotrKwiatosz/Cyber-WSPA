import socket
import time
import datetime
import os

TUNEL_HOST = "127.0.0.1"
TUNEL_PORT = 2000
INTERVAL_SEK = 60
KOMENDA_SSH = "ssh -f -N -R 2000:localhost:22 ssh123@20.215.40.85"

def sprawdz_tunel(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((host, port))
        s.close()
        return True
    except:
        return False

def log(text):
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {text}")

if __name__ == "__main__":
    log("Monitoring tunelu SSH wystartował...")

    while True:
        if sprawdz_tunel(TUNEL_HOST, TUNEL_PORT):
            log("✅ Tunel działa prawidłowo.")
        else:
            log("❌ Tunel NIE działa! Port niedostępny. Próba ponownego połączenia...")
            os.system(KOMENDA_SSH)
        time.sleep(INTERVAL_SEK)
