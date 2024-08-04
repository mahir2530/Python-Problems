# Initializing variables
a = 10
b = 10

# Using format() to insert variables a and b into the string
print('The value of a is {} and b is {} '.format(a, b))
# Output: The value of a is 10 and b is 10

# Using format() with positional arguments to replace placeholders
print('I like {0} and {1} '.format('chocolate', 'cake'))
# Output: I like chocolate and cake

# Using format() with keyword arguments to replace placeholders
print('Hi {name}, {greeting} '.format(greeting='good morning', name='Tirth'))
# Output: Hi Tirth, good morning

# Formatting a number with a field width of 10 characters
print(' {:10} '.format(12))
# Output: '        12 '

# Formatting a floating-point number with a width of 10 and 3 decimal places
print(' {:10.3f} '.format(12.2346))
# Output: '    12.235 '

# Formatting a number with left-alignment in a field width of 5, padded with zeros
print(' {:<05d} '.format(12))
# Output: '12   ' (Note: Python 3.10+ would output '12000')

# Formatting a floating-point number with a width of 8 and 3 decimal places, forcing a sign
print(' {:=8.3f} '.format(-12.2346))
# Output: '-  12.235'

# Formatting a string with a field width of 5
print(' {:5} '.format('cat'))
# Output: 'cat  '

# Formatting a string with right-alignment in a field width of 5
print(' {:>5} '.format('cat'))
# Output: '  cat'

# Formatting a string with center-alignment in a field width of 5
print(' {:^5} '.format('cat'))
# Output: ' cat '

# Formatting a string with center-alignment in a field width of 5, padded with '*'
print(' {:*^5} '.format('cat'))
# Output: '*cat*'

# Formatting a string with a maximum length of 5 characters
print(' {:.5} '.format('caterpillar'))
# Output: 'cater'

# Formatting a string with right-alignment in a field width of 5 and a maximum length of 3 characters
print(' {:>5.3} '.format('caterpillar'))
# Output: '  cat'

# Formatting a string with center-alignment in a field width of 5 and a maximum length of 3 characters
print(' {:^5.3} '.format('caterpillar'))
# Output: ' cat '
