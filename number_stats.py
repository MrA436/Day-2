num = input("Enter 5 numbers seperated by spaces:").split()
b=[]
for i in num:
    b.append(int(i))
print("Max number is:",max(b))
print("Min number is:",min(b))
print("sum of numbers is:",sum(b))
print("length of LIST is:",len(b))
