# Нужно считать файл parameters.txt. 
# Это файл с настройками расчетной модели.
# Формат в файле следующий первое слово в строке - это ключ, 
# потом после пробела - значение (может быть строкой, числом, или набором чисел),
# все, что после символа "//" это комментарий  должно игнорироваться.
# Реализуйте считывание значений из файла и запись этих значений в словарь.
f = open('parameters.txt', 'r', encoding='utf-8')
mas = f.readlines()
a = len(mas)
main_dict = {}
for i in range(len(mas)):
    main_str = mas[i] + '  '
    if main_str != '  ':
        key_i = ''
        j = 0
        while main_str[j] != ' ' and (main_str[j] + main_str[j+1] != '\t') and (main_str[j] + main_str[j+1] != '\n'):
            key_i += main_str[j]
            j += 1
        value_i = ''
        j += 1
        while (main_str[j] != ' ' and not(main_str[j] == '/' and main_str[j+1] == '/') and
               (main_str[j] + main_str[j+1] != '\t') and (main_str[j] + main_str[j+1] != '\n')):
            value_i += main_str[j]
            j += 1
        value_i = value_i.replace('\t', '')
        value_i = value_i.replace('\n', '')
        if value_i != '':
            main_dict[key_i] = value_i
f.close()
print(main_dict)

