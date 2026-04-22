brand = ("audi", "reno", "honda", "audi", "reno", "honda", "audi")
text = input("Введите название автопроизводителя: ")
switch = input("Введите слово для замены: ")

new_brand = []
for word in brand:
    if word == text:
        new_brand.append(switch)
    else :
        new_brand.append(word)

new_tuple = tuple(new_brand)
print(new_tuple)