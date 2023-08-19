#  function that takes a string. If the string is all uppercase characters, 
#  convert it to lowercase and add an exclamation mark at the end.


def upperToLower(string):
    lower = ""
    for i in range(1,len(string)):
      lower += string[i].lower()
    if(string.isupper()):
         print(string[0] +  lower + '!')  
    else:
        print(string[0].upper() +  lower )  
             

upperToLower("CAPS LOCK DAY IS OVER")   


