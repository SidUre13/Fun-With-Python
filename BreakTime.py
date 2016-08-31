#Program that pops up a youtube window in the browser in certain intervals, you can schedule your breaks within busy hours and listen to music
import time
import webbrowser
breaks = input("How many breaks you need ?") #number of breaks
breakinterval=input("How often you want to take a break (in seconds) ?") #number of breaks they want to take
YoutubeLink = raw_input("Paste the Youtube Link for your favourite Song")
i=0
print("The program is starting at", time.ctime())
while (i<breaks):
    print("Get to study. the next break is in", breakinterval, "seconds")
    time.sleep(breakinterval)
    print("Break starting at ",time.ctime)
    webbrowser.open(YoutubeLink)
    i=i+1
#Breaks interval project







