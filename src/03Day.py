
filename = "D:/Projects/M8.CodeOfAdvent2024/data/03DayData/codeOfAdventCopySimple.csv" #baby steps :)
#filename = "D:/Projects/M8.CodeOfAdvent2024/data/03DayData/codeOfAdventCopy.csv" #bigger practice
#filename = "D:/Projects/M8.CodeOfAdvent2024/data/03DayData/codeOfAdvent.csv" #real data

with open(filename, 'r') as file:
    content = file.read()
    print(content)

