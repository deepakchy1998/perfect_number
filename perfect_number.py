num1=int(input("enter your number :"))
sum=0
for i in range(1,num1):
    if num1%i==0:
        sum+=i
if sum==num1:
    print("given number is a perfect number")
else:
    print("given number is not a perfect number")
