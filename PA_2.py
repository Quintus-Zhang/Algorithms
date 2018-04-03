def count_split_inv(b, c):
    n = len(b) + len(c)
    n_b = len(b)
    d = []
    i = 0
    j = 0
    inv_count = 0

    for k in range(n):
        # if b(c) is exhausted, add remaining elements in c(b) to d
        if i == len(b):
            d.extend(c[j:])
            break
        elif j == len(c):
            d.extend(b[i:])
            break

        if b[i] < c[j]:
            d.append(b[i])
            i += 1
        elif c[j] < b[i]:
            d.append(c[j])
            j += 1
            inv_count += n_b - i   # count number of inversions while merge sorting
    return d, inv_count


#
def sort_and_count(a):
    n = len(a)

    if n == 1:
        return a, 0
    else:
        b, x = sort_and_count(a[:(n+1) // 2])   # 1,2,3,4,5 / n+1=6 / (n+1)//2=3 / left half: 1,2,3
        c, y = sort_and_count(a[(n+1) // 2:])
        d, z = count_split_inv(b, c)
    return d, (x + y + z)

# test cases
# a = [1, 3, 5, 2, 4, 6]
# a = [37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, 33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, 31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45]
# a = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84, 6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91, 35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 13, 29, 38, 16, 88, 61, 31, 85, 33, 54 ]

# read the text file
with open('IntegerArray.txt', 'r') as f:
    a = f.readlines()

for i, v in enumerate(a):
    a[i] = int(v)

d, num_inv = sort_and_count(a)
print(num_inv)