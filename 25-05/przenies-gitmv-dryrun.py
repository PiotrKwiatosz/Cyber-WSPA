import os

# Ścieżka główna repozytorium
base_dir = r'C:\Users\piotr\OneDrive\Dokumenty\IT\WSPA\GitHub\Cyber-WSPA'

# Zbierz pliki, które były wcześniej w katalogu głównym
old_files = {
    file: os.path.join(base_dir, file)
    for file in os.listdir(base_dir)
    if os.path.isfile(os.path.join(base_dir, file))
}

# Szukaj tych samych plików w podfolderach (nowe lokalizacje)
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file in old_files:
            old_path = old_files[file]
            new_path = os.path.join(root, file)

            if old_path != new_path and os.path.exists(new_path):
                print(f'git mv "{old_path}" "{new_path}"')
                del old_files[file]

# Podsumowanie
if not old_files:
    print("\n✅ Wszystkie pliki mają nowe lokalizacje.")
else:
    print("\n⚠️ Następujące pliki NIE ZOSTAŁY znalezione w nowych lokalizacjach:")
    for file, path in old_files.items():
        print(f" - {path}")
