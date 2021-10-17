# Данный модулб является минипроектом
import random

print()
print('Добро пожаловать в числовую угадайку!')
k = int(input('Введите максимальное значение для нашей игры: '))
print('Значение загадано!')
n = random.randint(1, k)


def is_valid(z, i):
    if not z.isdigit():
        return False
    else:
        if 0 < int(z) < i + 1:
            return True
        else:
            return False


m = str(0)
flag = False
cnt = 0

while not flag:
    m = input('Введите предполагаемое значение: ')
    if not is_valid(m, k):
        print('А может быть все-таки введем число от 1 до 100?')
    else:
        cnt += 1
        m = int(m)
        if m < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            print()
        elif m > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
            print()
        else:
            print()
            print('Вы угадали за', cnt, 'попыток поздравляем!')
            flag = True

print('Спасибо что играли в числовую угадайку. Еще увидимся!')
