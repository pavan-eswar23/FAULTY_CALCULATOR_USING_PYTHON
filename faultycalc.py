x=int(input("enter a number:"))
y=int(input("enter a number:"))
s=input("enter operation you want to perform")
if(x==56):
    print("56*3=444")
elif(x==55):
    print("55/6=4") 
elif(x==45):
    print("45+9=67")
else:
    if(s=="+"):
        print(x+y)
    elif(s=="*"):
        print(x*y)
    elif(s=="/"):
        print(x/y)        
            
