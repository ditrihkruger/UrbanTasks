first = int(input("first = "))
second = int(input("second = "))
third = int(input("third = "))
if (first == second) and (second == third):
    print(3)
elif(first == second) or (first == third) or (second == third):
    print (2)
if (first != second) and (second != third) and (first != third):
    print(0)