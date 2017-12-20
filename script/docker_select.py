#!/usr/bin/python2

import os
import cgi
import Cookie
import commands
import docker_image

print

print "<marquee>" +"<div align='center' valign='top'>" +"<h3>"+"Welcome  "+ docker_image.user+" Your password is "+docker_image.passwd +" and you are compromised." +"</div>"+ "</marquee>"




print "<form action="+"docker_details.py"+"> <br />"
#docker_image.docker_image_list()

#print "Enter Container name: <input type='text' name='cname' /> <br />"
print "Enter Number of containers for existing images: <input type='text' name='ccount' /><br />"
print "<input type='submit' /><br />"

print "</form>"


print "<form action='logout.py'>"
print "<button type='submit'>Logout</button>"
print "</form>"




print "<a href='start_dockerservice.py'>"+ "Want to create your own image ?" +"</a>"+"<br />"


print "<div align='right'> <a href='docker_manager.py' > <b> Docker Manager </b> </a> </div>"
print "<div align='right'> <a href='../cloudindex.html'> Cloud Index Page </a>"

