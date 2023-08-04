def divisibleBy(arr,divisor):
    finalArr=[]
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
          finalArr.insert(i,arr[i])
    print(finalArr)      


divisibleBy([0,1,2,3,4,5,6], 4)    