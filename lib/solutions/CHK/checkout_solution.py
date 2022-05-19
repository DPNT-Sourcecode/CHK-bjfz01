

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if len(skus) == 0:
        return -1
    if all(c in "ABCD" for c in skus.upper()):
        s = skus.upper()
        a = s.count('A') * 50
        b = s.count('B') * 30
        c = s.count('C') * 20
        d = s.count('D') * 15
        return a + b + c + d
    else:
        return -1


