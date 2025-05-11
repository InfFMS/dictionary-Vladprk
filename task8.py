# Представьте, что вы шпионы)
# Придумайте шифр, в котором буквы заменяются на какие-то символы
# и реализуйте шифроватор и дешифроватор

def coding(x):
    strr = ''
    for i in range(len(x)):
        strr += key_code1[x[i]]
    print(strr)


def decoding(x):
    strr = ''
    for i in range(len(x)):
        strr += key_code2[x[i]]
    print(strr)


action = input()
inp = input()
key_code1 = {}
key_code2 = {}
a1 = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
      'ц', 'ч', 'ш', 'щ', 'э', 'ю', 'я']
b1 = ["A", "b", "7", "#", "x", "T", "1", "g", "8", "%", "Q", "J", "w", "3", "p", "m", "L", "5", "&", "z", "C", "R", "k",
      "9", "*", "S", "e", "0", "Y", "F", "t", "D", "4", "h"]
for i in range(len(a1)):
    key_code1[a1[i]] = b1[i]
for i in range(len(a1)):
    key_code2[b1[i]] = a1[i]
if action == 'шифровка':
    coding(inp)
if action == 'дешифровка':
    decoding(inp)
