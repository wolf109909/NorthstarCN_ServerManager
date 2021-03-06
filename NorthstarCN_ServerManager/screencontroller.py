"""
Base library for controlling multiple server instances from "screen"
Idea: each server is binded to specific screen session with the same random docker name, so we can have multiple instances running at the same time.
"""
# I moved to tmux after realising screen is kinda bad for this
import subprocess
import platform
import os
import servercontroller
import loghandler
def NewScreenSubProcess(serveruid,startupcommand):
    servercontroller.RunShell(f"tmux new-session -d -n {serveruid}")
    servercontroller.RunShell(f"tmux send-keys -t {serveruid} '{startupcommand}' C-m")
    
def KillScreenSubProcess(serveruid):
    loghandler.printinfo(f"Killing tmux session:{serveruid}")
    servercontroller.RunShell(f"tmux send-keys -t {serveruid} 'C-b :kill-session'")
    loghandler.printinfo(f"Killing Docker container:{serveruid}")
    servercontroller.RunShell(f"docker stop {serveruid}")    

    
    