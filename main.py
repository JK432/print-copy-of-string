# Write a Python Program to get string which is n (non negative integer)       copies of a given string. 


def stringpro(str,a):
  print((str+" ")*(a-1),end="")
  print(str)



strg=input()
x=int(input())
stringpro(strg,x)



