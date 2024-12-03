print("Enter a list")
list1=[]
list1_size=int(input("Enter the size of list1:"))
print("Enter the elements of list1 are:")
for i in range(list1_size):
    list1.append(int(input()))
    print(list1)
print("Enter another list")
list2=[]
list2_size=int(input("Enter the size of list2:"))
print("Enter the elements of list2 are:")
for i in range(list2_size):
    list2.append(int(input()))
    print(list2)
combined_list=list1+list2
print(combined_list)
even_list=[]
odd_list = []
for i in combined_list:
    if (i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)
print(odd_list)
print(even_list)
print(even_list.sort())
print(odd_list.sort())
print(even_list+odd_list)






