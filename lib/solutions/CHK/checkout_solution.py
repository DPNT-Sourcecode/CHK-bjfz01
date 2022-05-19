

# noinspection PyUnusedLocal
# skus = unicode string
items = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}


def get_remainder(value, divisor) -> int | int:
    if value == 0:
        return 0, 0
    return value // divisor, value % divisor


def discount_a(skus) -> int:
    res, rem = get_remainder(skus.count('A'), 5)
    discount = res * items['A']

    res, rem = get_remainder(rem, 3)
    discount += res * 20

    return discount


def discount_b(skus) -> int:
    res, rem = get_remainder(skus.count('B'), 2)
    return res * 15


def discount_e(skus) -> int:
    res, rem = get_remainder(skus.count('E'), 2)
    return res * items['B']


def apply_offers(skus) -> int:
    return discount_a(skus) + discount_b(skus) + discount_e(skus)


def checkout(skus):
    if len(skus) == 0:
        return 0
    if all(c in items.keys() for c in skus):
        total = 0
        for c in skus:
            total += items[c]
        discount = apply_offers(skus)
        return total - discount
    else:
        return -1