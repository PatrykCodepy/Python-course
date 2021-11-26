import subprocess
import os

address = "8.8.8.8"
res = subprocess.call(['ping', address])
#os.system("ping  %s" % address)
if res == 0:
	print("ping to", address, "OK")
elif res == 2:
    print("no response from", address)
else:
    print("ping to", address, "failed!")

#ping 8.8.8.8 TTL-114