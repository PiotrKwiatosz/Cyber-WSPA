import os
import subprocess

# Ścieżka główna repozytorium (folder z plikami przed przeniesieniem)
base_dir = r'C:\Users\piotr\OneDrive\Dokumenty\IT\WSPA\GitHub\Cyber-WSPA'

# Pobranie listy plików w katalogu głównym (stara lokalizacja)
old_files = {
    file: os.path.join(base_dir, file)
    for file in os.listdir(base_dir)
    if os.path.isfile(os.path.join(base_dir, file))
}

# Przejście po wszystkich podkatalogach i dopasowanie przeniesionych plików
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file in old_files:
            old_path = old_files[file]
            new_path = os.path.join(root, file)

            # Jeśli plik faktycznie został przeniesiony, wykonaj git mv
            if old_path != new_path and os.path.exists(new_path):
                print(f"Przenoszę: {old_path} -> {new_path}")
                try:
                    subprocess.run(["git", "mv", old_path, new_path], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"❌ Błąd: {e}")
                # Po przeniesieniu usuwamy z listy, żeby nie próbować drugi raz
                del old_files[file]

# Podsumowanie
if not old_files:
    print("\n✅ Wszystkie pliki zostały przeniesione za pomocą git mv.")
else:
    print("\n⚠️ Nie znaleziono nowych lokalizacji dla następujących plików:")
    for file, path in old_files.items():
        print(f" - {path}")
