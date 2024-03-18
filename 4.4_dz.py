def parse_input(user_input):
    # Розбиваємо введений рядок на слова та зберігаємо перше слово як команду,
    # а решту як аргументи.
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower() # Видаляємо зайві пробіли та переводимо команду в нижній регістр.
    return cmd, *args # Повертаємо команду та аргументи.

def add_contact(args, contacts):
    name, phone = args # Розпаковуємо аргументи.
    contacts[name] = phone # Додаємо новий контакт до словника контактів.
    return "Contact added." # Повертаємо повідомлення про успішне додавання контакту.

def change_contact(args, contacts):
    name, phone = args # Розпаковуємо аргументи.
    if name in contacts: # Перевіряємо, чи існує контакт з таким ім'ям.
        contacts[name] = phone # Змінюємо номер телефону для вказаного контакту.
        return "Contact changed" # Повертаємо повідомлення про успішну зміну контакту.
    else:
        return "This contact is not listed" # Повертаємо повідомлення про те, що вказаний контакт не знайдено.

def show_contact(args, contacts):
    name = args[0] # Отримуємо ім'я контакту з аргументів.
    try:
        return contacts[name] # Повертаємо номер телефону для вказаного контакту.
    except:
        return "This contact is not listed" # Повертаємо повідомлення про те, що вказаний контакт не знайдено.

def main():
    # Створюємо порожній словник для зберігання контактів.
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ") # Отримуємо введення користувача.
        command, *args = parse_input(user_input) # Розбираємо введене користувачем рядок на команду та аргументи.

        # Перевіряємо команду та викликаємо відповідну функцію для її обробки.
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            print(show_contact(args, contacts))
        else:
            print("The assistant bot does not support this command")

if __name__ == "__main__":
    main()
