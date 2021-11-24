"""
@Author: Zeehan 
@Date: 2021-24-11 13:00:30
@Title : Calculate Wages til a condition of total working hours or days is reached for a month
"""
"""
Description:
     imported random library and declare 5 constant variable ans use if elif and use while loop  
Parameter:
      
Return:
        returned calculatewagetill100hrsor20isreached() randint is a function it return random integer
"""
import random
IS_PART_TIME = 1
IS_FULL_TIME = 2
EMP_RATE_PER_HOUR = 20
NUM_OF_WORKING_DAYS = 20
MAX_HRS_IN_MONTH = 100
def calculatewagetill100hrsor20isreached():
    empHrs = 0
    totalEmpHrs = 0
    totalWorkingDays = 0
    while (totalEmpHrs <= MAX_HRS_IN_MONTH and totalWorkingDays < NUM_OF_WORKING_DAYS):
        totalWorkingDays+=1
        empCheck = random.randint(0, 3)
        if (empCheck==IS_PART_TIME):
            empHrs = 4
        elif(empCheck== IS_FULL_TIME):
            empHrs = 8
        else: 
            empHrs = 0 
        totalEmpHrs += empHrs
        totalEmpWage = totalEmpHrs * EMP_RATE_PER_HOUR
        print(totalEmpWage)

if __name__=='__main__': 
    calculatewagetill100hrsor20isreached()       