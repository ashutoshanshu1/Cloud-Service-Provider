#!/usr/bin/python2

import cgi
import commands

print "Content-Type: text/html"
#print

username=cgi.FormContent()['username'][0]
passwd=cgi.FormContent()['passwd'][0]


#print username+" "+nickname




#print commands.getstatusoutput("sudo chown apache /project/script/users.txt")
 
f=open("/project/script/users.txt","a")
f.write("{} {} \n".format(username,passwd))
f.close()

#print commands.getoutput("sudo cat /project/script/users.txt")


print "location: ../login.html"
print








#print "Hello"

#c=commands.getoutput("cat /project/script/users.txt | grep {}".format(username))

#print c
	










