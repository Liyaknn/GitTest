def count_upper_lower(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

# Example usage:
input_string = "My name is Aliya"
upper, lower = count_upper_lower(input_string)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
