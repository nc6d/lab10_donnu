"""3. Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5."""

import random


# Keeping track of current position with the "index" argument and the max item and its position with the "pos_item",
# the base case is the empty array in with case we return what we have and in each iteration reduce the list.

def find_max_pos(array, index=0, pos_item=None, max_index=None):
    if max_index is None:
        max_index = len(array)
    if index >= max_index:
        return pos_item
    item = array[index]
    if pos_item is None:
        return find_max_pos(array, index + 1, (item, index), max_index)
    previous = pos_item[1]
    if previous >= item:
        return find_max_pos(array, index + 1, pos_item, max_index)
    else:
        return find_max_pos(array, index + 1, ('Maximal item: ', item, '\nIndex: ', index), max_index)


# Data to enter
arr = [random.randint(1, 5) ** 2 for x in range(int(input('Enter the length of array: ')))]
print('Generated array:\n', arr)
print(''.join(map(str, find_max_pos(arr))))
