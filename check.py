name = input("Whats your name ")
age = int(input("Enter your age "))
age_limit = 20
if age < age_limit:
    print(f"Youre not of age to use this application, you need to be atleast {age_limit} years old to use it ") and quit()
else:
    lastname=input(f"Whats your last name, {name} ")
    print(f"Hello {name} {lastname} you are {age} years old ")
