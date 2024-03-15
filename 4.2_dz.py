def get_cats_info(path):
    try:
        cats_info = []

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_info = {"id": cat_id, "name": name, "age": age}
                cats_info.append(cat_info)

        return cats_info

    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None

# Приклад використання функції
cats_info = get_cats_info("path/to/cats_file.txt")
if cats_info is not None:
    print(cats_info)
