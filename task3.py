string = input()
lst = string.split()
nword = len(lst)
newstring = ""
for i in range(nword):
    word = lst[i]
    nchar = len(word)
    newword = ""
    for j in range(1, nchar + 1):
        newword += word[-j]
    newstring += newword
    if i != nword - 1:
        newstring += " "
print(newstring)
