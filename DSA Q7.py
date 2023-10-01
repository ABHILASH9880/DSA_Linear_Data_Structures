# Python Program to convert the given prefix expression into an infix expression  
  
# Defining a function that will take a prefix string  
def prefixToInfix(prefix):  
    symbols = []  
       
    # reading the prefix string  
    l = len(prefix) - 1  
    while l >= 0:  
        if not Operator(prefix[l]):  
               
            # The current symbol is an operand  
            symbols.append(prefix[l])  
            l -= 1  
        else:  
             
            # the current symbol is an operator  
            string = "(" + symbols.pop() + prefix[l] + symbols.pop() + ")"  
            symbols.append(string)  
            l -= 1  
       
    return symbols.pop()  
  
def Operator(symbols):  
    if symbols == "*" or symbols == "+" or symbols == "-" or symbols == "/" or symbols == "^" or symbols == "(" or symbols == ")":  
        return True  
    else:  
        return False  
  
# Calling the function  
string = "*+P/QR-/STU"  
print("The infix string is: ", prefixToInfix(string))