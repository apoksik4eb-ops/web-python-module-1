def happy_num(num):
    if len(num) != 6:
        return False
    elif sum(map(int, num[:3])) == sum(map(int, num[3:])):
        return True
    else:
        return False
    
print(happy_num("123510"))