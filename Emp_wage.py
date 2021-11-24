"""
@Author: Zeehan 
@Date: 2021-24-11 13:00:30
@Title : emp wage using switcher 
"""
"""
Description:
     imported random library and declare 3 constant variable ans use if   
Parameter:
      use emphur function with parameter i and switcher is a dict and we returned value with .get method
Return:
       return key and value randint is a function it return random integer
"""
import random
IS_PART_TIME = 1
IS_FULL_TIME = 2
EMP_RATE_PER_HOUR = 20
empHrs = 0
empWage = 0
empCheck = random.randint(0, 3)
def empHrs(i):
        switcher={
                0:0,
                1:4,
                2:8,
             }
        return switcher.get(i,0)

empWage = empHrs(empCheck) * EMP_RATE_PER_HOUR
print(empWage)
 