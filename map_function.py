# map functions - applies a function to all items in a list
# map usually takes two input parameters --1. is function name and --2. is iterable, which is a collection

def square(num):
  return num**2

square(2)
# print out the square of two which is 4
# then here add map
num(2,3,4,5)
list(map(sqaure, num))

# map functions using lambda
numbers = [1,2,3,4,5]
list(map(lambda x:x**2 , numbers))

# Map multiple iterables

# Map multiple iterables

numbers1 = [1,2,3]
numbers2 = [4,5,6]

added_numbers = list(map(lambda x,y: x+y,numbers1 , numbers2))
print(added_numbers)


# map to convert a list of integers to list

str_numbers =["1","2","3","4","5"]
int_numbers = list(map(int, str_numbers))
print(int_numbers)

# to make upper words


words = ['apple','banana','cherry']
upper_word = list(map(str.upper, words))
print(upper_word)

# To get list of dictionary items or collections

def get_name(person):
    return person['name']

people = [
    {"name":'Abeni', 'age': 23},
    {'name': 'Efrem', 'age': 22}
]

list(map(get_name , people))






  ##### Conclusion
  The map function() is a pwoerful tool for applying transformations to iterable data structures. 
  It can be used with regular functions , labmda functions adn even multiple iterables,
  providing appreach to data processing in python.
