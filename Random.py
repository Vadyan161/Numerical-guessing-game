# Данный модулб является минипроектом
import random

n = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку!')


def is_valid(z):
    if not z.isdigit():
        return False
    else:
        if 0 < int(z) < 101:
            return True
        else:
            return False


m = str(0)
flag = False

while not flag:
    m = input('Введите предполагаемое значение: ')
    if not is_valid(m):
        print('А может быть все-таки введем число от 1 до 100?')
    else:
        m = int(m)
        if m < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif m > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            flag = True

print('Спасибо что играли в числовую угадайку. Еще увидимся!')
