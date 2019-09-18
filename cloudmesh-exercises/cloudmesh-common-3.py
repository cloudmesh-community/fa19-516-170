from cloudmesh.common.FlatDict import FlatDict
from cloudmesh.common.Printer import Printer

student = {"name": "Yanting",
           "address": {
               "city": "Bloomington",
               "state": "Indiana",
               "country": "United States"
           }
           }

flatStudent = FlatDict(student)
print(flatStudent)

data = [student]
table = Printer.flatwrite(data, sort_keys=["name"], order=["name", "address.city", "address.state", "address.country"],
                          header=["Name", "City", "State", "Country"], output='table')
print(table)
