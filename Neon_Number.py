n=int(input())
temp=n
sum=0
pro=n*n
while(pro!=0):
    rem=pro%10
    sum+=rem
    pro=pro//10
if(sum==temp):
    print("Neon Number")
else:
    print("Not Neon Number")