def line(dln, dir, sym):
    if dir == "h":
        print(dln * sym)
    
    if dir == "v":
        for i in range(dln):
            print(sym)

line(5, "v", "*")
