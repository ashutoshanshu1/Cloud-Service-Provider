#!/usr/bin/python2

import commands
import os
import Cookie
import cgi

docker_images:
	print "Content-type: text/html"
	print

#print "hello"

	print "<select name='image'>"
	for i in commands.getoutput("sudo docker images").split('\n'):
		j=i.split()
		print "<option> {0} : {1} </option>".format(j[0],j[1])	

	print "</select>"
