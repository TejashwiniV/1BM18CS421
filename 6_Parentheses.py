class parentheses:
   def is_valid_parentheses(self, str1):
        list = []
        dict = {"(": ")", "{": "}", "[": "]"}
        for i in str1:
            if i in dict:
                list.append(i)
            elif len(list) == 0 or dict[list.pop()] != i:
                return False
        return len(list) == 0
obj = parentheses()
string = input("Enter brackets: ")
output = obj.is_valid_parentheses(string)
if(output == True):
    print("Valid string")
else:
    print("Invalid string")
    
'''OUTPUT
Enter brackets: (){[]}
Valid string
Enter brackets: ([{]})
Invalid string
'''
