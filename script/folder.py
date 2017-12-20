#!/usr/bin/python2
import commands
import os
import Cookie
import cgi
#import getin

print "Content-type: text/html"
print

print """
<script>
function yes(name){

document.location='getin.py?x=/project/media/'+name

}




</script>
"""




folder=os.listdir("/project/media")
for files in folder:
	if files.find(".")>0:
		print "<a href='../{}'>".format(files) + files + "</a>"
		print "<br />"
	else:
		print "<form action='getin.py'>"
		print "<input type='button' name='filesure' value='{}' onclick='yes(this.value)' />".format(files)
		print "</form>"


print "<form enctype='multipart/form-date' action='uploadfile.py' method='post'>"
print "<input type='file' name='file' />"
print "<input type='submit' value='upload'/>"
print "</form>"
