import sys
if len(sys.argv)==2:
    script_name=sys.argv[0]
    salary=sys.argv[1]
else:
    script_name=sys.argv[0]
    salary="50000"  
bonus=int(salary)*10/100
total_salary=int(salary)+int(bonus) 
print("Script Name:",script_name)
print("Salary:",salary)
print("Bonus:",bonus)
print("Total Salary:",total_salary)
