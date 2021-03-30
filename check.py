name = input("Whats your name ")
age = int(input("Enter your age "))
if age < 18:
    print("Youre not of age to use this application ") and quit()
else:
    lastname=input(f"Whats your last name, {name} ")
    print(f"Hello {name} {lastname} you are {age} years old ")
