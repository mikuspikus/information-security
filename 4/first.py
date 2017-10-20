from random import randint

def _psrndm_generator(a, c, t, m = 2 ** 16, k = None):
    def generate(a, c, m, t):
        return (a * t + c) % m

    result, new_t  = [t], generate(a, c, m, t)

    while new_t != result[0] or new_t != result[-1]:
        if k != None:
            k -= 1
        result.append(new_t)
        new_t = generate(a, c, m, new_t)
        if not k:
            break

    return result

if __name__ == '__main__':
    for i in range(1, 50 + 1):
        a = randint(0, 100)
        c = randint(0, 100)
        t = randint(0, 100)
        k = len(_psrndm_generator(a, c, t, k = int(1e4)))
        print('{:>3} sequence. a = {:>3}, c = {:>3}, t = {:>3}, k = {:>5}'.format(i, a, c, t, k))