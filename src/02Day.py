# Function to check if a row is safe
def check_row_safety(row):
    ascending = all(row[i] < row[i + 1] and (row[i + 1] - row[i] <= 3) for i in range(len(row) - 1))  # Strictly ascending with max step
    descending = all(row[i] > row[i + 1] and (row[i] - row[i + 1] <= 3) for i in range(len(row) - 1))  # Strictly descending with max step
    
    if ascending:
        return True  # Row is safe
    elif descending:
        return True  # Row is safe
    else:
        return False  # Row is unsafe

# Read data from a file and count safe/unsafe rows
def process_file(filename):
    safe_count = 0
    unsafe_count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            # Convert the line into a list of integers
            row = list(map(int, line.strip().split()))
            # Check the safety of the row
            if check_row_safety(row):
                safe_count += 1
            else:
                unsafe_count += 1
    
    # Print the counts at the end
    print(f"Safe rows: {safe_count}")
    print(f"Unsafe rows: {unsafe_count}")

# File path
filename = "D:/Projects/M8.CodeOfAdvent2024/data/02DayData/codeOfAdventCopySimple.csv" #baby steps :)
#filename = "D:/Projects/M8.CodeOfAdvent2024/data/02DayData/codeOfAdventCopy.csv" #bigger practice
#filename = "D:/Projects/M8.CodeOfAdvent2024/data/02DayData/codeOfAdvent.csv" #real data

# Process the file
process_file(filename)