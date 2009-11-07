import urllib, urllib2
import socket
import sys

#import config

import sickbeard

from logging import *

XBMC_TIMEOUT = 10

# prevent it from dying if the XBMC call hangs
def notifyXBMC(input, title="midgetPVR"):

    global XBMC_TIMEOUT

    Logger().log("Sending notification for " + input, DEBUG)
    
    fileString = title + "," + input
    param = urllib.urlencode({'a':fileString})
    encodedParam = param.split("=")[1]
    
    Logger().log("Encoded message is " + encodedParam, DEBUG)
    
    host = sickbeard.XBMC_HOST
    
    try:
        urllib2.urlopen("http://" + host + "/xbmcCmds/xbmcHttp?command=ExecBuiltIn&parameter=Notification(" + encodedParam + ")", timeout=XBMC_TIMEOUT).close()
    except IOError as e:
        Logger().log("Warning: Couldn't contact XBMC HTTP server at " + host + ": " + str(e))
    
def updateLibrary(path=None):

    global XBMC_TIMEOUT

    Logger().log("Updating library in XBMC", DEBUG)
    
    host = sickbeard.XBMC_HOST
    
    try:
        if path == None:
            path = ""
        else:
            path = "," + urllib.quote_plus(path)
        urllib2.urlopen("http://" + host + "/xbmcCmds/xbmcHttp?command=ExecBuiltIn&parameter=XBMC.updatelibrary(video" + path + ")", timeout=XBMC_TIMEOUT).close()
    except IOError as e:
        Logger().log("Warning: Couldn't contact XBMC HTTP server at " + host + ": " + str(e))
