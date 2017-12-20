#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"


shellStatus=commands.getstatusoutput("sudo rpm -q shellinabox")
if shellStatus[0]!=0:
	shellInstallStatus=commands.getstatusoutput("sudo yum install shellinabox")
	if shellInstallStatus[0]==0:
		pass
	else:
		pass
else:
	pass
serviceStatus=commands.getstatusoutput("sudo systemctl start shellinaboxd.service")
print "location: shell-display1.py"
print
	








