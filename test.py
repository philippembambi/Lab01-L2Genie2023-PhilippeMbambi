import itertools

lst = [1,5,8,9,6]
a = lst[0]
for a, b in itertools.combinations(lst, 2):
    print(a, '<' , b, a<b )