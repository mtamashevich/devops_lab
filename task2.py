n = input()
m = len(n) // 2
for i in range(1, m+1):
    if n[i-1] == n[-i]:
        a = True
    else:
        a = False
        break
if a == True:
    print("yes")
else:
    print("no")
