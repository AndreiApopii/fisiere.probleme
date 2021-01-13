with open("globulete.txt", "r") as f:
    a=f.readline()
    r=int(a)+3
    b=int(a)+r-2
    t=int(a)+r+b
    with open("bradut.txt", "w") as f:
        f.write(str(t))