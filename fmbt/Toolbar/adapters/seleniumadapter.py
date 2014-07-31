#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Selenium adaptercode for model based testing of Toolbar

@author: Antti Minkkinen
'''
import os
import random
from glob import glob
from time import sleep, time, gmtime, strftime
from utils import TypeHelper

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC

b = webdriver.Firefox()
url = 'http://toolbar.n4sjamk.org'
b.get(url)

pollTime = 0.1      #page change poll delay, used as delay in other actions too
                    #the more ram in testmachine the shorter pollTime can be used
                    
timeoutTime = 1.0   #max time between page loads
account = ""

screenCount = 0
resultsPath = "../../fmbt-toolbar-testresults"

stateAssets = {
               "frontpage"    : ["page", "#btnTryDark"],
               "edit"         : ["page", "div#path.create"],
               "profile"      : ["page", "div#path.profile"],
               "toolbars"     : ["page", "div#path.toolbars"],
               "view_toolbar" : ["page", "div#path.bar"],
               "register" : ["dialog", "div#dialog-register"],
               "login"    : ["dialog", "div#dialog-login"],
               "add_link" : ["dialog", "div#dialog-newBox"],
               "add_tab"  : ["dialog", "div#dialog-newTab"],
               "confirm_dialog"  : ["dialog", "div#dialog-confirmation"],
               "edit_title"  : ["dialog", "div#dialog-editTitle"],
               "password_dialog"  : ["dialog", "div#dialog-setPassword"]
               }

def init():
    b.maximize_window()
    TypeHelper.initWords()
    
    global account
    if os.path.isfile('account'):
        f = open('account','r')
        account = f.readline()

def cleanUp():
    b.quit()
    return

'''
restart browser to release memory
'''
def reinitDriver():
    global b
    b.quit()
    b = webdriver.Firefox()
    b.get(url)
    b.maximize_window()

'''
frontpage
'''
def clickTry():
    b.find_element_by_id("btnTryDark").click()

def skipTutorial():
    wait()
    if isElement(".introjs-skipbutton"):
        b.find_element_by_css_selector("a.introjs-skipbutton").click()

'''
navigation
'''
def checkNavbar():
    return isElement("img#logo") or isElement("div#lines") or isElement("#btnLogin")

def checkMenu():
    return isElement("div#lines")

def clickLogo():
    b.find_element_by_id("logo").click()

def clickMenuRegister():
    rs()
    b.find_element_by_css_selector("button#btnRegister").click()

def clickMenuLogin():
    rs()
    b.find_element_by_css_selector("button#btnLogin").click()
        
def clickLines():
    rs()
    b.find_element_by_css_selector("div#lines").click()

def clickMenuToolbars():
    rs()
    b.find_element_by_css_selector("a[href=\"/bars\"]>div").click()

def clickMenuProfile():
    rs()
    b.find_element_by_css_selector("a[href=\"/profile\"]>div").click()

def clickMenuLogout():
    rs()
    b.find_element_by_css_selector("a[href=\"#\"]>div").click()

'''
edit page
'''
def selectTab():
    rs()
    icons = b.find_elements_by_css_selector("div.tab")
    item = random.choice(icons)
    item.click()

def clickEditTab():
    rs()
    b.find_element_by_css_selector("#btnEditTab").click()

def modifyToolbarTitle():
    rs()
    b.find_element_by_css_selector("#editBarTitle").click()

def checkLinks():
    rs()
    return isElement("div.boxExpand")

def clickToggleLink():
    rs()
    items = b.find_elements_by_css_selector("div.boxExpand")
    item = random.choice(items)
    item.click()

def clickDeleteLink():
    rs()
    items = b.find_elements_by_css_selector("div.boxRemove")
    item = random.choice(items)
    item.click()

def clickDeleteTab():
    rs()
    b.find_element_by_css_selector("#btnDeleteTab").click()

def clickAddTab():
    rs()
    b.find_element_by_css_selector("#btnOpenAddTab").click()

def checkTabButton():
    rs()
    return isElement("img.tabIcon")

def checkTab():
    rs()
    return isElement("div.tab") 

def checkSubmit():
    rs()
    return isElement("input[type=\"submit\"]")

def enterPassword():
    rs()
    textField = b.find_element_by_css_selector("input[type=\"password\"]")
    textField.click()
    textField.send_keys("password")

def clickSubmit():
    rs()
    b.find_element_by_css_selector("input[type=\"submit\"]").click()

def checkTextfield():
    rs()
    return isElement("input#txtBarPassword")

def clickSave():
    rs()
    b.find_element_by_css_selector("#btnCreateBar").click()
    
def clickView():
    rs
    b.find_element_by_css_selector("a#barLink").click()

def clickAddLink():
    rs()
    b.find_element_by_css_selector("div#btnAddBox").click()

def clickPassword():
    rs
    b.find_element_by_css_selector("#btnBarPassword").click()

'''
toolbars page
'''
def checkToolbar():
    rs()
    return isElement("button.delete")

def clickButtonEdit():
    rs()
    items = b.find_elements_by_css_selector("button[formaction=\"/edit\"]")
    item = random.choice(items)
    item.click()

def selectToolbar():
    rs()
    items = b.find_elements_by_css_selector("div.barsFieldTitle>a")
    item = random.choice(items)
    item.click()

def clickCreatenew():
    rs()
    b.find_element_by_css_selector("button#createNewBtn").click()

def clickDelete():
    rs()
    items = b.find_elements_by_css_selector("button.delete")
    item = random.choice(items)
    item.click()

'''
profile page
'''
def typePassword():
    b.find_element_by_css_selector("input#txtOldPassword").send_keys("password")
    b.find_element_by_css_selector("input#txtNewPassword").send_keys("password")
    b.find_element_by_css_selector("input#txtNewPassword2").send_keys("password")
    

def clickChange():
    b.find_element_by_css_selector("input#btnChange").click()
    

'''
register dialog
'''
def clickClose():
    rs()
    clickDialogButton(-1)

def clickCancel():
    rs()
    clickDialogButton(-1)

def writeAccount(acc = ""):
    global account
    if acc == "":
        account = TypeHelper.getUsername()
    else:
        account = acc
    print "\033[94m<variable name=\"account\">"+account+"</variable>\033[0m"
    f = open('account','w')
    f.write(account)
    f.close()

def typeRegisterInfo():
    global account
    if account:
        return
    writeAccount()
    
    email = b.find_element_by_css_selector("input#txtRegEmail")
    email.send_keys(account)
    
    password = b.find_element_by_css_selector("input#txtRegPassword")
    password.send_keys("password")
    password = b.find_element_by_css_selector("input#txtRegPassword2")
    password.send_keys("password")
    wait()

def clickDialogRegister():
    rs()
    clickDialogButton(0)

def checkAccountCreated():
    rs()
    lbl = b.find_element_by_css_selector("label#responseLbl")
    text = lbl.text
    if text == "Account created!":
        return True
    return False

def checkRegisterFail():
    rs()
    text = ""
    if isElement("label#responseLbl"):
        text = b.find_element_by_css_selector("label#responseLbl").text
    return checkAlert() or text == "Email address already in use!"

'''
login dialog
'''
def typeLoginInfo():
    global account
    if len(account)<3:
        return
    email = b.find_element_by_css_selector("input#txtLoginEmail")
    email.send_keys(account)
    
    password = b.find_element_by_css_selector("input#txtLoginPassword")
    password.send_keys("password")
    wait()

def clickDialogLogin():
    rs()
    clickDialogButton(0)

def deleteAccount(): #doesn't do anything on screen but deletes a file from disk
    global account
    account = ""
    if os.path.isfile("account"):
        os.remove("account")
    reinitDriver()
    wait(2.0)

def checkLoggedIn():
    rs()
    return isElement("div#lines")

def checkLoginFail():
    return checkAlert() or findElementByText("span.ui-dialog-title", "Authentication failed")

'''
edit title dialog
''' 
def typeToolbarTitle():
    textField = b.find_element_by_css_selector("input#txtBarTitle")
    textField.clear()
    textField.send_keys(TypeHelper.getBoardName())
    resetCursor()

'''
add_link dialog
'''
def addLinkTypeText():
    b.find_element_by_css_selector("input#txtBoxDesc").send_keys(TypeHelper.getTicketName())
    b.find_element_by_css_selector("input#txtBoxContent").send_keys(TypeHelper.getUrl())
    b.find_element_by_css_selector("input#txtBoxInfo").send_keys(TypeHelper.getTicketName())

def clickDialogSave():
    rs()
    clickDialogButton(0)

'''
add_tab dialog
'''
def addTabTypeText():
    tab = b.find_element_by_css_selector("input#txtTabTitle")
    tab.clear()
    tab.send_keys(TypeHelper.getBoardName())

def addTabSelectIcon():
    rs()
    icons = b.find_elements_by_css_selector("img.tabIcon")
    icon = random.choice(icons)
    icon.click()

'''
confirm dialog
'''
def clickYes():
    rs()
    clickDialogButton(0)

def clickNo():
    rs()
    clickDialogButton(-1)

'''
password dialog
'''
def typePasswordDialog():
    rs()
    b.find_element_by_css_selector("#txtBarPassword").send_keys("password")
    b.find_element_by_css_selector("#txtBarPassword2").send_keys("password")

def clickSetPassword():
    rs()
    clickDialogButton(0)

def checkPassword():
    rs()
    buttonSets = b.find_elements_by_css_selector("div.ui-dialog-buttonset")
    for buttonSet in buttonSets:
        if buttonSet.is_displayed():
            btns = buttonSet.find_elements_by_css_selector("button")
            if len(btns) == 3 and btns[1].is_displayed():
                return True
    return False

def clickRemovePassword():
    rs()
    clickDialogButton(1)

'''
utils
'''
def isElement(css):
    try:
        if b.find_element_by_css_selector(css).is_displayed():
            return True
        else:
            return False
    except:
        return False

def findElementByText(elementCss, text):
    if isElement(elementCss):
        elements = b.find_elements_by_css_selector(elementCss)
        for e in elements:
            if text not in e.text:
                elements.remove(e)
        elem = random.choice(elements)
        return elem
    return False


def clickDialogButton(button = 0):
    buttonSets = b.find_elements_by_css_selector("div.ui-dialog-buttonset")
    for buttonSet in buttonSets:
        if buttonSet.is_displayed():
            btn = buttonSet.find_elements_by_css_selector("button")[button]
            btn.click()
            return True

def checkAlert():
    try:
        WebDriverWait(b,timeoutTime).until(EC.alert_is_present())
        if EC.alert_is_present() == False:
            return False
        else:
            return True
    except:
        return False

def confirmAlert():
    if checkAlert():
        Alert(b).accept()
    
def confirmResponse():
    if isElement("div#dialog-response"):
        clickDialogButton(0)

def pressKey(key):
    b.switch_to().active_element().send_keys(Keys.RETURN)

def getUsername():
    return TypeHelper.getUsername()

def wipeScreens():
    for f in glob (resultsPath + '/*.png'):
        os.unlink (f)
    for f in glob (resultsPath + '/*.xwd'):
        os.unlink (f)

def rs(delete = True):
    return # for now
    '''
    Refresh screenshot. Deletes screenshots if limit has been reached.
    params:
        Bool delete , set false to skip deleting
    '''
    global screenCount
    # wipe screens
    if delete and screenCount > 20:
        wipeScreens()
        screenCount = 0
    screenCount += 1
    stamp = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
    b.save_screenshot(resultsPath + "/"+stamp+".png")

def getAccount():
    return account

def wait(time=pollTime):
    sleep(time)

def resetCursor():
    # not required in selenium
    return

def clearText():
    b.switch_to().active_element().clear()

def checkState(stateToCheck):
    '''
        checks if the current state is stateToCheck
    '''
    rs()
    if isElement(stateAssets[stateToCheck]):
        return True
    return False

def getState(): # TODO fix
    '''
        returns the state if found in stateAssets
    '''
    rs()
    for state in stateAssets:
        if isElement(stateAssets[state]):
            return state
    
    return "undetermined"


def verifyStateChangeTo(newState):
    '''
        waits until state has changed to newState
        
        return True if state changed or False if timeout
    '''
    if len(newState) < 1:
        return True
    startTime = time()
    while time() - startTime < timeoutTime:
        try:
            if stateAssets[newState][0] == "dialog" and isElement(stateAssets[newState][1]):
                return True
            elif stateAssets[newState][0] == "page"   and b.find_element_by_css_selector(stateAssets[newState][1]):
                return True
        except:
            wait()
            continue
    return False

def checkExitDialog():
    rs()
    return isElement("div.ui-widget-overlay") == False
