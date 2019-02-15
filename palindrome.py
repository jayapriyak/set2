l=int(input())
u=l
temp=0
while u!=0:
	temp=temp*10+u%10
	u=u//10
if l==temp:
	print("yes")
else:
	print("no")
