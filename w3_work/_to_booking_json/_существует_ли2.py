import pathlib
 
path = pathlib.Path('_booking.json')
print(f"{path.exists() =}") # True
print(f"{path.is_file() =}") # True
