import loghandler
import dockercontroller
import servercontroller
import os
import sys
import time
import json
from cmd import Cmd

class MainShellLoop(Cmd):
   def do_runserver(self, inp):
        print("Run Server:"+inp)
        return True
 
   def do_createserver(self, inp):
        print("Adding '{}'".format(inp))
        name = input("Specify Server name:")
        port = input("Specify Server port:")
        authport = input("Specify Server authport:")
        profile = input("Specify Server profile:")
        uid = servercontroller.GenerateUid()
        settings = servercontroller.GameServerSettings(name,port,authport,profile)
        servercontroller.GameServer(uid,0,settings)
        
        return True
   def do_startserver(self,inp):
       if inp == None:
           print("No server specified")
           return True
       print("Starting Server:"+inp)
       servercontroller
       return True
   def do_stopserver(self,inp):
       print("Stopping Server:"+inp)
       return True
   def do_listservers(self):
       print("Servers Available:")
       for server in servercontroller.GetServers():
           idx = servercontroller.GetServerIndex(server)
           name = server.settings.name
           port = server.settings.port
           authport = server.settings.authport
           profile = server.settings.profile
           print(f"INDEX:{idx} || NAME:{name} || PORT:{port} || AUTHPORT:{authport} || PROFILE:{profile}")
       return True
MainShellLoop().cmdloop()