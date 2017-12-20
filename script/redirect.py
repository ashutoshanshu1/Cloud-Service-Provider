#!/usr/bin/python2
print "content-type: text/html"

import cgi
import commands




Language=cgi.FormContent()['lang'][0]
userName=cgi.FormContent()['user'][0]
userPassword=cgi.FormContent()['pass'][0]

print "set-cookie: lang={}".format(Language)
print 
if Language=='PYTHON':
	print """
		<html>
		<head>
		<style>
		.button {
  		background-color: #008CBA; /* Blue */
    		border: none;
    		color: white;
    		padding: 15px 32px;
    		text-align: center;
    		text-decoration: none;
    		display: inline-block;
    		font-size: 16px;
	    	margin: 0 auto;
    		cursor: pointer;
		}
		</style>
		</head>
		</html>
	      """

	userAddStatus=commands.getstatusoutput("sudo useradd {} ".format(userName))
	print userAddStatus
	passwordStatus=commands.getstatusoutput("echo {0} |sudo passwd {1} --stdin".format(userPassword,userName))
	print passwordStatus
	print """
	<form action='shell-display1.py'>
	<center><br><br><br><br><br><br><br><br><br>
	<input type='submit' name='ch' class='button' value='Get Online Interpreter' />
	</form>
	<br><br><br><br>
	<form action='get-editor.py'>
	<input type='submit' name='ch' class='button' value='Write Code' />
	</center>
	</form>
	"""
	
else:
	print """
		<html>
		<head>
		<style>
		.button {
  		background-color: #008CBA; /* Blue */
    		border: none;
    		color: white;
    		padding: 15px 32px;
    		text-align: center;
    		text-decoration: none;
    		display: inline-block;
    		font-size: 16px;
	    	margin: 0 auto;
    		cursor: pointer;
		}
		</style>
		</head>
		</html>
	      """

	print """		
	<form action='get-editor.py'>
	<center><br><br><br><br><br><br><br><br><br>
	<input type='submit' name='ch' value='Write Code' />
	</center>
	</form>
	"""



