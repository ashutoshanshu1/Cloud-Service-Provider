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

print """
<h1> Choose Services to start </h1>
<form action='start_dockerservices.py'  >
Imagename: <input type='text' name='image' /><br />
Version name: <input type='text' name='version' /> <br />
SSHD: <input type='checkbox' name='sshd' value='sshd' /><br />
HTTPD: <input type='checkbox' name='httpd' value='httpd' /><br />
Net-Tools: <input type='checkbox' name='netools' value='netools' /><br />
Python2: <input type='checkbox' name='python' value='python' /><br />
<input type='submit' />
</form>
"""


print "<div align='right'> <a href='docker_manager.py' > <b> Docker Manager </b> </a> </div>"
print "<div align='right'> <a href='../cloudindex.html'> Cloud Index Page </a>"
