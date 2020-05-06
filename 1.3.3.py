"""1.3.3. Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5."""
import timeit
import random


# recursion method
# Keeping track of current position with the "index" argument and the max item and its position with the "pos_item",
# the base case is the empty array in with case we return what we have and in each iteration reduce the list.

def max_pos_rec(array, index=0, pos_item=None, max_index=None):
    if max_index is None:
        max_index = len(array)
    if index >= max_index:
        return pos_item
    item = array[index]
    if pos_item is None:
        return max_pos_rec(array, index + 1, (item, index), max_index)
    previous = pos_item[1]
    if previous >= item:
        return max_pos_rec(array, index + 1, pos_item, max_index)
    else:
        return max_pos_rec(array, index + 1, ('Maximal item: ', item, '\nIndex: ', index), max_index)


# iteration method
# Using comparisons to assign maximal value to "maximal" variable and defining his index with counter
def max_pos_iter():
    maximal = 0
    index = 0
    for i in range(len(arr)):
        if arr[i] > maximal:
            maximal = arr[i]
            index = i
    print(f'Maximal item: {maximal} \nIndex: {index}')


check = (input("Enter 1 to use recursion and 2 to use iteration: "))

arr = [random.randint(1, 5) ** 2 for x in range(int(input('Enter the length of array: ')))]
print('Generated array:\n', arr)

if check == "1":
    print(''.join(map(str, max_pos_rec(arr))))
elif check == "2":
    max_pos_iter()

# Execution time
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Program was executed by {t} seconds")
