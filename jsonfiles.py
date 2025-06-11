#json file handling
 
import json

# Define the data as a Python dictionary
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Write data to a JSON file
with open('data.json', 'w') as f:
    json.dump(data, f)

d1 = {
    "1": "text",
    "2" : "3"
}
with open('data.json', 'w') as f: #overwrite remove existing content and write new content 
    json.dump(d1, f)

with open('data.json', 'r') as f: #read only
    print(f.read())
    
with open('data.json', 'a') as f: # append, keep original as it is add in last 
    json.dump(data, f)
    
with open('data.json', 'r') as f:
    print(f.read())

with open('a.json', 'x') as f: #create new file and if exist then give error
    json.dump(data, f)

with open('a.json', 'r') as f:
    print(f.read())