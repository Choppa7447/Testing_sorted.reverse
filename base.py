x = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for miss in x:
    if miss < 5:
        print(miss)

b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
d = list(set(b)&set(c))
d.reverse()
print(d)

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print(result)



