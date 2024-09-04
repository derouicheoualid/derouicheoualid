#palindrome
def palindrome(num):
 str_num =str(num)

 if str_num == str_num [::-1]:
  return True
 else:
  return False

#test

num=12321
if( palindrome(num)):
  print (num ,"is palindrome")
else:
  print (num,"is not palindrome")






 



