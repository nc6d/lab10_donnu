"""1.4.2. Сформувати функцію, що визначатиме чи є задане натуральне число простим.
Простим називається число, що більше за 1 та не має інших дільників, окрім 1 та самого
себе)."""
import timeit
from math import sqrt


# recursion method
def prime_rec(n, j=2):
    if n < 2:
        return "Non-prime"
    if n == j:
        return 'Prime'
    if n % j == 0:
        return "Non-prime"
    return prime_rec(n, j + 1)


# iteration method
def prime_iter(n, j=2):
    if n < 2:
        return "Non-prime"
    if n == j:
        return "Prime"
    scope = sqrt(n)
    while j <= scope:
        if n % j == 0:
            return "Non-prime"
        j += 1
    return 'Prime'


check = input("Enter 1 to use recursion and 2 to use iteration: ")
if check == '1':
    print(prime_rec(int(input("Enter a natural number to check: "))))
elif check == '2':
    print(prime_iter(int(input("Enter a natural number to check: "))))

# Execution time
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Program was executed by {t} seconds")
