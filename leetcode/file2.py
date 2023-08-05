def isPalindrome(string):
    reversed_string = str(string)[::-1]

    if ( str(string) == reversed_string ):
      print("the provided string is a palindrome")
    else:
      print("the provided string is not a palindrome")


isPalindrome('-121')
isPalindrome(121)
isPalindrome(10)


