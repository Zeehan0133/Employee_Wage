"""
@Author: Zeehan 
@Date: 2021-24-11 13:00:30
@Title : Refactor the Code to write a function to get work hours
"""
"""
Description:
     imported random library and declare 5 constant variable ans use if elif and use while loop  
Parameter:
      
Return:
    retuned ComputeEmpWage():randint is a function it return random integer
"""
import random
IS_PART_TIME = 1
IS_FULL_TIME = 2
EMP_RATE_PER_HOUR = 20
NUM_OF_WORKING_DAYS = 2
MAX_HRS_IN_MONTH = 10
def ComputeEmpWage():
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
    print( totalEmpWage)
    print(totalEmpHrs)
        


if __name__=='__main__':
    ComputeEmpWage()