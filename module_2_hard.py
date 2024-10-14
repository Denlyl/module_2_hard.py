def trap(n):
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return f'{n} - {result}\nПоздравляю, тебя не раздавит!!!'

n = int(input('Введите число, если оно будет кратно сумме пары - ты спасен: '))

quest = trap(n)
print(quest)