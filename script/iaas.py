#!/usr/bin/python2
import cgi
import commands
import os
print "content-type: text/html"



#print "hello"
ipAddress=cgi.FormContent()['ip'][0]
#print ipAddress
#userName=cgi.FormContent()['username'][0]
#print userName
userPassword=cgi.FormContent()['pass'][0]
#print userPassword
osName=cgi.FormContent()['osname'][0]
#print osName
#osType=cgi.FormContent()['ostype'][0]
#print osType
cpu=cgi.FormContent()['cpunumber'][0]
#print cpu
storage=cgi.FormContent()['storagesize'][0]
#print storage
ram=cgi.FormContent()['ramsize'][0]
#print ram


var="""#!/usr/bin/python2
import commands
import os

statusvnc=commands.getstatusoutput("rpm -q tigervnc")

if statusvnc[0]==0:
	pass
else:
	commands.getoutput("yum install tigervnc")

commands.getoutput("vncviewer 192.168.43.44:5901 ")
"""


"""
createdir=commands.getstatusoutput("sudo mkdir -p /tvnc")
createfile=commands.getstatusoutput("sudo touch /tvnc/vnc.py")
perm=commands.getstatusoutput("sudo chown apache /tvnc/vnc.py")
execute=commands.getstatusoutput("sudo chmod +x /tvnc/vnc.py") 

f=open("/tvnc/vnc.py","w")
f.write(var)
f.close()
"""
#ucreatedir=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} mkdir -p /tvnc")

#commands.getstatusoutput("sshpass -p {0} sudo scp -o stricthostkeychecking=no  /tvnc/vnc.py {1}:/root/Desktop/ ".format(userPassword,ipAddress))


commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no -l root 192.168.43.250 'bash -c \"export DISPLAY=:0 && virt-manager\"'")

osStatus=commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no -l root 192.168.43.250 sudo virt-install --name {0} --location /os/rhel-server-7.3-x86_64-dvd.iso --os-type linux --os-variant rhel7 --memory {1} --vcpus {2} --disk /var/lib/libvirt/images/myclientvm.qcow2,size={3}  --graphics vnc,password=redhat,listen=0.0.0.0,port=5901 --noautoconsole".format(osName,ram,cpu,storage))


commands.getstatusoutput("sshpass -p redhat ssh -o stricthostkeychecking=no -l root 192.168.43.250 'bash -c \"cd /webcontent/websockify-master && ./run 192.168.43.250:12344 192.168.43.250:5901\"'")



print "location: http://192.168.43.250/vnc/vnc.html"
print




