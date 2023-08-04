# Remove Characters at Even Indices
def remove_even_indexes(string):
    newString = str()
    for i in range(len(string)):
        if i % 2 == 0:
          newString = string.replace(string[i],'')
    print(newString)

remove_even_indexes('hello there')        