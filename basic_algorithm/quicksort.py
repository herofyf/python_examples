
x=[1, 4, 8, 7]
#x = [1, 4, 8, 7, 12, 5]
x=[1, 14, 8, 9, 12,5,45]
'''
 这个算法用i, j来表示状态
'''
def quicksort_1(x, left, right):
    i = left
    j = right
    mid_v = x[int((i + j) / 2)]
    while i <= j:
        while x[i] < mid_v:
            i += 1
        while x[j] > mid_v:
            j -= 1
        if (i <= j):
            x[i], x[j] = x[j], x[i]
            i += 1
            j -= 1

    print(x[left: right + 1], ' ', mid_v)
    if j > left:
        quicksort_1(x, left, j)
    if i < right:
        quicksort_1(x, i, right)

#quicksort_1(x, 0, len(x) -1)

x = [4, 3, 1, 5]
def quicksort_2(x, left, right):
    i = left
    j = right
    pivot = x[right]
    while i <= j:
        while x[i] < pivot and i <= j:
            i += 1
        while x[j] > pivot and j >= 0:
            j -= 1
        if (i <= j):
            x[i], x[j] = x[j], x[i]
            i += 1
            j -= 1
    print(x[left: right + 1], ' ', pivot)
    if j > left:
        quicksort_2(x, left, j)
    if i < right:
        quicksort_2(x, i, right)

quicksort_2(x, 0, len(x) - 1)
for i in x:
    print(i)