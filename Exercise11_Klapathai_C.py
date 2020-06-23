number = int(input())
for x in range(number):
    print(" "*(number - x) + "*"*(x+1) + "*"*x)
