slices = int(input("Enter the number of slices: "))
if slices % 2 == 0:
    cost = slices * 120
else:
    cost = slices *123
print("Cost of pizza: ", cost)