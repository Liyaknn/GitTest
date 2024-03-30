def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    return s == s[::-1]

input_string = "Qazaq"
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")