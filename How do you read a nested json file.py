import json

with open("employee.json", "r") as file:
    data = json.load(file)

print(data["employee_name"])

print(data["department"]["department_name"])

print(data["department"]["location"])

print(data["skills"][0])