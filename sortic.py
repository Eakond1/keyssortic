def sa(a):
    if len(a) > 1:
        c = a[1]
        a[1] = a[0]
        a[0] = c
        return a


def sb(b):
    if len(b) > 1:
        c = b[1]
        b[1] = b[0]
        b[0] = c
        return b


def ss(a, b):
    a = sa(a)
    b = sb(b)
    return a, b


def pa(a, b):
    if len(b) > 0:
        a = a[::-1]
        a.append(b[0])
        a = a[::-1]
        return a


def pb(a, b):
    if len(a) > 0:
        b = b[::-1]
        b.append(a[0])
        b = b[::-1]
        return b


def ra(a):
    a = a[::-1]
    return a


def rb(b):
    b = b[::-1]
    return b


def rr(a, b):
    a = ra(a)
    b = rb(b)
    return a, b


def rra(a):
    if len(a) > 0:
        c = []
        c.append(a[-1])
        for i in range(len(a) - 1):
            c.append(a[i])
        a = c
        return a


def rrb(b):
    if len(b) > 0:
        c = []
        c.append(b[-1])
        for i in range(len(b) - 1):
            c.append(b[i])
        b = c
        return b


def rrr(a, b):
    a = rra(a)
    b = rrb(b)
    return a, b

