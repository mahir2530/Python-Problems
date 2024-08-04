
# Converting an integer to a string
num = 123
num_str = str(num)
print(num_str)  # Output: "123"
print(type(num_str))  # Output: <class 'str'>

# Converting a string to an integer
num_str = "123"
num = int(num_str)
print(num)  # Output: 123
print(type(num))  # Output: <class 'int'>

# Converting a string to a float
num_str = "123.45"
num = float(num_str)
print(num)  # Output: 123.45
print(type(num))  # Output: <class 'float'>

# Converting a float to an integer (note that this truncates the decimal part)
num_float = 123.45
num_int = int(num_float)
print(num_int)  # Output: 123
print(type(num_int))  # Output: <class 'int'>

# Joining a list of strings into a single string with spaces
list_of_strings = ['Hello', 'world']
joined_string = ' '.join(list_of_strings)
print(joined_string)  # Output: "Hello world"

# Splitting a string into a list of words
string = "Hello world"
list_of_words = string.split()
print(list_of_words)  # Output: ['Hello', 'world']

# Converting a list to a tuple
list_example = [1, 2, 3]
tuple_example = tuple(list_example)
print(tuple_example)  # Output: (1, 2, 3)
print(type(tuple_example))  # Output: <class 'tuple'>

# Converting a tuple to a list
tuple_example = (1, 2, 3)
list_example = list(tuple_example)
print(list_example)  # Output: [1, 2, 3]
print(type(list_example))  # Output: <class 'list'>

# Converting a dictionary to a list of tuples (key-value pairs)
dict_example = {'a': 1, 'b': 2}
list_of_tuples = list(dict_example.items())
print(list_of_tuples)  # Output: [('a', 1), ('b', 2)]

# Converting a list of tuples to a dictionary
list_of_tuples = [('a', 1), ('b', 2)]
dict_example = dict(list_of_tuples)
print(dict_example)  # Output: {'a': 1, 'b': 2}
