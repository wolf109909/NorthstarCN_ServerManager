"""
Core Server Definition and Control logics
"""
import dockercontroller
import loghandler
import uuid
GameServers = [] # Game server list we need to use for tracking each server

class GameServerSettings:
    def __init__(self,name,port,authport,profile):
        self.name = name
        self.port = port
        self.authport = authport
        self.profile = profile
        
class GameServer:
    def __init__(self,uid,status,settings):
        self.id = uid
        self.status = status
        
        if settings.__class__.__name__ == GameServerSettings:
            self.settings = settings
            GameServers.append(self)
        else:
            loghandler.printerror("GameServer settings is not a valid GameServerSettings object.")
           


        
            
    #Server control logic
    # 0 = Stopped, 1 = Starting, 2 = Running
    def isRunning(self):
        return self.status == 2
    def stop(self):
        dockercontroller.StopInstance(self)
    def start(self):
        dockercontroller.StartInstance(self)
        
    
        




def GetGameServer(uid):
    for server in GameServers:
        if server.id == uid:
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
        server.stop()
        GameServers.remove(server)
        
def StartAllServers():
    for server in GameServers:
        server.start()
def GetServerByIndex(idx):
    return GameServers[idx]

def GetServerIndex(server):
    return GameServers.index(server)

def GenerateUid():
    return "".join(str(ord(x)) for x in str(uuid.uuid4()))