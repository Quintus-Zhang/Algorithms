def partition(a, l, r):
    """return the index of pivot

    --------------------------------------------------------
    Invariant:
    all elements between the pivot and i are less than the pivot, and
    all elements between the i and j are greater than the pivot
    --------------------------------------------------------

    i points to the first element greater than the pivot
    j points to the next element to be compared with the pivot

    pivot is fixed until partitioning is done

    """
    p = a[l]    # use the leftmost element as the pivot
    i = l + 1
    for j in range(l + 1, r + 1):
        if a[j] < p:
            a[j], a[i] = a[i], a[j]
            i += 1
    a[l], a[i-1] = a[i-1], a[l]  # swap pivot element to the rightful position

    return i - 1


def quick_sort(a, l, r):
    global count
    if l >= r:
        return

    # # use the last element as the pivot (2)
    # a[l], a[r] = a[r], a[l]

    # # use the "median-of-three" pivot rule (3)
    # m_idx = l + (r - l) // 2
    # # a[m_idx] is the median
    # if a[l] <= a[m_idx] <= a[r] or a[r] <= a[m_idx] <= a[l]:
    #     a[l], a[m_idx] = a[m_idx], a[l]
    # # a[r] is the median
    # elif a[m_idx] <= a[r] <= a[l] or a[l] <= a[r] <= a[m_idx]:
    #     a[l], a[r] = a[r], a[l]
    # else:
    #     pass

    j = partition(a, l, r)
    count += r - l         # count the number of comparisons
    quick_sort(a, l, j-1)
    quick_sort(a, j+1, r)


# read the text file
with open('QuickSort.txt', 'r') as f:
    a = f.readlines()

for i, v in enumerate(a):
    a[i] = int(v)

l = 0
r = len(a)-1
count = 0
quick_sort(a, l, r)
print(a)
print(count)