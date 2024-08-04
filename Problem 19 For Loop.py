c=[1,2,3,4,5,6,7,8,9,10]
for i in c:
    print(c)
print('=======================================')
for a in range(4):
    print(a)
print('=======================================')
for a in range(2,7):
    print(a)
print('=======================================')
num=(1,2,3,4,5,6,7,8,9,10,11)
c_odd=0
c_even=0
for x in num:
    if x%2==0:
        c_even+=1
    else:
        c_odd+=1
print('number of even is : ',c_even)
print('number of odd is : ',c_odd)
