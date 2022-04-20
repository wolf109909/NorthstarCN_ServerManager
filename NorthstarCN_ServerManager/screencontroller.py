"""
Base library for controlling multiple server instances from "screen"
Idea: each server is binded to specific screen session with the same random docker name, so we can have multiple instances running at the same time.
"""
# I moved to tmux after realising screen is kinda bad for this
import subprocess
import platform
import os
def RunShell(command):
    if platform.system() != "Linux":
        print(command)
    else:
        os.system(command)
def NewScreenSubProcess(serveruid,startupcommand):
    RunShell(f"tmux new-session -d -n {serveruid}")
    RunShell(f"tmux send-keys -t {serveruid} '{startupcommand}' \n ")