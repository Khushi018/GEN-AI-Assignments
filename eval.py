user_input = input("Enter a string: ")
reversed_string = user_input[::-1]
print("Reversed string:", reversed_string)




def max_salary_employee(employees):
    max_salary_employee = max(employees, key=lambda emp: emp['salary'])
    return max_salary_employee
