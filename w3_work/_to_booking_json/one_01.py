import json

import pathlib
 
path = pathlib.Path('booking.json')
if path.exists():
     if path.is_file():
         
        with open('booking.json', 'r', encoding='utf-8') as f:
             data_in = json.load(f)
        count = len(data_in)

     else:
        print("booking.json не является файлом")
        exit()

else:
     print("booking.json не существует")
     #exit()
     count = 0
     data_in = {}



clientWeekday="пятница"
                            
clientTime="13:00"
clientTeacher="Другой_Учитель"
                            
clientName="Алиса"
clientPhone="(073)4569875"

data = {count+1: [clientWeekday,clientTime,
            clientTeacher,clientName,
            clientPhone]
       }

data_in.update(data)
data_out = data_in

with open('booking.json', 'w', encoding='utf-8') as f:
         json.dump(data_out, f, ensure_ascii=False)
    
