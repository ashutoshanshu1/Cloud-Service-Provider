#!/usr/bin/python2
import cgi
import commands
import os
import Cookie
print "Content-Type: text/html"

storagetype=cgi.FormContent()['storage'][0]

l=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])

m=l["x"].value
n=l["y"].value

a="{} {}".format(m,n)

b=commands.getoutput("sudo cat /project/script/users.txt")

if b.find(a)>=0:
	if storagetype=="object":
		print "location: ../objectstorage.html"
		print
	elif storagetype=="block":
		print "location: ../blockstorage.html"
		print

else:
	print "location: ../login.py"
	print













