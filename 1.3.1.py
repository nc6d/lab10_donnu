"""1.3.1. Сформувати функцію, що буде обчислювати факторіал заданого користувачем
натурального числа n."""
import timeit


# recursion method
def factorial_rec(n):
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n - 1)


# iteration method
def factorial_iter():
    n = int(input('Enter an digit: '))
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    print('The factorial is', factorial)


check = input('Enter 1 to use recursion and 2 to use iteration: ')

if check == '1':
    print('The factorial is', factorial_rec(int(input('Enter an digit: '))))
elif check == '2':
    factorial_iter()

# Execution time
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Program was executed by {t} seconds")
