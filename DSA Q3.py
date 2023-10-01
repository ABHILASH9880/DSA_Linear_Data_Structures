# Python3 program for the above approach
 
 
def checkString(s1, s2, indexFound, Size):
    for i in range(Size):
 
        # check whether the character is equal or not
        if(s1[i] != s2[(indexFound + i) % Size]):
            return False
 
        # %Size keeps (indexFound+i) in bounds,
        # since it ensures it's value is always less than Size
    return True
 
 
# driver code
s1 = "abcd"
s2 = "cdab"
 
if(len(s1) != len(s2)):
    print("s2 is not a rotation on s1")