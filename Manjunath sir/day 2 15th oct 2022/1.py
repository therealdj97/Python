n = input("Input the number of days in the month (28-31): ")
d = input("Input the starting day (0=Sun, 1=Mon,...): ")
for j in range(d):
		print ("  ") 
i = 1
while i <= n:
		if i < 10:
			print "", i,
		else:
			print i,
		if (i+d) % 7 == 0:
			print " "
		i = i + 1