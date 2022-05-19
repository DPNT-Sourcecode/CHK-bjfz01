

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if len(skus) == 0:
        return 0
    if all(c in "ABCD" for c in skus):
        a = skus.count('A') * 50 if 0 < skus.count('A') < 3 else (skus.count('A') // 3 * 130) + (skus.count('A') % 3 * 50)
        b = skus.count('B') * 30 if 0 < skus.count('B') < 2 else (skus.count('B') // 2 * 45) + (skus.count('B') % 2 * 30)
        c = skus.count('C') * 20
        d = skus.count('D') * 15
        return a + b + c + d
    else:
        return -1
