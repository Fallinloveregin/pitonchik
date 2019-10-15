import random
lst = []
for i in range(97, 123):
    lst.append(chr(i))
x = int(random.random() * 26)
print(lst[x])