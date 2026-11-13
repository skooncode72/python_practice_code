import json

with open("employee.json", "r") as file:
    data = json.load(file)

print(data)
print(data["employee_name"])
print(data["salary"])