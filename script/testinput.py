#!/usr/bin/python2
import cgi

print "Content-type: text/html"
print

print "<body bgcolor='456667'>"
print "<center>"
form=cgi.FieldStorage()
name=form.getvalue('name')
print "<form>"

print "<label>What is your name ?"

print "<input type='text' name='name'  /> </label>"
print "</form>"

print "<textarea>"+name+ "</textarea>"
print "</center>"
print "</body>"

