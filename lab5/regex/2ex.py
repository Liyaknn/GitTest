import re
txt = str(input())
x = re.search(r"a(bb|bbb)" , txt)
print(x)