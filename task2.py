# Напишите программу, которая получает на вход строку чисел, разделенных пробелами, и формирует словарь,
#  в котором ключами служат числа, а значениями – слово "четное" или "нечетное".
a = input() + ' '
a1, b1 = [], []
my_dict = {}
strr = ''
for i in range(len(a)):
    if a[i] == ' ':
        if int(strr) % 2 == 0:
            b1.append('чётное')
        else:
            b1.append('нечётное')
        a1.append(strr)
        strr = ''
    else: strr += a[i]
for i in range(len(a1)):
    my_dict[a1[i]] = b1[i]
print(my_dict)