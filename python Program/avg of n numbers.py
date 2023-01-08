#sum of n numbers
x = int(input("Enter nth number"))
sum = 0
for i in range(0,x,1):
    n= int(input("enter the number"))
    sum=sum+n
avg=sum/n
print("Average is ",avg)