#!/usr/bin/python2

import os
import cgi
import Cookie
import commands
import docker_image

spass=docker_image.spass
key=docker_image.key
sip=docker_image.sip

print


print """
<script>

function sw()
{
document.location='docker_manager.py';
}

</script>
"""


print "<marquee >" +"<div align='center' valign='top'>" +"<h3>"+"Welcome  "+ docker_image.user+" Your password is "+docker_image.passwd +" and you are compromised." +"</div>"+ "</marquee>"

x=cgi.FormContent()['x'][0]

s=commands.getoutput('sshpass -p {0} ssh -o {1} -l root {2} docker inspect {3} | jq .[].State.Status'.format(spass,key,sip,x)).split('\n')[1].strip('"')

commands.getstatusoutput('sshpass -p {0} ssh -o {1} -l root {2} docker rm -f {3}'.format(spass,key,sip,x))
print "<script> sw()</script>"












