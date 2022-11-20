def calcsis(b,n):
    if b !=16:
        return sum([int(n[-1-i]) * b**i for i in range(len(n))])
    else:
        s = list()
        for i in range(len(n)):
            if n[-1 - i] not in {'A', 'B', 'C', 'D', 'E', 'F'}:
                s.append(int(n[-1 - i]) * b**i)
            else:
                s.append((ord(n[-1 - i]) - 55) * b**i)
        return sum(s)  
print('Калькулятор запущен')
while True:
    print('Введите основание, введите число')
    base, number = int(input()), input()
    print('Перевод в 10-ную систему =', calcsis(base, number))
    output = input('Для завершения нажмите ex и ENTER\nВ противном случае нажмите ENTER\n')
    if output == 'ex':
        break