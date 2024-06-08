# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:51:33 2024

@author: user
"""

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
#t = is_prime(10)
#print(t)