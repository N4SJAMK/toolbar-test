#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
x11 Adaptercode for model based testing of Toolbar
Uses x11 to send events and receive screenshots

Image assets for image recognition are located in ../assets folder

########### NOTE: this adapter is outdated in terms of assets, use selenium adapter instead ###############

  Preconditions for use:
   - Machine has Firefox running
   - Firefox has its homepage set to Toolbar
   - Firefox window has focus before running

@author: Antti Minkkinen
'''
import os
import random
from glob import glob
from time import sleep
from utils import TypeHelper

import fmbtx11


pollTime = 0.3      #page change poll delay, used as delay in other actions too
                    #the more ram in testmachine the shorter pollTime can be used
                    
timeoutTime = 5.0   #max time between page loads
account = ""

d = fmbtx11.Screen(":0")
screenCount = 0
resultsPath = "../../fmbt-toolbar-testresults"

stateAssets = {
               "frontpage"  : "assets/try_white.png",
               "edit"       : "assets/addtab.png",
               "profile" : "assets/profilepage.png",
               "toolbars" : "assets/mytoolbars.png",
               "view_toolbar" : "assets/tabheadercorner.png",
               "register" : "assets/dialogcancel.png",
               "login" : "assets/dialogcancel.png",
               "add_link" : "assets/dialogsave.png",
               "add_tab" : "assets/dialogsave.png",
               "confirm_dialog" : "assets/dialogareyousure.png"
               }


def init():
    #print "<adapter_init>"
    d.setScreenshotDir(resultsPath)
    d.enableVisualLog(resultsPath + "/0toolbar.html")
    TypeHelper.initWords()
    
    global account
    if os.path.isfile('account'):
        f = open('account','r')
        account = f.readline()
    
    '''
    print "\t<adjust_oir_params>"
    s = rs()
    d.oirEngine().adjustParameters(s, "assets/logo.png")
    print "\t</adjust_oir_params>"
    print "</adapter_init>"
    '''

def cleanUp():
    return

'''
frontpage
'''
def clickTry():
    rs()
    d.tapBitmap("assets/try_white.png")
    wait()

def skipTutorial():
    wait()
    rs()
    d.tapBitmap("assets/exit.png")
    resetCursor()
    wait()
'''
navigation
'''
def checkNavbar():
    rs()
    return d.verifyBitmap("assets/logo.png")

def checkMenu():
    rs()
    return d.verifyBitmap("assets/lines.png")

def clickLogo():
    rs()
    d.tapBitmap("assets/logo.png")

def clickMenuRegister():
    rs()
    d.tapBitmap("assets/register.png")

def clickMenuLogin():
    rs()
    d.tapBitmap("assets/login.png")  
  
def clickLines():
    rs()
    d.tapBitmap("assets/lines.png")

def clickMenuToolbars():
    rs()
    d.tapBitmap("assets/menutoolbars.png")

def clickMenuProfile():
    rs()
    d.tapBitmap("assets/menuprofile.png")

def clickMenuLogout():
    rs()
    d.tapBitmap("assets/menulogout.png")
    
'''
edit page
'''
def selectTab():
    s = rs(False)
    d.oirEngine().addScreenshot(s)
    icons = d.oirEngine().findBitmap(s, "assets/tabcorner.png")
    active = d.oirEngine().findBitmap(s, "assets/tabcornerselected.png")
    icons = icons + active
    if len(icons) < 1:
        return
    item = random.choice(icons)
    x = item.coords()[0]
    y = item.coords()[1]
    
    d.tap((x,y))

def clickEditTab():
    rs()
    d.tapBitmap("assets/edittab.png")

def modifyToolbarTitle():
    s = rs(False)
    #d.tapOcrText("Save", tapPos=(0.5,-4.0))
    # TODO find a better way to find this element
    d.verifyBitmap("assets/logo.png")
    d.oirEngine().addScreenshot(s)
    search = d.oirEngine().findBitmap(s, "assets/logo.png")
    if len(search) < 1:
        return
    item = search[0]
    x = item.coords()[0]+100
    y = item.coords()[1]+110
    d.tap((x,y))
    sleep(pollTime)
    clearText()
    sleep(pollTime)
    typeDelay(TypeHelper.getBoardName())
    resetCursor()

def modifyTabTitle():
    rs()
    d.tapBitmap("assets/tabheadercorner.png", tapPos=(2.0,1.5))
    sleep(pollTime)
    clearText()
    sleep(pollTime)
    typeDelay(TypeHelper.getBoardName())
    resetCursor()

def checkLinks():
    rs()
    return d.verifyBitmap("assets/toolbar_icon_plus.png") or d.verifyBitmap("assets/toolbar_icon_minus.png")

def clickToggleLink():
    rs()
    d.tapBitmap("assets/toolbar_icon_plus.png") or d.tapBitmap("assets/toolbar_icon_minus.png")

def clickDeleteLink():
    rs()
    d.tapBitmap("assets/deletelink.png")

def clickDeleteTab():
    rs()
    d.tapBitmap("assets/deletetab.png")

def clickAddTab():
    rs()
    d.tapBitmap("assets/addtab.png")

def checkTabButton():
    rs()
    return d.verifyBitmap("assets/tabcorner.png")

def checkTab():
    rs()
    return d.verifyBitmap("assets/tabcornerselected.png") 

def clickRadio():
    rs()
    d.tapBitmap("assets/radiooff.png")

def changePassword():
    rs()
    d.tapBitmap("assets/textfield.png")
    clearText()
    typeDelay("password")

def checkSubmit():
    rs()
    return d.verifyBitmap("assets/submit.png")

def enterPassword():
    rs()
    d.tapBitmap("assets/textfield.png")
    typeDelay("password")

def clickSubmit():
    rs()
    d.tapBitmap("assets/submit.png")

def checkTextfield():
    rs()
    return d.verifyBitmap("assets/textfield.png")

def clickSave():
    rs()
    d.tapBitmap("assets/save.png")

def clickView():
    rs
    d.tapBitmap("assets/view.png")

def clickAddLink():
    rs()
    d.tapBitmap("assets/addlink.png")
'''
toolbars page
'''
def checkToolbar():
    rs()
    return d.verifyBitmap("assets/buttonedit.png")
def clickButtonEdit():
    rs()
    s = rs()
    d.oirEngine().addScreenshot(s)
    icons = d.oirEngine().findBitmap(s, "assets/buttonedit.png")
    if len(icons) < 1:
        return
    item = random.choice(icons)
    x = item.coords()[0]
    y = item.coords()[1]
    
    d.tap((x,y)) 

def selectToolbar():
    rs()
    s = rs()
    d.oirEngine().addScreenshot(s)
    toolbars = d.oirEngine().findBitmap(s, "assets/buttonedit.png")
    if len(toolbars) < 1:
        return
    item = random.choice(toolbars)
    x = item.coords()[0]-345
    y = item.coords()[1]
    
    d.tap((x,y)) 

def clickCreatenew():
    rs()
    d.tapBitmap("assets/createnew.png")
    
def clickDelete():
    rs()
    d.tapBitmap("assets/delete.png")

'''
profile page
'''
def typePassword():
    rs()
    d.tapBitmap("assets/passwordfield.png")
    typeDelay("password")
    pressKey("Tab")
    sleep(pollTime)
    typeDelay("password")
    pressKey("Tab")
    sleep(pollTime)
    typeDelay("password")

def clickChange():
    rs()
    d.tapBitmap("assets/change.png")

'''
register dialog
'''
def clickClose():
    rs()
    d.tapBitmap("assets/dialogclose.png")

def clickCancel():
    rs()
    d.tapBitmap("assets/dialogcancel.png")

def typeRegisterInfo():
    global account
    if account:
        return
    account = TypeHelper.getUsername()
    f = open('account','w')
    f.write(account)
    f.close()
    typeDelay(account)
    pressKey("Tab")
    sleep(pollTime)
    typeDelay("password")
    pressKey("Tab")
    sleep(pollTime)
    typeDelay("password")

def clickDialogRegister():
    rs()
    d.tapBitmap("assets/dialogregister.png")

def checkAccountCreated():
    rs()
    return d.verifyBitmap("assets/dialogaccountcreated.png")

def checkRegisterFail():
    rs()
    return d.verifyBitmap("assets/emailinuse.png") or d.verifyBitmap("assets/invalidemail.png")

'''
login dialog
'''
def typeLoginInfo():
    global account
    if len(account)<3:
        return
    clearText()
    typeDelay(account)
    pressKey("Tab")
    sleep(pollTime)
    clearText()
    typeDelay("password")
    sleep(pollTime)

def clickDialogLogin():
    rs()
    d.tapBitmap("assets/dialoglogin.png")

def deleteAccount(): #doesn't do anything on screen but deletes a file from disk
    global account
    account = ""
    if os.path.isfile("account"):
        os.remove("account")

def checkLoggedIn():
    rs()
    return d.verifyBitmap("assets/lines.png")

def checkLoginFail():
    rs()
    return d.verifyBitmap("assets/wrong.png") or d.verifyBitmap("assets/login.png")

'''
add_link dialog
'''
def addLinkTypeText():
    typeDelay(TypeHelper.getTicketName())
    pressKey("Tab")
    typeDelay(TypeHelper.getUrl())
    pressKey("Tab")
    typeDelay(TypeHelper.getTicketName())

def clickDialogSave():
    rs()
    d.tapBitmap("assets/dialogsave.png")
'''
add_tab dialog
'''
def addTabTypeText():
    typeDelay(TypeHelper.getBoardName())

def addTabSelectIcon():
    s = rs()
    d.oirEngine().addScreenshot(s)
    icons = d.oirEngine().findBitmap(s, "assets/iconselectcorner.png")
    if len(icons) < 1:
        return
    item = random.choice(icons)
    x = item.coords()[0]
    y = item.coords()[1]
    
    d.tap((x,y))

'''
confirm dialog
'''
def clickYes():
    rs()
    d.tapBitmap("assets/dialogyes.png")

def clickNo():
    rs()
    d.tapBitmap("assets/dialogno.png")
    
'''
password dialog
'''
def typePasswordDialog():
    rs()
    raise NotImplementedError()

def clickSetPassword():
    rs()
    raise NotImplementedError()

'''
utils
'''

def confirmResponse():
    rs()
    d.pressKey("Return")

def confirmAlert():
    rs()
    d.tapBitmap("assets/alertok.png")

def clickText(text):
    rs()
    d.tapOcrText(text, match=0.6)
    sleep(pollTime)

def clickImage(img):
    rs()
    d.tapBitmap("assets/"+img+".png")

def clickTextOver(text, param):
    rs()
    d.tapOcrText(text, param, match=0.6)

def pressKey(key):
    d.pressKey(key)

def typeText(text):
    typeDelay(text)
    
def typeDelay(msg):
    for x in xrange(0, len(msg)):
        d.pressKey(msg[x], hold=0.02)
    sleep(pollTime)

def getUsername():
    return TypeHelper.getUsername()

def wipeScreens():
    for f in glob (resultsPath + '/*.png'):
        os.unlink (f)
    for f in glob (resultsPath + '/*.xwd'):
        os.unlink (f)

def rs(delete = True):
    global screenCount, d
    # wipe screens
    if delete and screenCount > 20:
        wipeScreens()
        screenCount = 0
    screenCount += 1
    return d.refreshScreenshot()

def getAccount():
    return account

def wait(time=pollTime):
    sleep(time)

def resetCursor():
    d.tap((50,90))
    wait()

def clearText():
    wait(0.3)
    d.connection().sendKeyDown('Control_L')
    wait(0.1)
    d.pressKey('a')
    wait(0.1)
    d.connection().sendKeyUp('Control_L')
    wait(0.1)
    d.pressKey('BackSpace')

def checkState(stateToCheck):
    rs()
    if d.verifyBitmap(stateAssets[stateToCheck]):
        return True
    return False

def getState():
    rs()
    for state in stateAssets:
        if d.verifyBitmap(stateAssets[state]):
            return state
    
    return "undetermined"

'''
verifyStateChangeTo(newState):
    waits until state has changed to newState
    
    return True if state changed or False if timeout
'''
def verifyStateChangeTo(newState):
    if len(newState) < 1:
        return True
    rs()
    result = d.waitBitmap(stateAssets[newState], pollDelay=pollTime, waitTime=timeoutTime)
    return result

def checkExitDialog():
    rs()
    return d.verifyBitmap("assets/logo.png") or d.verifyBitmap("assets/try_white.png")