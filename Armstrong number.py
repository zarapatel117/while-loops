n=int(input("Enter a num "))
sum=0
temp=n
while temp>0:
    i=temp%10
    sum+=i**3
    temp//=10
if n==sum:
    print ("it is a Armstrong number")  
else:
    print("it is a normal number")      
