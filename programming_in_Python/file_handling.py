# To write text to a new file
# This writes to one line
"""with open('test.txt', 'w') as file:
    file.write("This is a test")
"""

"""
# This writes to multiple lines
with open('test.txt', 'w') as file:
    file.writelines(["This is a test", "\nThis is another test"])
"""

# This writes to end line
with open('test.txt', 'a') as file:
    file.writelines(["This is a test", "\nThis is another test"])

# Reading Files

# This writes to one line
with open('test.txt', 'r') as file:
    print(file.read) # or .read(40) will read first 40 characters
#or
data = file.readlines()

for x in data: # or for x in file:
    print(x)

