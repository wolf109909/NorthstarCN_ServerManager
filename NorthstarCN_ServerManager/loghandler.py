"""
Some functions for logging stuff
"""
debuglogging = True
errorlogging = True

def printerror(message):
    if errorlogging:
        print("[ERROR]: " + message)

def printdebug(message):
    if debuglogging:
        print("[DEBUG]: " + message)
 
def printinfo(message):
    print("[INFO]: " + message)