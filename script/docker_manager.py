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




print """
<script>
function start(cname)
{
document.location='start_docker.py?x=' +cname;
}
function stop(cname)
{
document.location='stop_docker.py?x=' +cname;
}
function removedd(cname)
{
document.location='remove_docker.py?x=' +cname;
}





</script>
"""


print "<marquee >" +"<div align='center' valign='top'>" +"<h3>"+"Welcome  "+ docker_image.user+" Your password is "+docker_image.passwd +" and you are compromised." +"</div>"+ "</marquee>"


try:

	l=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	ccount=l["ccount"].value
except:
	pass
#print "hello"

s=commands.getoutput("sshpass -p {0} ssh -o {1} -l root {2} docker ps -a".format(spass,key,sip))



print "<table border='2'>"
print "<tr><th> Image name   </th> <th>Container Name </th> <th> Status </th>  <th> Start </th> <th> Stop</th> <th> Remove </th> </tr>"

z=1
for i in s.split("\n"):
	if z<=2:	
		z=z+1
		pass
	else:
		j=i.split()
		print	"<tr><td>"+j[1]+"</td> <td>"+j[-1]+"</td>" +  "<td>" + commands.getoutput('sshpass -p {0} ssh -o {1} -l root {2} docker inspect {3} | jq .[].State.Status'.format(spass,key,sip,j[-1])).split('\n')[1].strip('"') + "</td>"+     "<td>" +"<input type='button' name='start' value='" +   j[-1]+   "' onclick=start(this.value) />" + "</td>"  "<td>" +"<input type='button' name='stop' value='" +   j[-1]+   "' onclick=stop(this.value) />" + "</td> " + "<td>" +"<input type='button' name='remove' value='" +   j[-1]+   "' onclick=removedd(this.value) />" + "</td> " +   "</tr>"
		


print "</table>"

print "<form action='live_shell.py'>"
print "<hr /><br />Enter a Container name to open shell area: <input type='text' name='cname' /><br />"
print "Enter first command to run: <input type='text' name='cmnd' /><br />"
print "<input type='submit' /><br /><hr />"
print "</form>"

print "<div align='right'> <a href='docker_manager.py' > <b> Docker Manager </b> </a> </div>"
print "<div align='right'> <a href='../cloudindex.html'> Cloud Index Page </a>"


