# Создайте программу-переводчик, которая хранит перевод
#  слов с русского языка на английский.
# После запуска программа выводит список слов в словаре 
# и предлагает пользователю ввести слово для перевода. 
# Если введенного слова нет в словаре выводится сообщение "нет такого слова".
# Используйте словари для словаря :)
my_dict = {'яблоко': 'apple', 'груша': 'pear'}
print(f'Какое слово вы хотели бы перевести: {list(my_dict.keys())}?')
a = input()
print(my_dict.get(a, 'нет такого слова'))
