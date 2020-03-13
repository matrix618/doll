import time
count = 0 
a = input('time:') 
b = int(a)
while (count < b):
    ncount = b - count
    print(ncount)
    time.sleep(1)
    count = count + 1


print('done')
