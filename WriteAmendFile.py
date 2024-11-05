#append the file
employee_file = open("employees.txt","a")
employee_file.write("\nSowmiya")
employee_file.close()


#overwrite the file
employee_file = open("index.html","w")
employee_file.write("<p>This is paragraph</p>")
employee_file.close()