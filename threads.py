
# coding: utf-8

# In[1]:


import time
import thread
def ok():
 while True :
  print"hey there"
  time.sleep(1)
def google():
 while True :
  print"bye there"
  time.sleep(2)
thread.start_new_thread(ok,())
thread.start_new_thread(google,())
while True :
    pass


