def words(string):
    s = string.split(' ')
    r = s[::-1]
    res = ' '.join(r)
    return res
   
def letters(res1):
    r = res1[::-1]
    res = ''.join(r)
    return res
    
string = input("Enter the string:")
res1 = words(string)
print("Words in backward order:",res1)
res2 = letters(res1)
print("letters in reverse order:",res2)
