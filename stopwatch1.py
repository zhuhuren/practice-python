import time

print('Press Enter to start. Afterwards press Enter to click the stop watch. Press ctr-C to end it.')
input()
print('Started')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        now = time.time()
        lapTime = round((now - lastTime), 2)
        totalTime = round((now - startTime), 2)
        lastTime = now
        print('Lap #{}:\tlap {}s,\ttotal {}s'.format(str(lapNum).zfill(2), lapTime, totalTime), end = '')
        lapNum += 1
        
except:
    KeyboardInterrupt
    print('\nDone')
