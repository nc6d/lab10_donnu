"""1. Сформувати функцію для введення з клавіатури послідовності чисел і виведення
її на екран у зворотному порядку (завершаючий символ послідовності – крапка)"""


# reverse entered string
def reverse(s):
    if len(s) == 1:
        return s[0]
    else:
        return s[len(s) - 1] + reverse(s[0:len(s) - 1])


# enter elements till dot will be not detected
arr = []
item = 0
k = 0
while item != '.':
    k += 1
    item = input(f'Enter element #{k}: ')
    arr.append(item)

# reformatting data to present
print(''.join(map(str, arr)))
print(reverse(arr))
