c = "*"
n = int(input("enter the given number: "))
d=" "
e=1
for i in range(1,n+1):
    if i ==1 or i==n:
        print(f"{c*(n)}")
    else:

        print(f"{c}{d*(n-2)}{c}")
