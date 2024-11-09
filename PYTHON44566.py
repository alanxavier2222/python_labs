""" python prograam to take the input from the user
and print the output
Author: alan xavier"""

mark = float(input("enter your mark:  "))
if(mark>90 and mark<=100):
    print("your grade is A")
elif(mark>80 and mark<=89):
    print("your grdae is b")
elif(mark>70 and mark<=79):
    print("your grade is c")
elif(mark>=60 and mark<=69):
    print("your garde is d")
else:
    print("your grade is f")
