def ppp(num):
    def wr(num2=None):
        nonlocal num
        if num2 is None:
            return num
        num += num2
        return wr

    return wr


def ppp1(num):
    def wr(num2=None):
        nonlocal num
        try:
            num2 = int(num2)
        except TypeError:
            return num
        num += num2
        return wr

    return wr


def ppp2(num):
    def wr(num2=None):
        try:
            num2 = int(num2)
        except TypeError:
            return wr.res
        wr.res += num2
        return wr
    wr.res = num
    return wr


def ppp3(num):
    def wr(num2=None):
        logic = {
            type(None): wr.res,
            int: num2
        }
        wr.res += logic[type(num2)]
        return wr.res
    wr.res = num
    return wr


def ppp4(num):
    def wr(num2=None):
        def inner():
            wr.res += num2
            return wr
        logic = {
            type(None): lambda: wr.res,
            int: inner
        }

        return logic[type(num2)]()
    wr.res = num
    return wr


class ppp4:
    def __init__(self, num):
        self._num = num

    def __call__(self, value=0):
        return ppp4(self._num + value)

    def __str__(self):
        return str(self._num)

class ppp3(int):
    def __call__(self, add=0):
        return ppp3(self + add)

# print(ppp(5)(89)())

# print(ppp1(5)(89)())

# print(ppp2(5)(89)())

# print(ppp3(5)(89))

# print(ppp4(5)(89)())

# print(ppp4(5)(90))

print(1 + ppp3(5)(90))