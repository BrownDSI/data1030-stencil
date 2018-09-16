def foo(x, y, z):
    while x != 0:
        x = (x + y) * z
        y = (y + x) * z

def bar():
    x = y = z = 1

    foo(x, y, z)

bar()

