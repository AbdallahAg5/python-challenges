# Check if a String Only Contains Numbers
def check_string(string):
    message = str()
    for i in range(len(string)):
        if string[i].isnumeric() == True :
          message = "string contains a number"
        else:
           message = "string does not contain a number"  
    
    print(message)


check_string("hello there")        
