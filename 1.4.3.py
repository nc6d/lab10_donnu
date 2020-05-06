"""1.4.3. Сформувати функцію для переведення натурального числа з десяткової системи
числення у шістнадцятирічну."""
import timeit


# recursion method
def hex_converter_rec(num):
    num, modulo = num // 16, all_digs[num % 16]
    if num:
        return hex_converter_rec(num) + modulo
    return modulo


# iteration method
def hex_converter_iter():
    return hex(n)


all_digs = "0123456789ABCDEF"  # all possible symbols of hex system
n = int(input('Enter a digit to convert: '))

check = input('Enter 1 to use recursion and 2 to use iteration: ')
if check == "1":
    print(n, '=', hex_converter_rec(n))
elif check == '2':
    print(n, '=', ''.join(map(str, hex_converter_iter().replace('0x', '').upper())))

# Execution time
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Program was executed by {t} seconds")
