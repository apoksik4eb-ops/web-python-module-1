def max_symbol(sym):
    sym = sym.replace(" ", "")
    max_count = 0
    char_result = ""

    for char in sym:
        count = sym.count(char)
        if count > max_count:
            max_count = count
            char_result = char
    return char_result

print(max_symbol("Hello hello rrrrrrr"))