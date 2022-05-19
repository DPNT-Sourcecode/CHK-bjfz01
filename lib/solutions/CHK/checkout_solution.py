

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
    return 0


def discount_b(skus) -> int:
    return 0


def discount_e(skus) -> int:
    return 0


def apply_offers(skus) -> int:
    return discount_a(skus) + discount_b(skus) + discount_e(skus)


def checkout(skus):
    if len(skus) == 0:
        return 0
    if all(c in "ABCD" for c in skus):
        # a = skus.count('A') * 50 if 0 < skus.count('A') < 3 else (skus.count('A') // 3 * 130) + (skus.count('A') % 3 * 50)
        # b = skus.count('B') * 30 if 0 < skus.count('B') < 2 else (skus.count('B') // 2 * 45) + (skus.count('B') % 2 * 30)
        # c = skus.count('C') * 20
        # d = skus.count('D') * 15
        total = 0
        for c in skus:
            total += items[c]
        discount = apply_offers(skus)
        return total - discount
    else:
        return -1
