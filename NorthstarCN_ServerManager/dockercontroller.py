"""
Server Launching/Stopping module for docker environment
"""
import os
import loghandler
import servercontroller 
import screencontroller
import platform

GameServerBaseFileDirectory = "/root/tf2/content"
def RunShell(command):
    if platform.system() != "Linux":
        print(command)
    else:
        os.system(command)

    
def ParseStartupCommand(GameServer):
    if GameServer.__class__.__name__ == "GameServer":
        containerName = str(GameServer.uid)
        containerNameArg = f"--name {containerName}"
        loghandler.printinfo("Parsing Startup Command")
        serverName = str(GameServer.settings.name)
        serverPort = str(GameServer.settings.port)
        serverAuthport = str(GameServer.settings.authport)
        serverProfile = str(GameServer.settings.profile)
        profileArgString = f"--env NS_EXTRA_ARGUMENTS=\"-profile {serverProfile}\""
        serverStartupCommand = f"docker run --rm --interactive --pull always {containerNameArg} --publish {serverAuthport}:{serverAuthport}/tcp --publish {serverPort}:{serverPort}/udp --mount \"type=bind,source={GameServerBaseFileDirectory},target=/mnt/titanfall,readonly\" --env NS_SERVER_NAME=\"{serverName}\" {profileArgString} ghcr.io/pg9182/northstar-dedicated:1-tf2.0.11.0"
        return serverStartupCommand
    else:
        loghandler.printerror("GameServer is not a valid GameServer Object!")
        return None
def StartInstance(GameServer):
    if GameServer.status == 1:
        loghandler.printinfo("Server is already running")
        return
        
        
    loghandler.printinfo("Starting Server:" + GameServer.settings.name)
    try:
        StartupCommand = ParseStartupCommand(GameServer)
    except:
        loghandler.printerror("Error occurred while trying to parse Startup Command")
    else:
        loghandler.printinfo("Successfully Parsed Startup Command")
        if StartupCommand != None:
            NewScreenSubProcess(GameServer.uid,StartupCommand)
            GameServer.status = 1
        else:
            loghandler.printerror("Invalid Startup Command!")
            GameServer.status = 0
            
def StopInstance(GameServer):
    if GameServer.status == 0:
        loghandler.printinfo("Server is not running!")
        return
    loghandler.printinfo("Stopping Server:" + GameServer.settings.name)
    try:
        containerName = str(GameServer.uid)
        serverStopCommand = f"docker stop {containerName}"
        RunShell(serverStopCommand)
        GameServer.status = 0
    except:
        loghandler.printerror("Error occurred while trying to stop server")
    else:
        loghandler.printinfo("Successfully stopped server")