# Задача 1: Подсчет символов
string = input("Введите строку: ")
char = input("Введите символ: ")
count = string.count(char)
print(f"Символ '{char}' встречается {count} раз(а)")


# Задача 2: Проверка начала и конца
filename = input("Введите название файла: ")
if filename.startswith("IMG_"):
    print("Название начинается с IMG_")
else:
    print("Название не начинается с IMG_")

if filename.endswith(".jpg") or filename.endswith(".png"):
    print("Название заканчивается на .jpg или .png")
else:
    print("Название не заканчивается на .jpg или .png")


# Задача 3: Поиск первого вхождения
text = "Автоматизация - это ключ к эффективности."
word = "ключ"
position = text.find(word)
if position != -1:
    print(f"Слово '{word}' найдено на позиции {position}")
else:
    print(f"Слово '{word}' не найдено")


# Задача 4: Удаление лишних пробелов
user_input = input("Введите строку с пробелами: ")
cleaned = user_input.strip().upper()
print(cleaned)


# Задача 5: Замена символов
ip_with_dashes = input("Введите IP-адрес с тире: ")
correct_ip = ip_with_dashes.replace("-", ".")
print(correct_ip)


# Задача 6: Поиск последнего вхождения
file_path = "/home/user/documents/report_final.docx"
last_slash_index = file_path.rfind("/")
filename = file_path[last_slash_index + 1:]
print(f"Имя файла: {filename}")


# Задача 7: Проверка и исправление email-адреса
email = input("Введите email: ").strip()

if email.count("@") != 1:
    print("Ошибка: email должен содержать ровно один символ @")
elif not (email.endswith(".com") or email.endswith(".ru")):
    print("Ошибка: домен должен заканчиваться на .com или .ru")
else:
    at_index = email.find("@")
    if at_index == 0 or at_index == len(email) - 1:
        print("Ошибка: символ @ не может быть в начале или конце")
    else:
        print("Адрес корректный")