# function that, given the start_of_range and end_of_range values, 
# returns a list containing all the numbers inclusive to that range.

def reversible_inclusive_list(start_of_range,  end_of_range):
    arr=[]
    if start_of_range < end_of_range :
        for i in range(start_of_range,end_of_range + 1 ):
            arr.append(i)
        return arr
    else:
        for i in range(start_of_range,end_of_range - 1  ,-1 ):
            arr.append(i)
        return arr

print(reversible_inclusive_list(20,10))
print(reversible_inclusive_list(2,6))