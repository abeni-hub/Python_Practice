# Create To do list To keep track of Tasks
to_do_list = ["Pray","Bible","Read Books","Clean house","Schedule for meeting"]

# Adding tasks
to_do_list.append("Meet Eyosi")
to_do_list.append("Go for package fill")

# Remove tasks
to_do_list.remove("Clean house")

# checking if the task is in the list

if "Schedule for meeting" in to_do_list:
    print("Don't forget the meeting you have!")
print("To do list remaining") 

for task in to_do_list:
    print("-",task)
