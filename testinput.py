#!/usr/bin/python2
import cgi

form=cgi.FieldStorage()
name=form.getvalue('name')
print """Content-type:text/html
<form>
<label>What is your name ?
<input type='text' name='name' value='{provided_name}' /> </label>
</form>

Hi <provided_name}""".format(provided_name=name)
