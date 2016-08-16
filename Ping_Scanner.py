#PING_SCANNER_VERSION_2.0
#`				COPY_RIGHTS_TO_CYBERSECURITYWORKS.PVT.LTD
#USAGE_FORMAT: 			In command prompt enter ping_scanner.py [IP_ADDRESS OR SUBNET OR RANGE]
#EXAMPLE:				Ping_Scanner.py 192.168.1.1 
#EXAMPLE:				Ping_Scanner.py 192.168.1.0/24 
#EXAMPLE:				Ping_Scanner.py 192.168.1.1-192.168.1.25 
import re
import sys
import os
import subprocess
s =  """      _ __    .=-.-..-._            _,---.            ,-,--.    _,.----.    ,---.      .-._        .-._           ,----.               
  .-`.' ,`. /==/_ /==/ \  .-._ _.='.'-,  \         ,-.'-  _\ .' .' -   \ .--.'  \    /==/ \  .-._/==/ \  .-._ ,-.--` , \  .-.,.---.   
 /==/, -   \==|, ||==|, \/ /, /==.'-     /        /==/_ ,_.'/==/  ,  ,-' \==\-/\ \   |==|, \/ /, /==|, \/ /, /==|-  _.-` /==/  `   \  
|==| _ .=. |==|  ||==|-  \|  /==/ -   .-'         \==\  \   |==|-   |  . /==/-|_\ |  |==|-  \|  ||==|-  \|  ||==|   `.-.|==|-, .=., | 
|==| , '=',|==|- ||==| ,  | -|==|_   /_,-.         \==\ -\  |==|_   `-' \\==\,   - \ |==| ,  | -||==| ,  | -/==/_ ,    /|==|   '='  / 
|==|-  '..'|==| ,||==| -   _ |==|  , \_.' )        _\==\ ,\ |==|   _  , |/==/ -   ,| |==| -   _ ||==| -   _ |==|    .-' |==|- ,   .'  
|==|,  |   |==|- ||==|  /\ , \==\-  ,    (        /==/\/ _ |\==\.       /==/-  /\ - \|==|  /\ , ||==|  /\ , |==|_  ,`-._|==|_  . ,'.  
/==/ - |   /==/. //==/, | |- |/==/ _  ,  /        \==\ - , / `-.`.___.-'\==\ _.\=\.-'/==/, | |- |/==/, | |- /==/ ,     //==/  /\ ,  ) 
`--`---'   `--`-` `--`./  `--``--`------'          `--`---'              `--`        `--`./  `--``--`./  `--`--`-----`` `--`-`--`--'  """
print s
hostIP = sys.argv[1]
l = []
j  = ""
l1 = ['0', '0']
l2 = ['1']
l3 = ['1']
c1 = 0
count = 0
v1 = hostIP
l1 = v1.split("-")	
def ping_range():
	v1= l1[0]
	v2= l1[1]
	c1 =0
	l2 = v1.split(".")
	l3 = v2.split(".")
	start = int(l2[3])
	end = int(l3[3])
	end = end+1
	for i in range(start,end):
		i = str(i)
		j=str(eval(i))
		command = "ping"+" "+l2[0]+"."+l2[1]+"."+l2[2]+"."+j 
		pro = subprocess.Popen(command, stdout = subprocess.PIPE, shell = True)
		(out,err) = pro.communicate()
		if "TTL" in out:
			print l2[0]+"."+l2[1]+"."+l2[2]+"."+j+" is active"
			c1 = c1+1
	print "No of IPs active "+str(c1)
def ping_subnet():
	
	(addrString, cidrString) = sys.argv[1].split('/')
	c1 = 0
	
	addr = addrString.split('.')
	cidr = int(cidrString)

	
	mask = [0, 0, 0, 0]
	for i in range(cidr):
		mask[i/8] = mask[i/8] + (1 << (7 - i % 8))

	
	net = []
	for i in range(4):
		net.append(int(addr[i]) & mask[i])

	
	broad = list(net)
	brange = 32 - cidr
	for i in range(brange):
		broad[3 - i/8] = broad[3 - i/8] + (1 << (i % 8))
	start = int(net[3])+1
	end = int(broad[3])-1
	for i in range(start,end):
		i = str(i)
		j=str(eval(i))
		
		command = "ping"+" "+str(net[0])+"."+str(net[1])+"."+str(net[2])+"."+j 
		
		pro = subprocess.Popen(command, stdout = subprocess.PIPE, shell = True)
		(out,err) = pro.communicate()
		
		if "TTL" in out:
			
			print str(net[0])+"."+str(net[1])+"."+str(net[2])+"."+j+" is active"
			c1 = c1+1
	print "No of IPs active "+str(c1)
def ping_single():
	v1 = sys.argv[1]
	command = "ping"+" "+v1
	v = subprocess.Popen(command, stdout = subprocess.PIPE, shell = True)
	(out,err) = v.communicate()
	if "TTL" in out:
		print v1+" is active"

def execute():
	if "/" in hostIP:
		ping_subnet()
	if "-" in hostIP:
		ping_range()
	if test:
		ping_single()		
pat2= re.compile("(^127\.)|(^10\.)|(^172\.1[6-9]\.)|(^172\.2[0-9]\.)|(^172\.3[0-1]\.)|(^192\.168\.)")
test2 = pat2.match(hostIP)
if test2:
   print "IP address accepted"
   pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
   test = pat.match(hostIP)
   execute()
else:
	print "Enter the correct IP"
   


