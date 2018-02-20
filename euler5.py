from fractions import gcd
def lcm(x,y): return x*y/gcd(x,y)

print reduce(lcm, range(1, 21))

