import collections
q=collections.deque()
n=int(input("Enter total elements to be added to the queue: "))
for i in range(n):
    elements=input()
    q.append(elements)
m=int(input("Enter total elements to be removed from the queue: "))
for j in range(m):
      q.popleft()
print(q)

