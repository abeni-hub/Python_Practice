# Key word arguments
def print_num(*args,**kwargs):
    for val in args:
        print(f"Positional arguments : {val}")
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        
print_num(1,2,3,"Great",name="Abeni", age="23",Country="Ethiopia")        
