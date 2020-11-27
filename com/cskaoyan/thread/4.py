#子进程
import subprocess

print('$ nslooup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)