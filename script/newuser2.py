#!/usr/bin/python2
import cgi
import commands

print "Content-Type: text/html"
print

username=cgi.FormContent()['username'][0]
passwd=cgi.FormContent()['passwd'][0]
nickname=cgi.FormContent['nickname'][0]

print username+" "+nickname

