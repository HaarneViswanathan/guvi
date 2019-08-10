n=int(input("Enter a number: "))
temp=n
reverse=0
while(temp!=0):
    remainder=temp%10
    reverse=reverse*10+remainder
    temp=temp//10
if(reverse==n):
    print("Yes")
else:
    print("No")
