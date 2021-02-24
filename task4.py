n = int(input())
q = -1
if n <= 9:
    q = (10 + n)
else:
    for i in range(2, 10):
        if (n % i == 0) & (n // i < 10):
            q = i * 10 + n // i
            break
print(q)
