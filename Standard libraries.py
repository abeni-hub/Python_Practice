import math
print(math.sqrt(16))
print(math.pi)



import random 
print(random.randint(1,10))
print(random.choice(['apple', 'banana', 'mango']))




# File and Directory Access

import os
print(os.getcwd())


os.mkdir('test')



# Data Serialization

import json 

data = {'name': 'John', 'age': 30, 'city': 'New York'}

json_string = json.dumps(data)
print(json_string)
print(type(json_string))


parsed_data = json.loads(json_string)
print(parsed_data)
print(type(parsed_data))




# CSV file

import csv

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['John', 30, 'New York'])
    writer.writerow(['Mike', 25, 'Chicago'])


with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)    


# Date and Time
from datetime import datetime , timedelta

now = datetime.now()
print(now)


yesterday = now - timedelta(days=1)
print(yesterday)


# Regular Expression

import re

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)
print(result.group())

