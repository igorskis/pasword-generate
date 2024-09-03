import random

digits = '1234567890'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

cp = int(input('Кол-во паролей '))
lp = int(input("Длина поролей "))
d = input("Включить цифры? ")
ul = input("Заглавные буквы? ")
ll = input("Строчные буквы? ")
z = input("Знаки? ")
n = input("Не добавлять символы il1Lo0O? ")



if d.lower() == 'y':
    chars += digits
if ll.lower() == 'y':
    chars += lowercase_letters
if ul.lower() == 'y':
    chars += uppercase_letters
if z.lower() == 'y':
    chars += punctuation
if n.lower() == 'y':
    for c in 'il1Lo0O':
        chars.replace(c,'')

def generate_password(l, c):
    password = ''
    for i in range(l):
        password += random.choice(c)
    return password


for k in range(cp):
    print(generate_password(lp, chars))
