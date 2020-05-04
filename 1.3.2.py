"""2. Сформувати функцію для обчислення цифрового кореню натурального числа.
Цифровий корінь отримується наступним чином: необхідно скласти всі цифри заданого
числа, потім скласти всі цифри знайденої суми і повторювати процес до тих пір, поки
сума не буде дорівнювати однозначному числу, що і буде цифровим коренем заданого
числа."""

# Calculating the sum of digits:
def dig_sum(n):
    if n < 10:
        return n
    else:
        return n % 10 + dig_sum(n // 10)


# Calculating an digital root:
def dig_root(n):
    if n < 10:
        return n
    else:
        return dig_root(dig_sum(n))


print("Digital root equals: ", dig_root(n=int(input('Enter an digit: '))))
