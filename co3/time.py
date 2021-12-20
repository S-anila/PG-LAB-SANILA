
import time
t=time.localtime()
print("time:",t)
print("current year:",t.tm_year)
print("current month:",t.tm_mon)
print("current time in sec:",time.time())
#print("current time:",time.ctime())
print("current time after 30 sec:",time.ctime(time.time()+30))