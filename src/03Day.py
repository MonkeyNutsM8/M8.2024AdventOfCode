import re

filename = "D:/Projects/M8.CodeOfAdvent2024/data/03DayData/codeOfAdventCopySimple.csv" #baby steps :)
filename = "D:/Projects/M8.CodeOfAdvent2024/data/03DayData/codeOfAdventCopy.csv" #bigger practice
filename = "D:/Projects/M8.CodeOfAdvent2024/data/03DayData/codeOfAdvent.csv" #real data

filtered_content = []

with open(filename, 'r') as file:
    content = file.read()
    print(content)
    
pattern = r'mul\((\d+),(\d+)\)'  # Capture the numbers inside the parentheses

# Find all matches using re.findall
matches = re.findall(pattern, content)

# Storage for filtered content
filtered_content = []

# Add the matches to filtered_content
for match in matches:
    filtered_content.append(f"mul({match[0]},{match[1]})")
    print("filtered content: ", filtered_content)

# Multiply the numbers inside each 'mul(<number>,<number>)'
math_content = []

for item in filtered_content:
    # Extract the numbers using a regular expression
    numbers = re.findall(r'\d+', item)
    
    # Convert to integers and multiply
    num1, num2 = int(numbers[0]), int(numbers[1])
    result = num1 * num2
    
    # Store the result
    math_content.append(result)

# Output the result content
print("Result Content:", math_content)

total_sum = sum(math_content)
print("Total sum: ", total_sum)