# Напишите программу, которая получает на вход две строки, и формирует из них словарь. 
# Ключами служат слова из первой строки, значениями – целые числа из второй.
# Пример ввода
# яблоки сливы груши персики манго киви апельсины
# 34 56 23 89 55 32 11
a, b = input() + ' ', input() + ' '
a1, b1 = [], []
strr = ''
for i in range(len(a)):
    if a[i] == ' ':
        a1.append(strr)
        strr = ''
    else: strr += a[i]
strr = ''
for i in range(len(b)):
    if b[i] == ' ':
        b1.append(strr)
        strr = ''
    else: strr += b[i]
my_dict = {}
for i in range(len(a1)):
    my_dict[a1[i]] = b1[i]
print(my_dict)
