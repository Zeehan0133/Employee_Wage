"""
@Author: Zeehan 
@Date: 2021-24-11 13:00:30
@Title : calculate daily wage 
"""
"""
Description:
     imported random library and declare 2 constant variable ans use if else   
Parameter:
        
Return:
       randint is a function it return random integer
"""
import random
IS_FULL_TIME = 1
EMP_RATE_PER_HUR = 20
#Emp_Hur=0
#Emp_Wage=0
empCheck = random.randint(0, 2)
if empCheck == IS_FULL_TIME:
    Emp_Hur=8
else:
    Emp_Hur=0
Emp_Wage= Emp_Hur * EMP_RATE_PER_HUR
print( Emp_Wage)           