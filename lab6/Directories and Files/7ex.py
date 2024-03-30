
try:
    with open('\\Users\\aliya\\OneDrive\\Рабочий стол\\lab6\\Directories and Files\\4.txt', 'r') as source:
        with open('\\Users\\aliya\\OneDrive\\Рабочий стол\\lab6\\Directories and Files\\5.txt', 'w') as destination:               
            for line in source:
                destination.write(line)
        print("File copied successfully.")
except Exception as e:
    print("An error occurred:", str(e))

