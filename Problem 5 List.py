l1 = []
l2=[5,7,1,2,3,6]
name = str(input("Enter name: "))
roll = int(input("Enter roll: "))
l1.append(name)
l1.append(roll)
l2.pop(1)
print(l2)
print("Original list: ", l1)
print("REVERSED")
l2.reverse()
print(l2)
print("============")

print("sorted")
l2.sort()
print(l2)
