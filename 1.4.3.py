"""3. Сформувати функцію для переведення натурального числа з десяткової системи
числення у шістнадцятирічну."""


def hex_converter(num):
    num, modulo = num // 16, all_digs[num % 16]
    if num:
        return hex_converter(num) + modulo
    return modulo


all_digs = "0123456789ABCDEF"  # all possible symbols of hex system
n = int(input('Enter a digit to convert: '))
print(n, 'in decimal =', hex_converter(n), 'in hex system')
