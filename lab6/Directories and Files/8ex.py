import os
p=(r"C:\Users\aliya\OneDrive\Рабочий стол\lab6\Directories and Files\delete.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file does not exist")
