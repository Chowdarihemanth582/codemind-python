n=int(input())
s=n*n
r=str(n)
b=r[::-1]
p=int(b)*int(b)
q=str(p)
if(int(q[::-1])==s):
    print("True")
else:
    print("False")