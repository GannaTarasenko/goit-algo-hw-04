import sys
from pathlib import Path
from colorama import Fore, Style

def display_directory_structure(directory):
    try:
        directory = Path(directory)
        if not directory.is_dir():
            print(f"{Fore.RED}Помилка: {directory} не є директорією{Style.RESET_ALL}")
            return

        print(f"{Fore.BLUE}Структура директорії {directory}:{Style.RESET_ALL}")

        for item in directory.iterdir():
            if item.is_dir():
                print(f"{Fore.GREEN}📁 {item.name}{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}📄 {item.name}{Style.RESET_ALL}")

                # Виведення файлів без кольору:
                # print(f"📄 {item.name}")

    except Exception as e:
        print(f"{Fore.RED}Сталася помилка: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python script.py шлях_до_директорії{Style.RESET_ALL}")
        sys.exit(1)

    directory_path = sys.argv[1]
    display_directory_structure(directory_path)
