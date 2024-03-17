def get_cats_info(path):
    try:  # Початок блоку спроби
        cats_info = []  # Ініціалізуємо порожній список для зберігання інформації про котів

        with open('cats_file.txt', 'r') as file:  # Відкриваємо файл для читання як file
            for line in file:  # Проходимо через кожен рядок у файлі
                cat_id, name, age = line.strip().split(',')  # Розділяємо рядок на окремі значення та присвоюємо їх cat_id, name і age
                cat_info = {"id": cat_id, "name": name, "age": age}  # Створюємо словник з інформацією про кота
                cats_info.append(cat_info)  # Додаємо словник до списку cats_info

        return cats_info  # Повертаємо список з інформацією про котів

    except FileNotFoundError:  # Обробка винятку, якщо файл не знайдено
        print("Файл не знайдено.")  # Виводимо повідомлення про відсутність файлу
        return None  # Повертаємо None

    except Exception as e:  # Обробка інших винятків
        print(f"Сталася помилка: {e}")  # Виводимо повідомлення про виняток
        return None  # Повертаємо None

# Приклад використання функції
cats_info = get_cats_info("path/to/cats_file.txt")  # Викликаємо функцію get_cats_info з шляхом до файлу
if cats_info is not None:  # Перевіряємо, чи не є результат функції None
    print(cats_info)  # Виводимо інформацію про котів
