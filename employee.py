import json

class Employees:
    def __init__(self,name,dob,height,city,state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Open a json file
with open('employee.json','r') as file :
    data = json.load(file)
    
# Create a list of Employee object from the dict
employees = [Employees(e['Name'], e['DOB'], e['Height'], e['City'] , e['State']) for e in data['Employees']]

# Printing the list
for employee in employees:
    print(employee.name, employee.dob, employee.height, employee.city, employee.state)
