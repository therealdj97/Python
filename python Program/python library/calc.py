def abc():
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=input("enter an operation to be made ie +-*/")
    if c=="+":
        d=a+b
    elif c=="-":
         d=a-b
    elif c=="*":
         d=a*b
    elif c=="/":
         d=a/b
    return d
