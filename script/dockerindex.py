#!/usr/bin/python2
import cgi
import commands
import os
import Cookie

print "Content-type: text/html"
 

data="suraj"

print "set-cookie: y={}".format(data)
print
print data

l=Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])

#print 
m=l["y"].value


print m




