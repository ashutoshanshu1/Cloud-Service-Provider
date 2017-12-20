#!/usr/bin/python2
import commands
import os
import Cookie
import cgi

print "content-type: text/html"
print


print """
<script>
function yes(pname,name){

document.location='getin.py?x='+pname+'/'+name

}




</script>
"""








def folderin(files):
	filess=os.listdir(files)
	b=files[8:]
	print "<br />"
	for a in filess:
		if a.find(".")>0:
			print "<a href='{}/{}'>".format(b,a) + a + "</a>"
			print "<br />"
		else:
			print "<form action='getin.py'>"
			n=files
			print "<input type='button' name='{}' value='{}' onclick='yes(this.name,this.value)' />".format(files,a)
			print "</form>"



files=cgi.FormContent()["x"][0]

folderin(files)
