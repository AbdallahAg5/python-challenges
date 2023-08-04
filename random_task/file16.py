#  Change Commas by Dots in a String


def check_string(string):
    modified_string = str()
    for i in range(len(string)):
        if string[i] == '.':
            modified_string +=','
        else:
            modified_string+=string[i]  
    print(modified_string)

check_string("hello there .")            