"""
@Author: Zeehan khan
@Date: 2021-24-11 13:00:30
@Title : Calculate total wage 
"""
"""
Description:
     Function here i used two function with  parameter whi will return compny name emp rateperhur numofworkingdays maxhurpermonth 
Parameter:
      we have five parameter in our program
Return:
       retuned compny emprateprhur numofworkingdays maxhurpermonth randint is a function it return random integer
"""
import random
IS_PART_TIME = 1
IS_FULL_TIME = 2
def computeempwage( company,  empRatePerHour,  numOfWorkingDays,  maxHoursPerMonth):
    empHrs = 0
    totalEmpHrs = 0
    totalWorkingDays = 0
    while (totalEmpHrs <= maxHoursPerMonth and totalWorkingDays < numOfWorkingDays):
        totalWorkingDays+=1
        empCheck = random.randint(0, 3)
        def empHrs(i):
            switcher = {
                0: 0,
                1: 4,
                2: 8,
            }
            return switcher.get(i, 0)
        totalEmpHrs += empHrs(empCheck)
        totalEmpWage = totalEmpHrs * empRatePerHour
    print("Total Emp Wage for company: " + str(company) + " is : " + str(totalEmpWage))


if __name__=='__main__':
    computeempwage("Airtel", 2, 10, 20)
