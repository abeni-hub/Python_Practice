# Key word arguments
def print_num(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        
print_num(name="Abeni", age="23",Country="Ethiopia")        

