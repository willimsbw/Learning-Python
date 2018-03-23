import time
import webbrowser

timeToWait = 3
break_count = 0
total_breaks = 3

print("Started timer at " + time.ctime())
while break_count < total_breaks:      
    #time.sleep() uses seconds. 7200 seconds = 2 hours
    time.sleep(3)
    webbrowser.open("https://www.youtube.com")
    break_count += 1

