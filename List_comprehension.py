 # we can do all of the above with list comprehension in one
square_list = [x**2 for x in range(10)]
print(square_list) 

# list comprehension with conditions
even_numbers = [num for num in range(10) if num%2==0]
print(even_numbers)

# Nested list comprehension
lst1 = [1,2,3,4]
lst2 = ['a','b','c','d']

pair = [[i,j] for i in lst1 for j in lst2]
print(pair)


# List comprehension with functions  calls
words = ["hello","world","list","comprehension"]
lengths = [len(words) for word in words]
print(lengths)

