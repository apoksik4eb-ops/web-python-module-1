text = "сегодня 19-01-26 был солнечный день. а завтра какая будет погода. завтра будет морозно. очень этого не хотелось, но куда деваться."
razdel = text.split(". ",)
print(". ".join(x.capitalize() for x in razdel))
print(len([x for x in text if x.isdigit()]))

punct = ".,?!:;"
count = 0
for x in text:
    if x in punct:
        count += 1
print(count)

print(len([x for x in text if x in punct]))



# count = 0
# for x in text:
#     if x.isdigit():
#         count += 1
# print(count)

