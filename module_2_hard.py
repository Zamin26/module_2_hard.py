def password(n):
    result = ""
    for i in range(1, n):
        for j in range(i+1, n):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result

n = int(input('Введите число от 3 до 20: '))
result = password(n)
print('Пароль:', result)