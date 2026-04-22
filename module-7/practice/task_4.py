line_file = set()
line_file_1 = set()

with open("file.txt", "r", encoding="utf-8") as file:
    for line in file:
        line_file.add(line.strip())

with open("file_1.txt", "r", encoding="utf-8") as file:
    for line in file:
        line_file_1.add(line.strip())

result = line_file ^ line_file_1
for str in result:
    print(f"Несовпадающие строки = {str}")