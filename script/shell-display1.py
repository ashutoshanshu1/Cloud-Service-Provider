#!/usr/bin/python2

print "content-type: text/html"
print

print """'
<center>
<iframe src="https://192.168.43.44:4200" height="70%" width="80%">
</iframe><br><br>
</center>
"""

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

print "<form action='get-editor.py'>"
print "<center><input type='submit' class ='button' value='Get Editor' /></center>"
print "</form>"


