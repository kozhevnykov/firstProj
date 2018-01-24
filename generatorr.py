import itertools

def primes():
    a=[2]
    t=3
    while True:
        yield a[-1]
        flag=True
        k=0
        while flag:
            if t % a[k] == 0:
                t=t+1
                k=-1
            k += 1
            if k == len(a):
                flag = False
        a.append(t)
        t=t+1

print(list(itertools.takewhile(lambda x : x <= 31, primes())))