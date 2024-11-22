limit=int(input("Enter a limit:"))


for i in range(limit):
    for j in range(i+1):
        print("*",end="")
    print()


for s in range(limit,0,-1):
    for r in range(s):
        print("*",end="")
    print()

for t in range(limit+1):
    for f in range(limit-t):
        print(" ",end="")
    for f in range(2*t-1):
        print("*",end="")
    print()

for t in range(limit,0,-1):
    for f in range(limit - t):
        print(" ", end="")
    for f in range(2 * t - 1):
        print("*", end="")
    print()


