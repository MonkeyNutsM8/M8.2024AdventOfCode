import csv

test_mode = True

def test_print(msg, var): 
    if test_mode == True:
        print(f"{msg}: {var}")  


file = "D:/Projects/M8.CodeOfAdvent2024/data/codeOfAdventCopySimple.csv" #baby steps :)
#file = "D:/Projects/M8.CodeOfAdvent2024/data/codeOfAdventCopy.csv" #bigger practice
#file = "D:/Projects/M8.CodeOfAdvent2024/data/codeOfAdvent.csv" #real data

reader = csv.reader(file)

list1 = []
list2 = []

counter = 0


#open file
with open(file, 'r') as file:
    reader = csv.reader(file, delimiter=' ') #space is delimiter
    #content = file.read()
    #print(reader)

    for row in reader:
        counter = counter + 1
        test_print("row1new", row)
        #remove empty strings by multiple spaces
        row = [value for value in row if value] #filters out empty strings
        test_print("row2new", row)
        if len(row) == 2: #see if row has two values
            list1.append(row[0])
            list2.append(row[1])
        test_print("counter", counter)
 

#split each value into characters without losing its origional figure and
#sort them ascending
sorted_list1 = [sorted(value) for value in list1]
sorted_list2 = [sorted(value) for value in list2]

total_difference = 0

for value1, value2 in zip(sorted_list1, sorted_list2):
    #calculate difference for current pair
    pair_difference = sum(abs(int(c1) - int(c2)) for c1, c2 in zip(value1, value2))
    diff = 0 + pair_difference
    total_difference += pair_difference
    test_print("Temp diff", diff)


#print("List 1:", sorted_list1[:10])
#print("List 2:", sorted_list2[:10])
print("Total difference:", total_difference)