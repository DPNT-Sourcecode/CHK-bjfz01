

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if len(skus) == 0:
        return -1
    if all(c in "ABCD" for c in skus.upper()):
        s = skus.upper()
        a = 50 if 0 < s.count('A') < 3 else s.count('A') * 50
        b = 30 if 0 < s.count('B') < 2 else s.count('B') * 30
        c = s.count('C') * 20
        d = s.count('D') * 15
        return a + b + c + d
    else:
        return -1



