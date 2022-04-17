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
        
 
   def do_createserver(self,inp):
        print("Adding '{}'".format(inp))
        name = input("Specify Server name:")
        port = input("Specify Server port:")
        authport = input("Specify Server authport:")
        profile = input("Specify Server profile:")
        uid = servercontroller.GenerateUid()
        settings = servercontroller.GameServerSettings(name,port,authport,profile)
        servercontroller.GameServer(uid,0,settings)
        
        
   def do_startserver(self,inp):
       if inp == None:
           print("No server specified")
           
       print("Starting Server:"+inp)
       server = servercontroller.GetServerByIndex(int(inp))
       if server == None:
           print("Server not found")
       else:
           server.Start()
       
   def do_stopserver(self,inp):
       print("Stopping Server:"+inp)
       server = servercontroller.GetServerByIndex(int(inp))
       if server == None:
           print("Server not found")
       else:
           server.Stop()
   def do_listservers(self,inp):
       print("Servers Available:")
       for server in servercontroller.GetServers():
           idx = servercontroller.GetServerIndex(server)
           uid = server.uid
           name = server.settings.name
           port = server.settings.port
           authport = server.settings.authport
           profile = server.settings.profile
           print(f"INDEX:{idx} || UID:{uid} || NAME:{name} || PORT:{port} || AUTHPORT:{authport} || PROFILE:{profile}")
       
MainShellLoop().cmdloop()