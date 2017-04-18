import os
os.chdir("/etc/mysql/newcerts")
os.system('python genCert.py')
