s1 = "hello to python"
print('Convert first character to uppercase: ', s1.capitalize())

s2 = 'o'
print('Count occurrences of substring "o" from index 3 to 15: ', s1.count(s2, 3, 15))

s3 = 'l'
print('Count occurrences of substring "l": ', s1.count(s3))

s4 = 'python'
print('Check if the string ends with "python" (True/False): ', s1.endswith(s4))

s5 = 'o'
print('Check if the string ends with "o" from index 2 to 13 (True/False): ', s1.endswith(s5, 2, 13))

print('Find index of first occurrence of "o": ', s1.find(s5))
print('Find index of first occurrence of "l" from index 1 to 10: ', s1.find(s3, 1, 10))

print('Check if the string is alphanumeric (s1): ', s1.isalnum())

s6 = 'aaaaaa'
print('Check if the string is alphanumeric (s6): ', s6.isalnum())

t = '111'  # t should be a string to use isalpha method
print('Check if all characters in the string are alphabets (t): ', t.isalpha())
print('Check if all characters in the string are alphabets (s1): ', s1.isalpha())

s7 = '12345'
print('Check if all characters in the string are digits (s7): ', s7.isdigit())

s8='Python'
print("Check if all characters in the string are lowercase (s1): ",s1.islower())
print("Check if all characters in the string are lowercase (s8): ",s8.islower())

s9='PYTHON'
print("Check if all characters in the string are uppercase (s9): ",s9.isupper())

print("Return the string in uppercase (s1): ",s1.upper())

print("Return the string in lowercase (s1): ",s1.lower())

s10='                 '
print("Check whitespace (s10): ",s10.isspace())

print("Return length of an object (s10): ",len(s10))
print("Return length of an object (s9): ",len(s9))

s11='Welcome to Python'
print('Swapcase from an object: ',s11.swapcase())

string='abc python abc'
print('Remove leading and trailing whitespace: ',string.strip())

s12='   Hello world '
print('Remove leading character: ', s12.lstrip())

s13='@@@@@@@HEllooooooooo@@@'
print('Remove leading "@" character: ', s13.lstrip('@'))

print('Remove trailing character: ', s12.rstrip())

num=[1,3,2,8,5,10,6]
print('Maximum is: ',max(num))

num=[3,2,8,5,10,6]
print('Minimum is: ',min(num))
