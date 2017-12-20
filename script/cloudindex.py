#!/usr/bin/python2

import cgi
import commands
import Cookie
import os

print "Content-Type: text/html"


service=cgi.FormContent()['service'][0]

#print os.environ
l=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])


m=l["x"].value
n=l["y"].value

a="{} {}".format(m,n)



b=commands.getoutput("sudo cat /project/script/users.txt")


if b.find(a)>=0:
        if service=="staas":
		print "location: ../storagetype.html"
		print
	elif service=="caas":
		print "location: docker_select.py"
		print
	elif service=="iaas":
		print "location: ../iaas.html"
		print
	elif service=="paas":
		print "location: ../paas.html"
		print
else:
        print "location: ../login.html"
	print









