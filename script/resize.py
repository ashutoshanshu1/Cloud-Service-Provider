#!/usr/bin/python2
import cgi
import commands
import os
import Cookie

print "Content-type: text/html"

data=cgi.FormContent()['size'][0]

sip="192.168.43.44"
spass="suraj1996"
l=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
m=l["x"].value
n=l["y"].value
a="{} {}".format(m,n)
ip=l["ip"].value
m=m+"sshfs"
passwd=l["passwd"].value



b=commands.getoutput("sudo cat /project/script/users.txt")


if int(b.find(a))>=0:
	umount=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} umount /media/{2}".format(passwd,ip,m))
	extend=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} lvextend --size +{2}G /dev/vg1/{3}".format(spass,sip,data,m))
	reformat=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} resize2fs /dev/vg1/{2}".format(spass,sip,m))
	mount=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} mount {3}:/media/{2} /media/{2}".format(passwd,ip,m,sip))
	print "location: ../createdsshfs.html"
	print

else:
	print "location: ../login.html"
	print


