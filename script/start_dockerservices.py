#!/usr/bin/python2

import os
import cgi
import Cookie
import commands
import docker_image

spass=docker_image.spass
key=docker_image.key
sip=docker_image.sip







s=cgi.FormContent()
dname=cgi.FormContent()['image'][0]
vname=cgi.FormContent()['version'][0]
a=[]
for i in s.keys():
	a.append(i)
	








commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} touch /commit/Dockerfile".format(spass,key,sip))
commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} chown apache /commit/Dockerfile".format(spass,key,sip))
commands.getstatusoutput("echo 'FROM centos' | sshpass -p {0} ssh -o {1} -l root {2} cat > /commit/Dockerfile".format(spass,key,sip))
for i in a:
	if i=="sshd":
		commands.getoutput("echo 'RUN yum install openssh -y' | sshpass -p {0} ssh -o {1} -l root {2} cat >> /commit/Dockerfile  ".format(spass,key,sip))
	if i=="httpd":
		commands.getoutput("echo 'RUN yum install httpd -y' | sshpass -p {0} ssh -o {1} -l root {2} cat >> /commit/Dockerfile  ".format(spass,key,sip))
	if i=="netools":
		commands.getoutput("echo 'RUN yum install net-tools -y' | sshpass -p {0} ssh -o {1} -l root {2} cat >> /commit/Dockerfile  ".format(spass,key,sip))
	if i=="python":
		commands.getoutput("echo 'RUN yum install python -y' | sshpass -p {0} ssh -o {1} -l root {2} cat >> /commit/Dockerfile  ".format(spass,key,sip))


commands.getoutput("sshpass -p {0} ssh -o {1} -l root {2} docker build -t {3}:{4} /commit".format(spass,key,sip,dname,vname))


print "location: docker_select.py"
print
	
