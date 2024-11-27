print("Hello Users!")               
num =input("what is your name?")
print("Hello ", num)

from datetime import datetime

print()

birth_year = int(input("What is your year of birth?"))
current_year = datetime.now().year
age = current_year - birth_year

drive = input("Do you know how to drive? Yes/No")

if drive == "yes":
    licence_age = int(input("How old are you got your driving licence?"))
    licence_year = birth_year + licence_age
    driving_years = current_year - licence_year
    print("You got your driving licence in ",licence_year," and you have been driving for ",driving_years," years. ")
    
    
else:
    if age> 30:
        got_licence = birth_year + 30
        late_years = current_year - got_licence
        print("You are ", age , " year old now but you still can't dirve. /n You are supposed to get your licence in ",got_licence,late_years," years ago at the age of 30 at the latest.")
    else:
        years_to_go = 30 - age
        required_year = birth_year +  30
        print("You are ",age," years old now and you should work on getting your driving licence before you turn 30. /n You have ", years_to_go," years to go until the year ",required_year)    
    
