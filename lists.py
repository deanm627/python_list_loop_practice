# Part 1 - Change a list

numbers = [1, 2, 3, 4, 5, 99, 2600, 300]

reversed_list = list(reversed(numbers))

print(numbers)
print(reversed_list)

# Part 2 - String to list 

string = "ketchup"
lst = []

for char in string:
    lst.append(char)

lst.reverse()

string2 = ""
for letter in lst:
    string2 += letter

print("Original string: %s, Reversed string: %s"%(string, string2))

# Part 3 - List + Conditional 

elemental = ["Fire", "Water", "Cloud", "Earth"]

test = input("Enter an element name: ")

if test in elemental:
    elemental.remove(test)
else:
    elemental.append(test)

print(elemental)