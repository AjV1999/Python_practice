i = input("Enter a number: ")
if i.isalpha():
    print(i, "Is a string")
elif i.isdigit():
    if i == "0":
        print(i, "Is zero")
    else:
        print(i, "Is an real number")
elif "." in i:
    print(i, "Is a floating number")
elif "i" in i:
    print(i, "Is a Complex number")
else:
    print("Invalid input")