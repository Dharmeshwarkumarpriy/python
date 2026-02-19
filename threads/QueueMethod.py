import queue

q=queue.Queue()
n=int(input("enter the value:"))
for i in range(n):
    q.put(i)

    while not q.empty():
        print(q.get())