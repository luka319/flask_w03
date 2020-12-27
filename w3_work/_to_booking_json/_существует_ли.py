import pathlib
 
path = pathlib.Path('music.mp3')
print(f"{path.exists() =}") # True
print(f"{path.is_file() =}") # True
