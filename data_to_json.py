import json

f = open('data.py', 'r')
data = json.loads(f)
f.close()

print(f"{data=}")
states = data

# place = {"title":"Shoney's"}
#dumped = ...

with open("data.json", "w") as f:
   json.dump(states, f)