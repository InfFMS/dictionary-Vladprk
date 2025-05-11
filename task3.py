# Напишите программу, которая получает на вход строку и подсчитывает, 
# сколько раз в ней встречается каждый символ (независимо от регистра).
# Результат нужно вывести без фигурных скобок
# Пример. 
# ввод:
# Абракадабра
# Вывод
# а-5 б-2 д-1 к-1 р-2
a_1 = input()
a = a_1.lower()
letters = ''
count = []
for i in range(len(a)):
    if letters.find(a[i]) == -1:
        letters += a[i]
        count.append(1)
    else:
        count[letters.find(a[i])] += 1
answer = ''
for i in range(len(letters)):
    answer += f'{letters[i]}-{count[i]} '
print(answer)
