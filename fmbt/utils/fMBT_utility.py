#!/usr/bin/env python
# -*- coding: utf-8 -*- 
"""
Some misc. helper methods for GUI testing with fMBT

"""

import shutil
import os
import zipfile
import datetime
import pexpect
import codecs

"""
Transfers file to remote host
"""
def ScpTransfer(user, password, host, path, files):
    child = pexpect.spawn('scp %s %s@%s:%s' % (files, user, host,path))
    print 'scp %s %s@%s:%s' % (files, user, host,path)
    i = child.expect(['assword:', r"yes/no"], timeout=30)
    if i == 0:
        child.sendline(password)
    elif i == 1:
        child.sendline("yes")
        child.expect("assword:", timeout=30)
        child.sendline(password)
    data = child.read()
    print data
    child.close()

"""
wipes directory and makes a new one if necessary
"""

def initFMBT(screen, path):
    if not os.path.exists(path):
        os.makedirs(path)
    screen.setScreenshotDir(path)
    screen.enableVisualLog(path + "/testlog.html")
    
def wipeDir(path):
    if os.path.exists(path):
        shutil.rmtree(path)

"""
saves folder to a timestamped zipfile
"""
def saveResults(foldername):
    filename = 'test-results ' + str(datetime.datetime.now())
    zipf = zipfile.ZipFile(filename, 'w')
    zipdir(foldername, zipf)
    zipf.close()

def zipdir(path, zipfile):
    for root, files in os.walk(path):
        for f in files:
            zipfile.write(os.path.join(root, f))

def randomString():
    return os.urandom(3).encode('hex')

def readWordList(fileName):
    with codecs.open(fileName, "r", "utf-8") as f:
        words = f.readlines()
    return words
