

# noinspection PyUnusedLocal
# skus = unicode string
items = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 70,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 20,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 17,
    'Y': 20,
    'Z': 21
}

any_three_items = {
    'S': 20,
    'T': 20,
    'X': 17,
    'Y': 20,
    'Z': 21
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


def discount_f(skus) -> int:
    f_count = skus.count('F')
    num_free_f = f_count // 3
    return items['F'] * num_free_f


def discount_h(skus) -> int:
    res, rem = get_remainder(skus.count('H'), 10)
    discount = res * 20

    res, rem = get_remainder(rem, 5)
    discount += res * 5

    return discount


def discount_k(skus) -> int:
    res, _ = get_remainder(skus.count('K'), 2)
    return res * 20


def discount_n_m(skus) -> int:
    discount = 0
    m_count = skus.count('M')
    if skus.count('N') >= 3:
        if m_count > 0:
            discount = items['M'] * (skus.count('N') // 3)

    return discount


def discount_p(skus) -> int:
    res, _ = get_remainder(skus.count('P'), 5)
    return res * items['P']


def discount_q(skus) -> int:
    res, _ = get_remainder(skus.count('Q'), 3)
    return res * 10


def discount_r_q(skus) -> int:
    res, _ = get_remainder(skus.count('Q'), 3)
    discount_q = res * 10

    discount_r = 0
    q_count = skus.count('Q')
    if skus.count('R') >= 3:
        if q_count > 0:
            discount_r = items['Q'] * (skus.count('R') // 3)

    discount = 0
    if q_count > 3:
        discount = discount_q + discount_r
    else:
        discount = discount_r if discount_r > discount_q else discount_q

    return discount


def discount_u(skus) -> int:
    u_count = skus.count('U')
    num_free_u = u_count // 4
    return items['U'] * num_free_u


def discount_v(skus) -> int:
    res, rem = get_remainder(skus.count('V'), 3)
    discount = res * 20

    res, rem = get_remainder(rem, 2)
    discount += res * 10

    return discount


def apply_offers(skus) -> int:
    discount = discount_a(skus) + discount_b_e(skus) + discount_f(skus) + discount_h(skus) + discount_k(skus) + discount_n_m(skus) + discount_p(skus) + discount_r_q(skus) + discount_u(skus) + discount_v(skus)
    return discount


def any_three_offer(skus):
    eligible_item_prices = []
    for c in skus:
        if c in any_three_items.keys():
            eligible_item_prices.append(any_three_items[c])
    eligible_item_prices.sort(reverse=True)

    total = 0
    while len(eligible_item_prices) > 2:
        total += 45
        temp = eligible_item_prices[3:]
        eligible_item_prices = temp

    total += sum(eligible_item_prices[:2])
    return total


def checkout(skus):
    if len(skus) == 0:
        return 0
    if all(c in items.keys() for c in skus):
        total = 0
        for c in skus:
            if c not in any_three_items.keys():
                total += items[c]
        discount = apply_offers(skus)
        sum_any_three = any_three_offer(skus)
        return total - discount + sum_any_three
    else:
        return -1


