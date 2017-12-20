#!/usr/bin/python2

import cgi
import commands

print "Content-Type: text/html"
print

user=cgi.FormContent()['user'][0]
paswd=cgi.FormContent()['paswd'][0]
ip=cgi.FormContent()['ip'][0]
vg=cgi.FormContent()['vg'][0]
clientpass=cgi.FormContent()['clientpass'][0]
clientip=cgi.FormContent()['clientip'][0]
size=cgi.FormContent()['size'][0]


#print user
#print paswd

write1="""---
- hosts: gb
  tasks:

        - package:
                         name: 'scsi-target-utils.x86_64'
                         state: present

        - file:
                         state: directory
                         path: '/gbs'

        - fetch:
                         src: '/etc/tgt/targets.conf'
                         dest: '/gbs/'
                         flat: yes

        - lvol:
                         vg: '{0}'
                         lv: '{1}'
                         size: '{2}'


""".format(vg,user,size)
f1=open("/project/ansible/part1.yml",'w')
f1.write(write1)
f1.close

print commands.getstatusoutput("sudo ansible-playbook -i ../ansible/part1.yml  ../ansible/hosts --syntax-check")


"""


commands.getstatusoutput("sudo chown apache /gbs/targets.conf")

#file creation
file1=open("/gbs/targets.conf",'a')
file1.write("<target {0}>\n\t\tbacking-store /dev/{1}/{0}\n</target>\n".format(user,vg))
file1.close()

#file upload
status=commands.getstatusoutput("sudo sshpass -p {0} scp -o stricthostkeychecking=no /gbs/targets.conf root@{1}:/etc/tgt/targets.conf".format(paswd,ip))
if status[0]==0:
   print "File sucessfully uploaded"
else:
   print "File not uploaded"

print "</br>"
#service startt

status=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} systemctl restart tgtd".format(paswd,ip))
if status[0]==0:
   print "Service Sucessfully started"
else:
   print "Service not started"




#print clientpass
#print clientip
#print ip
clientDisc=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} iscsiadm --mode discoverydb --type sendtargets --portal {2} --discover".format(clientpass,clientip,ip))
print clientDisc
if clientDisc[0]==0:
   print "Client Sucessfully discovered block"
else:
   print "Block not discovered"


clientLog=commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no {1} iscsiadm --mode node --targetname {3} --portal {2} --login".format(clientpass,clientip,ip,user))
if clientLog[0]==0:
   print "Client Sucessfully logged in"
else:
   print "Log in Unsuccessful"



"""
