#!/usr/bin/python2

import os
import cgi
import Cookie
import commands
import docker_image

spass=docker_image.spass
key=docker_image.key
sip=docker_image.sip


try:
	cname=cgi.FormContent()['cname'][0]
	commands.getstatusoutput("sshpass -p {0} ssh -o {1} -l root {2} docker start {3}".format(spass,key,sip,cname))
except:
	pass

cmnd=cgi.FormContent()['cmnd'][0]


try:
	l=Cookie.SimpleCookie(os.environ['HTTP_COOKIE'])
	cname=l['cnames'].value
except:
	pass



print "set-cookie: cnames={}".format(cname)

print

print """

<script>


function changes(changename)
{
var cname=changename
var textarea1=document.getElementById('t1').value;
document.getElementById('t2').value=changename;
}




</script>

"""










print "<marquee >" +"<div align='center' valign='top'>" +"<h3>"+"Welcome  "+ docker_image.user+" Your password is "+docker_image.passwd +" and you are compromised." +"</div>"+ "</marquee>"

print "Container name: {}".format(cname)


print "<form action='live_shell.py'>"
print "<textarea name='cmnd' rows='15' cols='50' id='t1'>"+ "</textarea>"
#print "<textarea name='outputs' rows='10' cols='50' id='t2'>"+"</textarea>"
print "<input type='submit' />"
print "</form>"


print "<br />"



z=1
for i in commands.getoutput("sshpass -p {0} ssh -o {1} -l root {2} docker exec {3} {4}".format(spass,key,sip,cname,cmnd)).split("\n"):
	if z==1:
		z=z+1
		pass
	else:
		for j in i.split():
			print j
	print "<br />"
		




print "<div align='right'> <a href='docker_manager.py' > <b> Docker Manager </b> </a> </div>"
print "<div align='right'> <a href='../cloudindex.html'> Cloud Index Page </a>"



