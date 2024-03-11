from my_queue import Queue

q = Queue(size=6)
q.data[2] = 10
q.data[3] = 12
q.start = 2
q.end = 3
q.enqueue(7)
print(q)
q.dequeue()
print(q)
q.enqueue(1)
print(q)
q.enqueue(6)
print(q)

q_1 = Queue(size=3)
q_1.enqueue(1)
q_1.enqueue(5)
q_1.enqueue(5)

q_2 = Queue(size=3)
q_2.enqueue(2)
q_2.enqueue(1)
q_2.enqueue(5)

q_3 = Queue(size=2)
q_3.enqueue(11)
q_3.enqueue(5)

print(q_1 < q_2)
print(q_3 < q_2)

print(sorted([q_1, q_2, q_3]))
