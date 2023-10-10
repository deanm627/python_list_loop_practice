# Part 1 - Start/End

print("Select a range of numbers from 1-100")
start = int(input("Enter a starting number: "))
if (start < 1):
    print("Out of range")
    exit()
end = int(input("Enter an ending number: "))
if (end > 100):
    print("Out of range")
    exit()
# Increment by 1
# while start < end:
#     print(start)
#     start += 1

# Increment by more than 1
while start < end:
    print(start)
    start += 5


# Part 2 - Multi-Condition Check

string = "Apple TV Primary Classroom"
counter = 0

while (counter < len(string)):
    if (counter % 2) == 0 and string[counter] != " ":
        print(string[counter])
    counter += 1