"""2. Сформувати функцію, що визначатиме чи є задане натуральне число простим.
Простим називається число, що більше за 1 та не має інших дільників, окрім 1 та самого
себе)."""


def prime(n, j=2):
    if n < 2:
        return "Non-prime"
    if n == j:
        return 'Prime'
    if n % j == 0:
        return "Non-prime"
    return prime(n, j + 1)


print(prime(int(input("Enter a natural number to check: "))))
