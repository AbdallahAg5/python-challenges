# Check if a String Starts with a Prefix
def check_prefix(string,prefix):
    if len(prefix) == 1 and string[0] == prefix:
        print('the string you provided starts with :' + prefix)
    elif len(prefix) == 1 and string[0] != prefix: 
        print('the string you provided does not  starts with : ' + prefix)
    elif  len(prefix) != 1:
            if string[0:len(prefix)] == prefix:
                  print('the string you provided starts with :' + prefix)
            else:
                  print('the string you provided does not  starts with : ' + prefix)
                 

check_prefix("hello there",'ohhh')