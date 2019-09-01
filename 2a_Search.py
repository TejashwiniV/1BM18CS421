def func(list,key):
    for num in list:
        if num == key:
            return True
    else:
            return False 
list = []
n = int(input("Enter the size of list:"))
print("Enter the list elements in ascending order:")
for i in range(n):
    num = int(input())
    list.append(num)
print(f'List:{list}')
key = int(input("Enter the key to search:"))
res=func(list,key)
if(res==True):
    print("Key found")
else:
    print("Key not found")
