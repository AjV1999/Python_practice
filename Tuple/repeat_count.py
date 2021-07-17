tup = tuple(input("Enter tuple values: "))
a = []
for i in tup:
    if i not in a:
        if tup.count(i) > 1:
            a.append(i)
            print(i, "is repeated:", end = " "), print(tup.count(i), "times")