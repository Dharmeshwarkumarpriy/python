import queue

q=queue.Queue()

# put the elements into the queue. ...
q.put(20)
q.put(30)
q.put(40)
q.put(50)

# get the queue. ...
print(q.get())
print(q.get())
print(q.get())
print(q.get())