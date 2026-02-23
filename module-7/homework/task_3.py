with open("file.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    if lines:
        lines.pop()
    
with open("statistic.txt", "a", encoding="utf-8") as file:
    file.writelines(lines)