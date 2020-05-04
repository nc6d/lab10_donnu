"""1. Сформувати функцію, що буде обчислювати факторіал заданого користувачем
натурального числа n."""

def  factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print('The factorial is', factorial(int(input('Enter an digit: '))))
