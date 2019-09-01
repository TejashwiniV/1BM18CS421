a = []
b = []
n = int(input("Enter the size of list:"))
print("Enter the list elements:")
for num in range(0,n):
    ele = int(input())
    a.append(ele)
print("List elements:",a)
for even in a:
    if even%2 == 0:
        b.append(even)
print("Even elements in the list are:",b)
