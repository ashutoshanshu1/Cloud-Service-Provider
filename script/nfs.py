#!/usr/bin/python2
import cgi
import commands
import os
import Cookie
print "Content-Type: text/html"


#print cgi.FormContent()[][]

#username=cgi.FormContent()['username'][0]
drivesize=cgi.FormContent()['drivesize'][0]
clientip=cgi.FormContent()['clientip'][0]
passwd=cgi.FormContent()['passwd'][0]

sip="192.168.43.44"
spass="suraj1996"
vgname="vg1"
key="stricthostkeychecking=no"

print "set-cookie: ip={}".format(clientip)
print "set-cookie: passwd={}".format(passwd)
print "set-cookie: vgname={}".format(vgname)
print "set-cookie: sip={}".format(sip)
print "set-cookie: sip={}".format(spass)



l=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
m=l["x"].value
n=l["y"].value

username=m+"nfs"



a="{} {}".format(m,n)
b=commands.getoutput("sudo cat /project/script/users.txt")
if b.find(a)>=0:
	lvcreated=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} lvcreate --size {3}G --name {4} {5}".format(spass,key,sip,drivesize,username,vgname))

	
	lvformat=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} mkfs.ext4 /dev/{3}/{4}".format(spass,key,sip,vgname,username))


	createdir=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} mkdir -p /project/media/{3}".format(spass,key,sip,username))


	mount=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} mount /dev/{3}/{4} /project/media/{4}".format(spass,key,sip,vgname,username))

	permission=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} chown apache /etc/exports ".format(spass,key,sip))

#commands.getstatusoutput("sshpass -p {0} scp -o {1} root@ ".format(spass,key,sip,drivesize,username,vgname))

	updatefile=commands.getstatusoutput("echo '/project/media/{0} {1}(rw,no_root_squash)' | sshpass -p {2} ssh -o {3} -l root {4} 'cat >> /etc/exports' ".format(username,clientip,spass,key,sip))

	nfsrestarts=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} systemctl restart nfs".format(spass,key,sip))


	permissionmedia=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} chown apache /media/".format(passwd,key,clientip))
	


	createdirc= commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} mkdir -p /media/{3}".format(passwd,key,clientip,username))
	
	

#print commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} chown apache /media/{3}".format(spass,key,clientip,username))

	mountc=commands.getstatusoutput(" sshpass -p {0} ssh -o {1} -l root {2} mount {4}:/project/media/{3} /media/{3}".format(passwd,key,clientip,username,sip))
	
	print "location: ../creatednfs.html"
	print
	

else:
	print "location: ../login.html"
	print

