import time
# two main functions to measure th time taken by a program: time.perf_counter, time.process_time
t1 = time.perf_counter()
for i in range(0, 1001, 100):
    print(i, end=', ')
print('\b\b')
time.sleep(10)
t2 = time.perf_counter()
print('Time taken by the program: ', t2-t1)
