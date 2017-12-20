#!/usr/bin/python2
import cgi
import os
import Cookie
import commands


print "Content-type: text/html"


sip="192.168.43.44"
spass="suraj1996"
key="stricthostkeychecking=no"

l=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
user=l["x"].value
passwd=l["y"].value

def docker_image_list():
		


	s=commands.getoutput("sshpass -p {0} ssh -o {1} -l root {2} docker images".format(spass,key,sip))	

	

	print "<select name='image'>"
	z=1
	for i in s.split("\n"):
		if z<=2:
			z=z+1
		else:
			j=i.split()
			print "<option>" + j[0] + ":" + j[1] + "</option>"

	print "</select><br />"

	#print "<input type='submit' />"
	

