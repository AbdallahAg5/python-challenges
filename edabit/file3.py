# Given two strings comprised of + and -, 
# return a new string which shows how the two strings interact

def neutralise(series_a: str, series_b: str) -> str:
    newString=""
    for i in range(len(series_a)):
            if(series_a[i] == '+' and series_b[i] == '-' or  series_a[i] == '-' and series_b[i] == '+'):
                 newString += "0"
            if(series_a[i] == '-' and series_b[i] == '-'):
                 newString += "-"
            if(series_a[i] == '+' and series_b[i] == '+'):
                 newString += "+"

    return newString


print(neutralise("-++-", "-+-+"))
print(neutralise("-+-+-+", "-+-+-+"))
