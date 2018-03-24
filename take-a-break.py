import time
import webbrowser

timeToWait = 3
breakCount = 0
totalBreaks = 3

#time.ctim() gives a timestamp for current time
print("Started timer at " + time.ctime())
while breakCount < totalBreaks:      
    #time.sleep() uses seconds. 7200 seconds = 2 hours
    time.sleep(timeToWait)
    webbrowser.open("https://www.youtube.com/watch?v=ZYC1lrSdSk8")
    break_count += 1

