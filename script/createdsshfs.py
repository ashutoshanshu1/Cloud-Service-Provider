#!/usr/bin/python2
import cgi
import commands
import os
import Cookie

print "Content-type: text/html"

data=cgi.FormContent()['use'][0]

sip="192.168.43.44"

l=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
m=l["x"].value
n=l["y"].value
a="{} {}".format(m,n)
ip=l["ip"].value

m=m+"sshfs"
passwd=l["passwd"].value



b=commands.getoutput("sudo cat /project/script/users.txt")


if int(b.find(a))>=0:
	if data=="unmount":
		umount=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} umount /media/{2}".format(passwd,ip,m))
		print "location: ../createdsshfs.html"
		print
	elif data=="mount":
		commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} mkdir -p /media/{2}".format(passwd,ip,m))
		mount=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sshpass -p {0} sshfs {2}@{3}:/media/{2} /media/{2}".format(passwd,ip,m,sip))
		print "location: ../createdsshfs.html"
		print
 
	else: 
		print "location: ../resize.html"
		print


	
	



else:
	print "location: ../login.html"
	print



