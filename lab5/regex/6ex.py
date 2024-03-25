import re

text = str(input())
replacedText = re.sub(r'[ ,.]', ':', text)
print(replacedText)