from random import randrange, randint
import math as mth

def Lehman(p, m = 50):
    for i in range(1, m):
        a = randint(1, p)
        k = ((a % p) ** ((p - 1) // 2)) % p
        if k != 1 and k != (p - 1):
            return False
    return True


def MillerRabin(n, k = 50):  
	if n == 2:
		return True
	if not n % 2:
		return False # if number is even -- it's composite number

	def check(a, s, d, n):
		x = pow(a, d, n)
		if x == 1:
			return True
		for i in range(s - 1):
			if x == n - 1:
				return True
			x = pow(x, 2, n)
		return x == n - 1

	s = 0
	d = n - 1

	while d % 2 == 0:
		d >>= 1
		s += 1

	for i in range(k):
		a = randrange(2, n - 1)
		if not check(a, s, d, n):
			return False
	return True

accuracy = 1e3
k = 10
for p in range(int(1e6), int(1e8) + 1):
	test_rabin_miller = MillerRabin(p, int(mth.log2(accuracy)/2))
	if test_rabin_miller:
		print('Processed number {0}'.format(p))
		k -= 1
	if not k:
		break