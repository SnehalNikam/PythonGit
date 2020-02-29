a = int (input("Enter a no for a = "))
b = int (input("Enter a no for b = "))
c = int (input("Enter a no for c = "))
if a > b:
    if a > c:
        print("A is greater")
    else:
        print("C is greater")
else:
    if b > c:
        print("B id greater")
    else:
        print("C is greater")