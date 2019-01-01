import time
import webbrowser
count=0
print("this program is started on"+time.ctime())
while(count<3):
      count+1
      time.sleep(10)
      webbrowser.open("youtube.com")