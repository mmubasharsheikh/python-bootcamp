## Problem: Get user's name his age and show him his age in 2035 in following format "Hi xyz, you will be x years old in 2035"

# Getting user's data...
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

# Setting curent and future age...
current_year = 2025
calculate_upto_year = 2035

# Logic to calculate future age...
future_age = age + (calculate_upto_year-current_year)

# Print final statement...
print(f"Hello {name}, you will be {future_age} years old in {calculate_upto_year}.")