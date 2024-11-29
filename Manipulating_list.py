# manipulating lists
    # Ask 4 students at Datanomics to enter their names one at a time
student_names = []
student_names_1 = input("Enter the name of a new student: ")
student_names_2 = input("Enter the name of another new student: ")
student_names_3= input("Enter the name of another new student: ")
student_names_4= input("Enter the name of another new student: ")


student_names = ([student_names_1 ,student_names_2, student_names_3,student_names_4])

 # Extend the list student_names using the .extend() list method with two additional new students 
student_names.extend(['Abeni'])
student_names.extend(['Rahel'])


# Print student_names
print(student_names)

 # Find the position of one of the students and store the result in a variable called 'position'
position = 2
remove_students = student_names[position]
print(remove_students)


# Remove that student  from the list student_names using the .pop() list method
student_names.pop(position)

# prints student_names one more time
print(student_names)
