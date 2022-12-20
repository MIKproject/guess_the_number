from random import *

n = 1
while n > 0:
    print('Добро пожаловать в числовую угадайку')
    x = int(input('Генерация чисел с 1 по: '))
    random_number = randint(1, x)
    counter = 0
    
    
    def is_valid(num):
        return num.isdigit() and int(num) in range(1, x + 1)
    
    
    while True:
        n = input(f'Введите число от 0 до {x} включительно: ')
        counter += 1
        if is_valid(n):
            n = int(n)
            if n < random_number:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            if n > random_number:
                print('Ваше число больше загаданного, попробуйте еще разок')
            if n == random_number:
                print('Вы угадали, поздравляем!')
                print(f'Вы угадали с {counter} попытки')
                break
        else:
            print(f'А может быть все-таки введем целое число от 1 до {x}? ')
            continue
    
    s = int(input('Желаеете повторить? 1 - ДА / 0 - НЕТ: '))
    n = s
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')