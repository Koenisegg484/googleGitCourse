import re

def reverse_name(name):
    pattern = "(\w*) (\w*)"
    result = re.search(pattern, name)
    return result.group(2) + " " + result.group(1)

name = input("Enter yur full name : ")
nam = reverse_name(name)
print(nam)