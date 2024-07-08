def complexcalc():
 # a=int(input("Enter a number: "))
 # b=int(input("Enter a number: "))
 c=(input("enter the sign to use"))
 # if c=='-':
 #    result=a-b
 #    print(result)
 # elif c=='+':
 #    result=a+b
 #    print(result)
 # elif c=='*':
 #    result=a*b
 #    print(result)
 # elif c=='/':
 #
 #    if b==0:
 #        print("number cant be divided by zero")
 #        print("EXIT")
 #    else:
 #        result=a/b
 #        print(result)
 # elif c=='%':
 #    result=a%b
 #    print(result)
 # else:
 #    print("No operation can be done,YessiR")
 def add():
   a = int(input("Enter a number: "))
   b = int(input("Enter a number: "))
   result=a+b
   print(result)
 def sub():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    result=a-b
    print(result)
 def mul():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    result=a*b
    print(result)
 def div():
     a = int(input("Enter a number: "))
     b = int(input("Enter a number: "))
     result=a/b
     print(result)
 def mod():
     a = int(input("Enter a number: "))
     b = int(input("Enter a number: "))
     result=a%b
     print(result)
 def none():
     print("Naaah,, thats not a sign")
 if c=='-':
    sub()
 elif c=='+':
    add()
 elif c=='*':
   mul()
 elif c=='/':
     div()

 elif c=='%':
    mod()
 else:
     none()








complexcalc()


