"""
Core Server Definition and Control logics
"""
import dockercontroller
import loghandler
import platform
import uuid
import os
GameServers = [] # Game server list we need to use for tracking each server
def RunShell(command):
    if platform.system() != "Linux":
        print(command)
    else:
        os.system(command)

class GameServerSettings:
    def __init__(self,name,port,authport,profile):
        self.name = name
        self.port = port
        self.authport = authport
        self.profile = profile
        
class GameServer:
    def __init__(self,uid,status,settings):
        self.uid = uid
        self.status = status
        
        if settings.__class__.__name__ == "GameServerSettings":
            self.settings = settings
            GameServers.append(self)
        else:
            #print("Received GameServerSettings Classname: {}",settings.__class__.__name__)
            loghandler.printerror("GameServer settings is not a valid GameServerSettings object.")
           


        
            
    #Server control logic
    # 0 = Stopped, 1 = Starting, 2 = Running
    def isRunning(self):
        return self.status == 2
    def Stop(self):
        dockercontroller.StopInstance(self)
    def Start(self):
        dockercontroller.StartInstance(self)
        
    
        
def GetServers():
    return GameServers



def GetGameServer(uid):
    for server in GameServers:
        if server.uid == uid:
            return server
    return None

def GetGameServerByName(name):
    for server in GameServers:
        if server.settings.name == name:
            return server
    return None

def GetGameServerByPort(port):
    for server in GameServers:
        if server.settings.port == port:
            return server
    return None

def GetGameServerByAuthPort(port):
    for server in GameServers:
        if server.settings.authport == port:
            return server
    return None

def GetGameServerByProfile(profile):
    for server in GameServers:
        if server.settings.profile == profile:
            return server
    return None
# remove all servers
def RemoveAllServers():
    for server in GameServers:
        server.Stop()
        GameServers.remove(server)
        
def StartAllServers():
    for server in GameServers:
        server.Start()
def GetServerByIndex(idx):
    return GameServers[idx]

def GetServerIndex(server):
    return GameServers.index(server)

def GenerateUid():
    return "".join(str(ord(x)) for x in str(uuid.uuid4()))[:8]