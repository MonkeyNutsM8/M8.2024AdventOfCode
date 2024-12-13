import csv

test_mode = True

def test_print(msg, var): 
    if test_mode == True:
        print(f"{msg}: {var}")  


filename = "D:/Projects/M8.CodeOfAdvent2024/data/01DayData/codeOfAdventCopySimple.csv" #baby steps :)
#filename = "D:/Projects/M8.CodeOfAdvent2024/data/01DayData/codeOfAdventCopy.csv" #bigger practice
#filename = "D:/Projects/M8.CodeOfAdvent2024/data/01DayData/codeOfAdvent.csv" #real data

#reader = csv.reader(file)

list1 = []
list2 = []

#counter = 0


#open file
with open(filename, 'r') as file:
    for line in file:
        lineList = line.split()
        print(lineList)
        list1.append(lineList[0])
        list2.append(lineList[1])
    print(list1, list2)
    list1.sort()
    list2.sort()
    print(list1, list2)

    #reader = csv.reader(file, delimiter=' ') #space is delimiter
    #content = file.read()
    #print(reader)

    #for row in reader:
    #    print("row", row)
    #    counter = counter + 1
    #    test_print("row1new", row)
    #    #remove empty strings by multiple spaces
    #    row = [value for value in row if value] #filters out empty strings
    #    test_print("row2new", row)
    #    if len(row) == 2: #see if row has two values
    #        list1.append(row[0])
    #        list2.append(row[1])
    #    test_print("counter", counter)
 

#split each value into characters without losing its origional figure and
#sort them ascending
#sorted_list1 = [sorted(value) for value in list1]
#sorted_list2 = [sorted(value) for value in list2]

total_difference = 0

for value1, value2 in zip(list1, list2):
    #calculate difference for current pair
    pair_difference = abs(int(value1) - int(value2))
    diff = 0 + pair_difference
    total_difference += pair_difference
    #test_print("Temp diff", diff)


#print("List 1:", sorted_list1[:10])
#print("List 2:", sorted_list2[:10])
print("Total difference:", total_difference)