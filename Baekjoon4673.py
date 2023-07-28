def make_dn(num):
    digits = list(map(int,str(num)))
    dn = num + sum(digits)
    return dn


numbers = list(range(10000))
for n in range(10000):
    try:
        numbers.remove(make_dn(n))
    except:
        continue

for n in numbers:
    print(n)


