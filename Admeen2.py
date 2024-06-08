# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:54:16 2024

@author: user
"""

def Welcome():
    name = input("Enter Your Name")
    gender = input("Enter your gender")
    if gender == "male" or gender == "m":
        print(f"Hello! Mr. {name} You are welcome")
    elif gender == "Female" or gender == "m":
        print(f"Hello! Mrs. {name} You are welcome")
    else:
        print("Input not recognised")
Welcome("Adeyemi", "male")