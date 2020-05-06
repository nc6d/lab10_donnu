"""1.3.2. Сформувати функцію для обчислення цифрового кореню натурального числа.
Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
числа."""
import timeit


# recursion method
# Calculating the sum of digits:
def dig_sum(n):
    if n < 10:
        return n
    else:
        return n % 10 + dig_sum(n // 10)


# Calculating an digital root:
def dig_root_rec(n):
    if n < 10:
        return n
    else:
        return dig_root_rec(dig_sum(n))


# Using an iteration method:
def dig_root_iter():
    n = int(input('Enter an digit: '))
    while n > 9:
        i = int(n % 10)
        n = n // 10
        n = n + i
    print("Digital root equals: ", n)


check = input('Press 1 to use recursion and 2 to use iteration: ')
if check == '1':
    print("Digital root equals: ", dig_root_rec(n=int(input('Enter an digit: '))))
elif check == '2':
    dig_root_iter()

# Execution time
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Program was executed by {t} seconds")
