# List 
# Data structure
   
environment = ["dev", "prd", "stgg" ]

print(environment)
print(environment[0])
print(len (environment))

environment.append("project")
print("new=", environment)
print(dir(environment))
print(format(environment))

#give a documentaion of perticular things
print(environment.insert.__doc__)

# Dictionary 

device_info = {
    "name": "Tech Solutions",
    "Ram": " 16 GB",
    "CPU": 8,
    "isNew": False
}

print(device_info.get("name") )