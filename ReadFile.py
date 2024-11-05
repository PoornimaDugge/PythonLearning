emp_file = open("employees.txt","r")
for employee in emp_file.readlines():
    print(employee)
emp_file.close()
