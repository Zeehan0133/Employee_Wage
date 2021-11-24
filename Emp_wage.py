"""
@Author: Zeehan 
@Date: 2021-24-11 13:00:30
@Title : check emp[loyee attendance
"""
"""
Description:
     Check whether a employee is present or not  
Parameter:
      
Return:
       randint is a function it return random integer
"""
import random
FULL_TIME=1
empCheck = random.randint(0, 2)
if empCheck==FULL_TIME:
    print("Employee is Present ")
else:
    print("Employee is Absent ")    