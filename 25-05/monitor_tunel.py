import socket
import time
import datetime

TUNEL_HOST = "127.0.0.1"
TUNEL_PORT = 2000  # port przekierowany z Azure
INTERVAL_SEK = 60

def sprawdz_tunel(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((host, port))
        s.close()
        return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

def log(text):
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {text}")

if __name__ == "__main__":
    log("Monitoring tunelu SSH wystartował...")

    while True:
        if sprawdz_tunel(TUNEL_HOST, TUNEL_PORT):
            log("✅ Tunel działa prawidłowo.")
        else:
            log("❌ Tunel NIE działa! Port niedostępny.")
            # Tutaj możesz dodać restart tunelu lub powiadomienie
            # np. os.system("ssh -R ...")
        time.sleep(INTERVAL_SEK)
