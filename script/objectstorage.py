#!/usr/bin/python2
import cgi
import commands
import os
import Cookie
print "Content-Type: text/html"
#print 
#print "Hello"


l=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
m=l["x"].value
n=l["y"].value
sip="192.163.43.44"
spass="suraj1996"
vgname="vg1"




print "set-cookie: ip={}".format(sip)
print "set-cookie: spass={}".format(spass)
print "set-cookie: vgname={}".format(vgname)

a="{} {}".format(m,n)
b=commands.getoutput("sudo cat /project/script/users.txt")
if b.find(a)>=0:
	protocol=cgi.FormContent()['protocol'][0]
	if protocol=="nfs":
		print "location: ../nfs.html"
		print
	elif protocol=="sshfs":
		print "location: ../sshfs.html"
		print
		
else:
	print "location: ../login.html"
	print















