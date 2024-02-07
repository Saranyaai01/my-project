def sample():
    a=3+1
    print(a)
    if a==3:
        print("a is 3")
        x="I am saranya narayanan"
        for x1 in x:
            print(x1)
        x=x.split(" ")
        for x2 in x:
            print(x2)
    if a==4:
        print("a is 4")
        l=["a",1,1.2,"saranya"]
        print(l)
        print(type(l))
        for l2 in l:
            print(l2)
    if a>=6:
        print("a value is",a)
    else:
        print("end")
        
    y=input("Enter the is:").split()
    print(y) 

    i = 0
    while i < 8:
        i += 1
        if i == 4:
            continue
    print(i)      
sample()
   