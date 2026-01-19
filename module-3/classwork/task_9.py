text = "сегодня 19-01-26 был солнечный день. а завтра какая будет погода. завтра будет морозно. очень этого не хотелось, но куда деваться."
razdel = text.split(". ")
print(". ".join(x.capitalize() for x in razdel))

a = text.split()
print(a)
