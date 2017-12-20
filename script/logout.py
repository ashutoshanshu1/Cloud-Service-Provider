#!/usr/bin/python2
import os
import Cookie
import cgi
import commands


print "Content-type: text/html"

name="qwertyuiasdfgh"
passwp="rtyuioplkjhgfd"

print "set-cookie: x={}".format(name)
print "set-cookie: y={}".format(passwp)


print "location: ../login.html"
print
