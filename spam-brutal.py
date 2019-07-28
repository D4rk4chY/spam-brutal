#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
import sys
import urllib2
import random
G0 = '\x1b[0;32m'
G1 = '\x1b[1;32m'
C0 = '\x1b[0;36m'
C1 = '\x1b[1;36m'
P0 = '\x1b[0;35m'
P1 = '\x1b[1;35m'
W0 = '\x1b[0;37m'
W1 = '\x1b[1;37m'
B0 = '\x1b[0;34m'
B1 = '\x1b[1;34m'
R0 = '\x1b[0;31m'
R1 = '\x1b[1;31m'
RE = '\x1b[0;0m'
D0 = '\x1b[0;90m'
LG = '\x1b[1;97;41m'


def logo(s):
    os.system('clear')
    os.system('clear')
    os.system('clear')
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)


logo('''

%s
___  ____ _  _ ___ ____ _     ____  ___    _    _    _
|__] |__/ |  |  |  |__| |     [__  │___│  /_\  │ \  / │
|__] |  \ |__|  |  |  | |___  ___] │     /   \ │  \/  │
%s---------------e.r.o.r------------------------
%s   Author : D4rk4chy                         %s
%s---------------0.4.0.4------------------------
  Gunakanlah dengan Bijak.
  '''
     % (P1, D0, LG, RE, D0))
try:
    numb = raw_input('   %s[+] %sTarget : ' % (P0, W0))
    print '   %s[+] %sSilahkan tunggu ...' % (P0, W0)
    urllib2.urlopen('https://sinafipika.000webhostapp.com/sms.php/sms.php?nomor=%s&paket=99999999999999999999999'
                     % numb)
    print '''   %s[+] %sSukses 

''' % (P0, G0)
    os.system('xdg-open https://www.youtube.com/watch?v=FS0HrrQzDXg')
except:
    print '''   %s[+] %sGagal 

''' % (P0, R0)
    os.system('xdg-open https://www.youtube.com/watch?v=FS0HrrQzDXg')
    exit()
