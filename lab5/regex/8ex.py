import re

text = str(input())

words = re.findall(r'[A-Z][^A-Z]*', text)
print(words)