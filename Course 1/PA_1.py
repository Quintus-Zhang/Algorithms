def count_digits(x):
    if x == 0:
        return 1
    counter = 0

    while x > 0:
        counter += 1
        x = x//10
    return counter


x = 31415926535897932384626433832795028841971693993751058209749445
y = 271828182845904523536028747135266249775724709369995957496696762


def product(x, y):
    n_x = count_digits(x)
    n_y = count_digits(y)
    n = max(n_x, n_y)

    nby2 = n // 2

    if n_x == 1 and n_y == 1:
        return x * y

    a = x // 10 ** nby2
    b = x % 10 ** nby2
    c = y // 10 ** nby2
    d = y % 10 ** nby2

    ac = product(a, c)
    ad = product(a, d)
    bc = product(b, c)
    bd = product(b, d)

    res = 10**(2 * nby2) * ac + 10 ** nby2 * (ad + bc) + bd
    return res


def karatsuba(x, y):
    n_x = count_digits(x)
    n_y = count_digits(y)
    n = max(n_x, n_y)

    nby2 = n // 2  # trick: to use nby2 here

    if n_x == 1 and n_y == 1:
        return x * y

    a = x // 10 ** nby2
    b = x % 10 ** nby2
    c = y // 10 ** nby2
    d = y % 10 ** nby2

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    res = 10**(2 * nby2) * ac + 10 ** nby2 * ad_plus_bc + bd
    return res

