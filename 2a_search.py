def func(list,key):
    for num in list:
        if num==key:
            return True
    else:
            return False      
list = [1,2,3,4,5,6,7,8,9]
print(list)
key = int(input("Enter the key to search\n"))
res=func(list,key)
if(res==True):
    print("Key found")
else:
    print("Key not found")
