# avg of entered numbers

def get_numbers(num):
    arr = []
    for i in range(num):
       number = input("Enter number " +  str(i) + ' ')
       arr.insert(i,number) 
    count_avg(arr)   

def count_avg(arr):
    count=int()
    for i in range(len(arr)):
      count += int(arr[i])
    
    result = int(count / len(arr))
    print(result)


get_numbers(3)       