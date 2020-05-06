"""1.4.1. Сформувати функцію для введення з клавіатури послідовності чисел і виведення
її на екран у зворотному порядку (завершаючий символ послідовності – крапка)"""
import timeit


# recursion method
# reverse entered string
def reverse_rec(s):
    if len(s) == 1:
        return s[0]
    else:
        return s[len(s) - 1] + reverse_rec(s[0:len(s) - 1])


# iteration method
def reverse_iter(s):
    line = ""
    for i in s:
        line = i + line
    return line


# enter elements
# till dot will be not detected
arr = []
item = 0
k = 0
while item != '.':
    k += 1
    item = input(f'Enter element #{k}: ')
    arr.append(item)

print('Default order:\n', ''.join(map(str, arr)))

check = (input("Enter 1 to use recursion and 2 to use iteration: "))
if check == "1":
    print('-' * 30, '\n', 'Default order:\n', ''.join(map(str, arr)))
    print('\n', 'Reversed order:\n', reverse_rec(arr))
elif check == '2':
    print('-' * 30, '\n', 'Default order:\n', ''.join(map(str, arr)))
    print('\n', 'Reversed order:\n', reverse_iter(arr))

# Execution time
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Program was executed by {t} seconds")
