def overlapping():
    with open("prime_numbers.txt","r") as file1:
        str1=file1.read()
        l1=str1.split(',')
    with open("happy_numbers.txt","r") as file2:
        str2=file2.read()
        l2=str2.split(',')
    print("Overlapping numbers are: ")
    for i in l1:
        for j in l2:
            if i==j:
                print(j)
overlapping()

'''
OUTPUT:
Overlapping numbers are: 
 7
 13
 19
 23
 31
 79
 97
 103
 109
 139
 167
 193
 239
 263
 293
 313
 331
 367
 379
 383
 397
 409
 487
 563
 617
 653
 673
 683
 709
 739
 761
 863
 881
 907
 937
 '''
