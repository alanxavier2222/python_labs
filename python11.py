num1 = input("enter the first  number:")
num2 = input("enter the second number:")
num3 = input("enter the third number:")
if(num1>num2 and num2<num3):
    print("num2 is smaller")
elif(num2>num1 and num1<num3):
    print("num1 is smaller")
elif(num3<num1 and num3<num2):
    print("num3 is smaller")
else:
    print("all are equal")