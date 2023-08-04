# Check if a String Ends with a Suffix
def check_prefix(string,prefix):
    if len(prefix) == 1 and string[-1] == prefix:
        print('the string you provided starts with :' + prefix)
    elif len(prefix) == 1 and string[-1] != prefix: 
        print('the string you provided does not  starts with : ' + prefix)
    elif  len(prefix) != 1:
            if string[-1:len(prefix)] == prefix:
                  print('the string you provided starts with :' + prefix)
            else:
                  print('the string you provided does not  starts with : ' + prefix)
                 

check_prefix("hello there",'e')