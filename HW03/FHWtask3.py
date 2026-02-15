import sys
from pathlib import Path
from colorama import init, Fore

# Активуємо colorama
init(autoreset=True)

# Перевірка, чи користувач передав аргумент командного рядка
if len(sys.argv) < 2:
    print("Будь ласка, вкажіть шлях до директорії як аргумент командного рядка.")
    sys.exit(1)

# Беремо шлях до директорії з аргументу
dir_path = Path(sys.argv[1])

# Перевірка, чи шлях існує і чи це директорія
if not dir_path.exists():
    print(f"Шлях {dir_path} не існує!")
    sys.exit(1)

if not dir_path.is_dir():
    print(f"{dir_path} не є директорією!")
    sys.exit(1)

# Рекурсивна функція для обходу папок і файлів
def print_directory(path, indent=0):
    for item in path.iterdir():
        if item.is_dir():
            print("  " * indent + Fore.BLUE + f"[DIR] {item.name}")
            print_directory(item, indent + 1)
        else:
            print("  " * indent + Fore.GREEN + item.name)

# Викликаємо функцію для виводу структури директорії
print_directory(dir_path)