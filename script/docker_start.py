#!/usr/bin/python2
import os
import cgi
import Cookie
import commands
import docker_image

spass=docker_image.spass
key=docker_image.key
sip=docker_image.sip



print 



print "<marquee >" +"<div align='center' valign='top'>" +"<h3>"+"Welcome  "+ docker_image.user+" Your password is "+docker_image.passwd +" and you are compromised." +"</div>"+ "</marquee>"



l=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
ccount=l["ccount"].value

i=0
a=[]
b=[]

while i<int(ccount):
	c="image{}".format(i)
	d="container{}".format(i)
	a.append(cgi.FormContent()[c][0])
	b.append(cgi.FormContent()[d][0])
	i=i+1

i=0
while i<int(ccount):
	isthere=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} docker inspect {3}".format(spass,key,sip,b[i]))
	if isthere[0]==0:
		print "{0}: already exist try another name <br />".format(b[i])
	else:
		status=commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} docker run -dit --name {3} {4}".format(spass,key,sip,b[i],a[i]))
		if status[0]==0:
			print "{0}: running in background...<br />".format(b[i])
		else:
			print "Unexpected error occured starting {}....<br />".format(b[i])
	i=i+1



print "<marquee direction='right'>" + "Click <a href='docker_manager.py'> here </a> to go to <b>Docker Manager</b> <br />" + "</marquee>" 

print "<div align='right'> <a href='docker_manager.py' > <b> Docker Manager </b> </a> </div>"
print "<div align='right'> <a href='../cloudindex.html'> Cloud Index Page </a>"























