def gcd(x, y):
    if x > y:
        return gcd(y, x)
    elif x == 0:
        return y
    elif not x & 1 and not y & 1:
        return gcd(x >> 1, y >> 1) << 1
    elif not x & 1 and y & 1:
        return gcd(x >> 1, y)
    elif x & 1 and y & 1:
        return gcd(x, y >> 1)
    return gcd(x, y - x)

def test_gcd():
    assert gcd(3, 2) is 1
    assert gcd(100, 20) is 20
    assert gcd(30, 25) is 5

if __name__ == '__main__':
    test_gcd()