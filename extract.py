def f(x): return x % 2 != 0 and x % 3 != 0
list_1 = [1,12,13,21,6,5,4,9,11,18,27,3,0]
prifil = filter(f, list_1)
print(list(prifil))


pri = map(f, list_1)
pri = list(pri)

print(pri)