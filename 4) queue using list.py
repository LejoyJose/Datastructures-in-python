queue=[]
def enqueue():
    e=input("Enter Element to be enqueued:")
    queue.insert(0,e)
def dequeue():
    if not queue:
        print("Queue is already empty",queue)
    else:
        queue.pop()
def display():
    print(queue)
    

while True:
    print("1-enqueue , 2=dequeue , 3-display,4-exit")
    n=int(input("Enter the operation to be performed:"))
    if(n==1):
        enqueue()
    elif(n==2):
        dequeue()
    elif(n==3):
        display()
    elif(n==4):
        print(queue)
        break
    else:
        print("Please select valid Operations")
