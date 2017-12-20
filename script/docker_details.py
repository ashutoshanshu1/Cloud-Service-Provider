#!/usr/bin/python2
import os
import cgi
import Cookie
import commands
import docker_image

spass=docker_image.spass
key=docker_image.key
sip=docker_image.sip


ccount=cgi.FormContent()["ccount"][0]
print "set-cookie: ccount={}".format(ccount)
print


print "<marquee>" +"<div align='center' valign='top'>" +"<h3>"+"Welcome  "+ docker_image.user+" Your password is "+docker_image.passwd +" and you are compromised." +"</div>"+ "</marquee>"
print "<h1> Enter Container name and Choose docker image </h1>"

i=0
s=commands.getoutput("sshpass -p {0} ssh -o {1} -l root {2} docker images".format(spass,key,sip))
print "<form action='docker_start.py' >"

while i<int(ccount):

	print "Enter Container Name: <input type='text'" + " name='container{}'".format(i)+" />"
	

	print "<select name='image{}'>".format(i)
	z=1
	for m in s.split("\n"):
		if z<=2:
			z=z+1
		else:
			j=m.split()
			print "<option>" + j[0] + ":" + j[1] + "</option>"

	print "</select><br />"




	i=i+1












print "<br /><input type="+"submit" + " />"
print "</form>"










print "<div align='right'> <a href='docker_manager.py' > <b> Docker Manager </b> </a> </div>"
print "<div align='right'> <a href='../cloudindex.html'> Cloud Index Page </a>"











