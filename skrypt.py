import os
import subprocess

# Ścieżka do głównego katalogu repozytorium
base_dir = r'Cyber-WSPA'

# Zbierz wszystkie pliki, które znajdują się w podfolderach (czyli nowych lokalizacjach)
moved_files = {}
for root, dirs, files in os.walk(base_dir):
    for file in files:
        old_path = os.path.join(base_dir, file)  # poprzednia lokalizacja
        new_path = os.path.join(root, file)      # nowa lokalizacja (jeśli inna)
        if old_path != new_path:
            moved_files[old_path] = new_path

# Wypisz i wykonaj git mv
for old, new in moved_files.items():
    # Upewnij się, że plik wcześniej istniał w katalogu głównym
    if os.path.exists(new):
        print(f"git mv \"{old}\" \"{new}\"")
        try:
#            subprocess.run(["git", "mv", old, new], check=True)
            print(f"git mv \"{old}\" \"{new}\"")
        except subprocess.CalledProcessError:
            print(f"❌ Błąd przy przenoszeniu: {old} -> {new}")

print('Nacisnij ENTER')

