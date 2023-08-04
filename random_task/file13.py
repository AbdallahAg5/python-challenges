# How do you find the sum of n numbers in Python?
def sum(num):
    count = int()
    for i in range(len(num)):
        count += num[i]
    print(count)    


sum([1,2,3,4,5])