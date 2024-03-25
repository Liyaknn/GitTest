import re

txt = str(input())
pattern = re.compile(r"[A-Z]{1}[a-z]+")
print(pattern.findall(txt))