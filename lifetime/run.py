import os
import json
import time
import subprocess

tm_st = time.time()

cmdCommand = 'powershell D:\\home\\site\\wwwroot\\coldstart\\record.exe' #specify your cmd command
process = subprocess.Popen(cmdCommand.split(), shell=True,stdout=subprocess.PIPE)
output5, error = process.communicate()

# postreqdata = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'w')
response.write("response time "+str(tm_st)+"@\n"+output5)
response.close()

import socket
import json
import os
import subprocess
import time
import subprocess

env_dist = os.environ
print env_dist.get('WEBSITE_INSTANCE_ID')
env1 = env_dist.get('WEBSITE_INSTANCE_ID')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
eip = s.getsockname()[0]
print 'eip ' + str(eip)

output6 = socket.getfqdn()
iip = socket.gethostbyname(socket.getfqdn()[:-1])
print 'iip ' + str(iip)

output7 = urlopen('http://ip.42.pl/raw').read()


cmdCommand = 'powershell D:\\home\\site\\wwwroot\\lifetime\\record.exe' #specify your cmd command
process = subprocess.Popen(cmdCommand.split(), shell=True,stdout=subprocess.PIPE)
output5, error = process.communicate()
print output5

log_file = 'D:\\local\\Temp\\lifetime_log.txt'
print os.path.exists(log_file)
if os.path.exists(log_file):
    output6 = 'TheLogFileExist'
    print output6
else:
    output6 = 'TheLogFileDONTExist'
    logfile = open(log_file, "wb")
    logfile.close()
    print output6


postreqdata = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'w')
response.write('#env#'+env1+'#iip#'+str(iip)+'#iip2#'+str(output7)+'#eip#'+str(eip)+'#address#'+output5+'#file#'+output6)
response.close()