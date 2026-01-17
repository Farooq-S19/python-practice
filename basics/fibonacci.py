# def fibonacci(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     else:
#         print(a, end=",")
#         print(b, end=",")
#         for i in range(2,n):
#             nex =a+b
#             a=b
#             b=nex
#             print(b,end=",")
# n =int(input("Enter number :"))
# fibonacci(n)
import re
def polindrome(txt):
    nom_txt=re.sub(r'[^a-z0-9]','',txt.lower())
    return nom_txt==nom_txt[::-1]
print(polindrome("Race car"))
print(polindrome("Race&#)#car"))