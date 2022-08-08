import collections
stack=collections.deque()
n=int(input("Enter total elements: "))
for i in range(0,n):
    value=input()
    stack.append(value)
print(f"Your stack before pop: {stack}")
m=int(input("Enter total elements to be removed: "))
for j in range(0,m):
    if(m<=n):
        stack.pop()
    else:
        print("Stack will be emptied")
        break
print(f"your stack after pop is {stack}")
