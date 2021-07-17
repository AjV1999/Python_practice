l = []
n = int(input("Enter number of elements: "))
for i in range(0,n):
    ele = int(input("Enter a value: "))
    l.append(ele)
if(len(l) < 2):
    print(l)
else:
    l.sort()
    print("Second smallest number: ", l[1])