def convert_temperature(temp,unit):
    """ This function converts temperature between Celsius and Faranheit"""
    if unit == 'C':
        return temp * 9/5 + 32
    elif unit == 'F':
        return (temp-32)*5/9 
    else:
        return None
    
print(convert_temperature(25,'C'))
print(convert_temperature(77,'F'))    
