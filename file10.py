def solve(s):

   newString = "" 
   if len(s) > 0 and len(s) < 1000:
     words = s.split(' ')
     for i in range(len(words)):
      word = words[i]
      upper = word[0].upper() + word[1:]

      
      newString += upper + ' '   
        
   print(newString)     
      

solve("abdallah agmar")
