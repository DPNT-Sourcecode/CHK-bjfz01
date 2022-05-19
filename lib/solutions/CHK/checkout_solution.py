

# noinspection PyUnusedLocal
# skus = unicode string
items = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40
}


def get_remainder(value, divisor):
    if value == 0:
        return 0, 0
    return value // divisor, value % divisor


def discount_a(skus) -> int:
    res, rem = get_remainder(skus.count('A'), 5)
    discount = res * items['A']

    res, rem = get_remainder(rem, 3)
    discount += res * 20

    return discount


def discount_b_e(skus) -> int:
    res, rem = get_remainder(skus.count('B'), 2)
    discount_b = res * 15

    discount_e = 0
    b_count = skus.count('B')
    if skus.count('E') >= 2:
        if b_count > 0:
            discount_e = items['B'] * (skus.count('E') // 2)

    if b_count > 2:
        discount = discount_b + discount_e
    else:
        discount = discount_b if discount_b > discount_e else discount_e
    return discount


def apply_offers(skus) -> int:
    return discount_a(skus) + discount_b_e(skus)


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