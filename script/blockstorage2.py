#!/usr/bin/python2

import cgi
import commands

print "Content-Type: text/html"
print

vg="vg1"
user=cgi.FormContent()['username'][0]
clientpass=cgi.FormContent()['clientpass'][0]
clientip=cgi.FormContent()['clientip'][0]
size=cgi.FormContent()['size'][0]
ip="192.168.43.44"
paswd="suraj1996"
print "hello"
write2="""[storageserver]
{0}   ansible_ssh_user=root  ansible_ssh_pass={1}

[webserver]
{0}   ansible_ssh_user=root  ansible_ssh_pass={1}

[clientserver]
{2}   ansible_ssh_user=root  ansible_ssh_pass={3}
""".format(ip,paswd,clientip,clientpass)



f2=open("/project/ansible/hosts",'w')
f2.write(write2)
f2.close()



write1="""---
- hosts: storageserver
  tasks:

        - package:
                         name: "scsi-target-utils.x86_64"
                         state: present

        - file:
                         state: directory
                         path: "/gbs"

        - fetch:
                         src: "/etc/tgt/targets.conf"
                         dest: "/gbs/"
                         flat: yes

        - lvol:
                         vg: "{0}"
                         lv: "{1}"
                         size: "{2}"
                          
- hosts: webserver
  tasks:
        - file:
                         path: "/gbs/targets.conf"
                         owner: "apache"

        - blockinfile:
                         path: "/gbs/targets.conf"
                         block:  |
                           <target {1}>
                               backing-store /dev/{0}/{1}
                           </target>

- hosts: storageserver
  tasks:
        - copy:
                         src: "/gbs/targets.conf"
                         dest: "/etc/tgt/targets.conf"



        - service:
                         name: "tgtd"
                         state: restarted

- hosts: clientserver
  tasks:
        - open_iscsi:
                         show_nodes: yes
                         discover: yes
                         portal: {3}
                         login: yes
                         target: {1}



""".format(vg,user,size,ip)

f1=open("/project/ansible/yes.yml",'w')
f1.write(write1)
f1.close()


print commands.getstatusoutput("sudo ansible-playbook ../ansible/yes.yml -i ../ansible/hosts")

print "<br /><br /><br /><br />"

print "Block storage set up successfully"
print "<a href='../storagetype.html'> click here to go back </a> "

