import time

def naive_way():
    ssum = 0
    for i in range(1, 1000):
        if not i % 3 or not i % 5:
            ssum += i

    return ssum

def pythonic_way():
    return sum((n for n in range(1000) if not n % 3 or not n % 5))

def math_way():
    partial = (0 + 999) * (999 / 3) / 2 + (0 + 995) * (995 / 5) / 2
    partial -= (0 + 999) * (990 / 15) / 2
    return partial


if __name__ == '__main__':
    print naive_way()
    print pythonic_way()
    print math_way()

    t1 = time.time()
    for i in range(100 * 1000):
        naive_way()
    print time.time() - t1
    t2 = time.time()
    for i in range(100 * 1000):
        pythonic_way()
    print time.time() - t2
    t3 = time.time()
    for i in range(100 * 1000):
        math_way()
    print time.time() - t3
