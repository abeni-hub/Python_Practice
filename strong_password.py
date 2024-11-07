def is_strong_password(password):
    """Check if the password is strong or not"""
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+' for char in password):
        return False
    return True


## calling the function
print(is_strong_password("WeakPWD"))
print(is_strong_password("Str0ngPwd"))
