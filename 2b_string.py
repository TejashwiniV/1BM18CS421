def backward(string):
    words=string.split(" ")
    words=words[-1::-1]
    output2=' '.join(words)
    return output2
    

def reverse(string):
    words=string.split(" ")
    newwords=[word[::-1] for word in words]
    output1=' '.join(newwords)
    return output1
    

string=input("Enter the string\n")
res1=backward(string)
print("Words in backward order :",res1)
res2=reverse(string)
print("letters in backward order :",res2)
