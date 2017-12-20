#!/usr/bin/python2
import cgi
import commands
import Cookie
import os

print "Content-type: text/html"

try:

	l=os.environ

	z=0

	for cook in l.keys():
		if cook=='HTTP_COOKIE':
			z=1	

	
	if z==1: 
		l=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
		m=l["x"].value
		n=l["y"].value
		a="{} {}".format(m,n)
		b=commands.getoutput("sudo cat /project/script/users.txt")

		if int(b.find(a))>=0:
			print "location: ../cloudindex.html"
			print
		else:
			username=cgi.FormContent()['username'][0]
			passwd=cgi.FormContent()['passwd'][0]
			print "set-cookie: x={}".format(username)
			print "set-cookie: y={}".format(passwd)

			a="{} {}".format(username,passwd)
			b=commands.getoutput("sudo cat /project/script/users.txt")

			if b.find(a)>=0:
		        	print "location: ../cloudindex.html"
		        	print
			else:
		        	print "location: ../login.html"
		        	print
		

	else:

		username=cgi.FormContent()['username'][0]
		passwd=cgi.FormContent()['passwd'][0]
		print "set-cookie: x={}".format(username)
		print "set-cookie: y={}".format(passwd)
	
		a="{} {}".format(username,passwd)
	 
		b=commands.getoutput("sudo cat /project/script/users.txt")


		if b.find(a)>=0:
			print "location: ../cloudindex.html"
			print
		else:
			print "location: ../login.html"
			print

except:
	print "location: ../login.html"
	print

