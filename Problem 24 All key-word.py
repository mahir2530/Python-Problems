print("===================| LIST |===================")
list = [1, 2, 3, 4]
a = all(list) 
print("The result for list is : ", a)  

list1 = [1, 2, 3, 0, 4]
b = all(list1)  
print("The result for list1 is : ", b)  

list2 = [0, False]
c = all(list2) 
print("The result for list2 is : ", c)  

list3 = []
d = all(list3)  
print("The result for list3 is : ", d)  

# Strings
print("===================| STRING |===================")
s = 'welcome to python'
print(all(s))  

s = '000'
print(all(s))  

s = ' '
print(all(s))  

# Dictionaries
print("===================| dictionaries |===================")
s = {0: 'False', 1: 'True'}
print(all(s))  

s = {1: 'False', 2: 'True'}
print(all(s)) 

s = {1: 'True', False: 0}
print(all(s)) 

s = {}
print(all(s))  

s = {'0': 'True'}
print(all(s))  
