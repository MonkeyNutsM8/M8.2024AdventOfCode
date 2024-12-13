
filename = "D:/Projects/M8.CodeOfAdvent2024/data/01DayData/codeOfAdventCopySimple.csv" #baby steps :)
#filename = "D:/Projects/M8.CodeOfAdvent2024/data/01DayData/codeOfAdventCopy.csv" #bigger practice
#filename = "D:/Projects/M8.CodeOfAdvent2024/data/01DayData/codeOfAdvent.csv" #real data

list1 = []
list2 = []

with open(filename, 'r') as file:
    for line in file:
        linelist = line.split()
        print(linelist)
        list1.append(linelist[0])
        list2.append(linelist[1])
    print(list1, list2)
    list1.sort()
    list2.sort()
    print(list1, list2)

total_difference = 0

for value1, value2 in zip(list1, list2):
    pair_difference = abs(int(value1) - int(value2))
    diff = 0 + pair_difference
    total_difference += pair_difference

print("total difference: ", total_difference)




