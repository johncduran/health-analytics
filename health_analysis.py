import pandas as pd
import numpy as np


# The funtion below is used to calculate BMI and body fat percentage
# I will be using the following formulas for my function

# BMI = (pounds/inches^2) x 703

# Men Body Fat Percentage = (1.20 x BMI) + (0.23 x Age) – 16.2

# Women Body Fat Percentage = (1.20 x BMI) + (0.23 x Age) – 5.4

def calculate_body_fat(weight, height, gender, age):
    bmi = (weight / (height ** 2)) * 703
    
    body_fat_data = {
        "male": {
            "operation": 16.2,
            "description": "Male body fat percentage"
        },
        "female": {
            "operation": 5.4,
            "description": "Female body fat percentage"
        }
    }
    
    if gender in body_fat_data:
        operation = body_fat_data[gender]["operation"]
        body_fat_percentage = (1.20 * bmi) + (0.23 * age) - operation
        description = body_fat_data[gender]["description"]
        result = {
            "description": description,
            "body_fat_percentage": body_fat_percentage
        }
    else:
        result = {
            "description": "Please only enter 'male' or 'female' as an option.",
            "body_fat_percentage": None
        }
    
    return result

# The following should be how the info should be inputted 
weight = int(input("Enter weight in pounds: "))
height = int(input("Enter height in inches: "))
gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

BodyFatResult = calculate_body_fat(weight, height, gender, age)
print(BodyFatResult["description"] + ":", BodyFatResult["body_fat_percentage"])

