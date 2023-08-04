# Remove Characters at Even Indices
def remove_even_indexes(string):
    for i in range(len(string)):
        if i % 2 == 0:
            string.replace(string[i],'')
    print(string)

remove_even_indexes('hello there')        