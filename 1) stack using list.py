my_stack=[]
def pushelement():
    n=input("Enter the element to be pushed")
    my_stack.append(n)
    print(my_stack)
def popelement():
    if len(my_stack)==0:
        print("Stack is already empty")
    else:
        e=my_stack.pop()
        print(my_stack)

while True:
    print("1.push 2.pop 3.exit")
    userip=int(input("Enter the operations to be doned on stack"))
    if(userip==1):
        pushelement()
    elif(userip==2):
        popelement()
    elif(userip==3):
        print("you are exited the program")
        break
    else:
        print("Please Enter a valid operation")
