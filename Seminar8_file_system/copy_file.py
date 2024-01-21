

def copy_file():
    file_number = int(input("Выберит файл, с которым Вы хотите работать\n"
                       "Введите цифру 1 или 2: "))
    while file_number < 1 or file_number > 2:
        file_number = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    source_file_number = f"db/data_{file_number}.txt"

    with open(source_file_number, 'r', encoding='utf-8') as file:
        content = file.read()

    line_number = int(input("Введите номер строки для копирования: "))
    lines = content.split('\n')
    line_to_copy = lines[line_number - 1]

    file_number_second = int(input("Выберите файл, в который хотите скопировать данные\n"
                       "Введите цифру 1 или 2: "))
    while file_number_second < 1 or file_number_second > 2:
        file_number_second = int(input("Ошибка!!!\n"
                           "Введите цифру 1 или 2: "))
    source_file_number_second = f"db/data_{file_number_second}.txt"

    with open(source_file_number_second, 'a+', encoding='utf-8') as file:
        file.write(f'{line_to_copy}\n')

    print('Данные успешно скопированы!')
    file.close()
