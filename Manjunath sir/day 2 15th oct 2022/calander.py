n = int(input("Input the number of days in the month (28-31): "))
d = int(input("Input the starting day (0=Sun, 1=Mon, 2=Tue, 3=Wed, 4=Thu, 5=Fri, 6=Sat): "))
for j in range(0,d):
    #pattern try start
     for i in range(0, j+1):
         
            # printing stars
            print("* ",end="")
            #pattern try end
            print("")
i = 1
while i <= n:
    if i < 10:  # One problem we see is that some dates have one digit and some have two. This causes the numbers not to line up nicely. We can fix that by printing an additional space if the number is less than 10:
        print("",i,)
    else:
        print('' ,i,)
    if (i+d) % 7 == 0:
            print('')
    i = i + 1
