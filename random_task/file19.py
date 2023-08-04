# Check if a String Ends with a Suffix
def check_prefix(string,prefix):
    if string.endswith(prefix):
     print('the string you provided end with :' + prefix)
    else:
     print('the string you provided does not  end with : ' + prefix)
                 

check_prefix("hello theree",'eeeee')