u=int(input())
flag=0
for r in range(2,u//2):
	if u%r==0:
		flag=1
		break
if flag==0:
	print("yes")
else:
	print("no")
	
