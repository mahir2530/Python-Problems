marks=[]

a=int(input("enter a marks :- " ))
b=int(input("enter a marks :- " ))
c=int(input("enter a marks :- " ))
d=int(input("enter a marks :- " ))
e=int(input("enter a marks :- " ))

marks.append(a)
marks.append(b)
marks.append(c)
marks.append(d)
marks.append(e)

print("the marks :- " ,marks)
print("---THE SORTED MARKS---")
marks.sort()
print("the marks :- " ,marks)
