string = input("Введите строку: ").lower() # Получаем строку от пользователя и переводим в нижний регистр
index = 0 #  index будет использоваться для подсчета индексов символов
for char in string: # Проходим по каждому символу строки
    if char == 'е': # Проверяем, является ли символ буквой 'е'
        print(f"Буква 'е' найдена на индексе: {index}") # Выводим индекс, если символ равен 'е'
    index += 1 # Переходим к следующему символу