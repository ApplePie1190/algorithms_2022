"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""

def even_odd(number, even=0, odd=0):
    if number == 0:
        return even, odd
    else:
        tmp_number = number % 10
        number = number // 10
        if tmp_number % 2 == 0:
            even += 1
        else:
            odd += 1
        return even_odd(number, even, odd)


if __name__ == '__main__':
    user_number = int(input('Введите число: '))
    print(f'Количество четных и нечетных цифр в числе {user_number}: {even_odd(user_number)}')



