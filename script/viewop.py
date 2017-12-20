#!/usr/bin/python2

import cgi
import commands
import Cookie
import os

print"content-type: text/html" 
print
#print cgi.FormContent()

try:
	l=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	Language=l["lang"].value
	print Language
except:
	Language='PYTHON'
	pass



code1=cgi.FormContent()['code'][0]

print "\n\n\n" 
print "<pre>"

if Language == 'JAVA':
	commands.getoutput("sudo chown apache /project/script/prog.java")
	f=open("/project/script/prog.py",'w')
	f.write(code1)
	f.close()
	print commands.getoutput("sudo javac /project/script/prog.java")

elif Language == 'PYTHON':
	commands.getoutput("sudo chown apache /project/script/prog.py")
	f=open("/project/script/prog.py",'w')
	f.write(code1)
	f.close()
	print commands.getoutput("sudo python /project/script/prog.py")

elif Language == 'PHP':
	commands.getoutput("sudo chown apache /project/script/prog.php")
	f=open("/project/script/prog.php",'w')
	f.write(code1)
	f.close()
	print commands.getoutput("sudo python /project/script/prog.php")
print "</pre>"

