# This program explains the file reading syntaxes

try:
    employee_details = open("employee_details.txt", "w")
except FileNotFoundError as err:
    print(err)

if employee_details.readable():
    for employee in employee_details.readlines():
        print(employee)
else:
    print("Please provide a readable file")


employee_details.close()

