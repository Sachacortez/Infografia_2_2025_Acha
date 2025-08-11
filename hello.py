age = 20
height = 1.75
name = "Diego"
print(f"Well, 'ello there, my name is {name}. I am {age} years old and {height} meters tall.")

try:
    age2 = float(input("How old are you? "))
except ValueError:
    print("Please enter a valid number for your age.")
print(age2, type(age2))