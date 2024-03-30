import os

path = '\\Users\\aliya\\OneDrive\\Рабочий стол\\lab6'
if os.path.exists(path):
    print("The path exists.")
    print("Filename:",os.path.basename(path) )
    print("Directory:", os.path.dirname(path) )
else:
    print("The path does not exist.")




