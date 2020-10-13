def gen(num):
    current = 0
    a, b = 0, 1
    while current < num:
        if a % 2 == 0:
            yield a
            current += 1
        a, b = b, a + b


def f(num):
    ans = [i for i in gen(num)]
    return ans


answer = f(4)
print(answer)
