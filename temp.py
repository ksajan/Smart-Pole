import json
with open ('static/file.json', 'r') as file :
    data = json.load(file)
    if data["status"] == "ON" :
        switch = "OFF"
    else:
        switch = "ON"

print(switch)
