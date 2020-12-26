import json

"""
# парсинг x:
y = json.loads(x)
# результатом будет словарь Python:
print(y["age"])
"""
#teachers = 


with open("teachers.json", "r", encoding="utf-8") as f:
    te = json.load(f) # работает!!!

#print(f"{te =}")
print(f"{type(te) =}") # list
print(f"{len(te) =}") # 12

for z in te:
    if z["id"] == 3:
       print(f'{z["name"] =}')
       name = z["name"]


with open("goals.json", "r", encoding="utf-8") as f:
    goal = json.load(f) # работает!!!

for zz,kk in goal.items():
    #if zz["travel"]:
       #print(f'{zz["travel"] =}')
       print(f'{zz =}')
       print(f'{kk =}')

print(f"{goal =}")
print(f"{type(goal) =}") # list
print(f"{len(goal) =}") # 12

#==============

for z in te:
    if z["free"]:
       fr  = z["free"]
       print(f'{fr =}')
       print(f"{type(fr) =}") # 
       print(f"{len(fr) =}") #

print(f"---- {type(fr) =}") # 

for ke, va in fr.items(): # fr ={'mon': {'8:00': False, '10:00': False,
       #print(f'{ke =}') # OK!!!
       #print(f'{va =}') # OK!!!
       for ke2, va2 in va.items():
          if va2:
             print(f'{ke2 =}') # OK!!!
             print(f'{va2 =}') # OK!!!









