#!/usr/bin/python2
import cgi
import commands
import os
import Cookie
print "Content-Type: text/html"

#sshfs

#username=cgi.FormContent()['username'][0]
drivesize=cgi.FormContent()['drivesize'][0]
clientip=cgi.FormContent()['clientip'][0]
passwd=cgi.FormContent()['passwd'][0]

sip="192.168.43.44"
spass="suraj1996"
vgname="vg1"
key="stricthostkeychecking=no"


#print "hello"


print "set-cookie: ip={}".format(clientip)
print "set-cookie: passwd={}".format(passwd)
print "set-cookie: sip={}".format(sip)
print "set-cookie: spass={}".format(spass)
print "set-cookie: vgname={}".format(vgname)

l=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
m=l["x"].value
n=l["y"].value

username=m


a="{} {}".format(m,n)
b=commands.getoutput("sudo cat /project/script/users.txt")


if b.find(a)>=0:


	lvcreate=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} lvcreate --size {3}G --name {4}sshfs {5}".format(spass,key,sip,drivesize,username,vgname))
	




	lvformat=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} mkfs.ext4 /dev/{3}/{4}sshfs".format(spass,key,sip,vgname,username))
	

	

	createdir=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} mkdir -p /media/{3}sshfs".format(spass,key,sip,username))
	
	

	mounts=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} mount /dev/{3}/{4}sshfs /media/{4}sshfs".format(spass,key,sip,vgname,username))
	
	
	
	own=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} chown apache /etc/exports ".format(spass,key,sip))
	
	
	


	#writec=commands.getstatusoutput("echo '/media/{0}sshfs {1}(rw,no_root_squash)' | sshpass -p {2} ssh -o {3} -l root {4} 'cat >> /etc/exports' ".format(username,clientip,spass,key,sip))
	
	
	

	restartnfs=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} systemctl restart nfs".format(spass,key,sip))
	
	
	


	useradd=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} useradd {3}sshfs".format(spass,key,sip,username))
	
	

	cpass=commands.getstatusoutput("echo '{4}' | sshpass -p {0} ssh -o {1} -l root {2} passwd {3}sshfs --stdin".format(spass,key,sip,username,passwd))	
	

	ownc=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} chown {3}sshfs /media/{3}sshfs".format(spass,key,sip,username))
	
	
	
	
	ownmod=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} chmod 700 /media/{3}sshfs".format(spass,key,sip,username))
	
	
	
	aown=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} chown apache /media/".format(passwd,key,clientip))
	

	
	
	

	mkdirc=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} mkdir -p /media/{3}sshfs".format(passwd,key,clientip,username))

	
	
	mountcl=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sshpass -p {0} sshfs {2}sshfs@{3}:/media/{2}sshfs /media/{2}sshfs".format(passwd,clientip,username,sip))

	#commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} systemctl restart nfs".format(passwd,key,clientip))

	
	print "location: ../createdsshfs.html"
	print
else:

	print "location: ../login.py"
	print


