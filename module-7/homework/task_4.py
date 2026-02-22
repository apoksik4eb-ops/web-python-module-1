max_line = None
max_count_line = 0

with open("file.txt", "r", encoding="utf-8") as file:
    for line in file:
        if len(line) > max_count_line:
            max_line = line
            max_count_line = len(line)

print(f"Самая длиная строка = {line}, ее длина = {max_count_line} символов.")