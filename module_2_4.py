
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:               # При помощи цикла for переберите список numbers.
    if i > 1:                    #
        for j in range(2, i):    #делится ли каждое число на 2, делитель находится число не простое,
                                 #если делителя не нашлось, то число простое
            if (i % j) == 0:    #проверяем, делится ли значение i на j без остатка.
                is_primes = False #проверка переменной если составное число
                break
        else:
            is_primes = True  # проверка переменной простое число
        if is_primes:
            primes.append(i)   #простые записываются
        else:
            not_primes.append(i) # составные записываются
print(f"Primes: {primes}")
print(f"Not_primes: {not_primes}")