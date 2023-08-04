#  Remove Spaces from a String
def remove_spaces(string):
    modified_string=str()
    for i in range(len(string)):
       if string[i] == " ":
         modified_string = string.replace(string[i],'')
    print(modified_string) 

remove_spaces("hello there       ")          