def f(n):
    if (n == 0): return 1
    n = abs(n)
    count = 0
    while (n > 0):
        count += 1
        n //= 10
    return count

def rc2(m):
    if (not(isinstance(m, int)) or (m < 0)): return False
    start = 0
    while True:
        count = 0
        for n in range(start, start+3):
            count += f(n)
        if (count > 9): break
        start += 1
    return (m == start)

print (rc2(998))