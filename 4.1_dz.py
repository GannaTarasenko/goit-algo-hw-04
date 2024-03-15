def total_salary(path):
    try:
        total_salary = 0  # Ініціалізація змінних для підрахунку загальної заробітної плати та кількості розробників
        num_developers = 0

        with open(path, 'r', encoding='utf-8') as file:  # Відкриття файлу для читання
            for line in file:  # Прохід по кожному рядку у файлі
                name, salary = line.strip().split(',')  # Розділення рядка на ім'я та зарплату
                total_salary += int(salary)  # Додавання зарплати до загальної суми
                num_developers += 1  # Інкрементування лічильника розробників

        average_salary = total_salary / num_developers  # Обчислення середньої заробітної плати
        return total_salary, average_salary  # Повернення загальної суми та середньої заробітної плати

    except FileNotFoundError:  # Обробка винятку, якщо файл не знайдено
        print("Файл не знайдено.")
        return None, None  # Повернення None для обох значень у випадку винятку
    except Exception as e:  # Обробка інших можливих винятків
        print(f"Сталася помилка: {e}")
        return None, None  # Повернення None для обох значень у випадку винятку

# Приклад використання функції
total, average = total_salary("path/to/salary_file.txt")  # Виклик функції зі шляхом до файлу
if total is not None and average is not None:  # Перевірка чи функція повернула коректні значення
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
