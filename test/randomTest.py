import re

# Input string with various characters and 'mul(<number>,<number>)'
input_string = '32&*£%mUl%(*(123,562)£"FHKAmul(234,43)2*%£mul(23,543)'

# Regular expression pattern (matches 'mul(number,number)')
pattern = r'mul\((\d+),(\d+)\)'  # Capture the numbers inside the parentheses

# Find all matches using re.findall
matches = re.findall(pattern, input_string)

# Storage for filtered content
filtered_content = []

# Add the matches to filtered_content
for match in matches:
    filtered_content.append(f"mul({match[0]},{match[1]})")

# Multiply the numbers inside each 'mul(<number>,<number>)'
result_content = []

for item in filtered_content:
    # Extract the numbers using a regular expression
    numbers = re.findall(r'\d+', item)
    
    # Convert to integers and multiply
    num1, num2 = int(numbers[0]), int(numbers[1])
    result = num1 * num2
    
    # Store the result
    result_content.append(result)

# Output the result content
print("Result Content:", result_content)
