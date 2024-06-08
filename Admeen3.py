# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:25:22 2024

@author: user
"""

def welcome(name, gender):
    name = input("Enter Your Name: ")
    gender = input("Enter your Gender: ")
    if gender == "male":
        print(f"Hello Mr. {name}, you are welcome")
    elif gender == "female":
        print(f"Hello Mrs. {name}, you are welcome")
    else:
        print("Value not recognised")
welcome("Adeyemi", "male")