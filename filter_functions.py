def even(num):
    if num%2 == 0:
        return True
    
even(2)    

lst = [1,2,3,4,5,6,7,8,9,10,11,12]
list(filter(even, lst))

# to get numbers greater than five by using lambda functions with filter

numbers = [1,2,3,4,5,6,7,8,9,10]
greater_than_five = list(filter(lambda x:x>4, numbers))
print(greater_than_five)


# Filter a lambda functions and mulitple conditions

numbers = [1,2,3,4,5,6,7,8,9,10]
even_and_greater_than_five = list(filter(lambda x:x> 5 and x%2 == 0 , numbers))
print(even_and_greater_than_five)


# Filter to check if the age is greater than 25 in dictionaries

people = [
    {'name': ' Abeni', 'age': 32},
    {'name': 'Efrem' , 'age': 34},
    {'name':'Duluulinat', 'age': 23}
    
]


def age_greater(person):
    return person['age']>25


list(filter(age_greater, people))
