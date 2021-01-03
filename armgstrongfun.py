def armgstrong(n):
   armg=0
   while(n>0):
        d=n%10
        armg=armg+(d*d*d)
        n=n//10
   return armg
n=int(input("enter no"))
y=armgstrong(n)
if(y==n):
    print("armgstrong number")
else:
    print("not armgstrong number")
