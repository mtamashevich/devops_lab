n = int(input())
s = "".split()
sum1 = 0
sum2 = 0
for i in range(n):
    s += input().split()
for i in range(0, n * n, n + 1):
    sum1 += int(s[i])
# print(sum1)
for i in range(n - 1, n * n - 1, n - 1):
    sum2 += int(s[i])
# print(sum2)
print(abs(sum1 - sum2))
