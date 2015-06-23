#!python3
i = 1
j = 2
s = 2
while (True):
    k = i+j
    if k > 4000000:
        break
    if not (k%2):
        s += k
    i = j
    j = k
print(s)