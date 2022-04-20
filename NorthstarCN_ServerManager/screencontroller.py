"""
Base library for controlling multiple server instances from "screen"
Idea: each server is binded to specific screen session with the same random docker name, so we can have multiple instances running at the same time.
"""

def NewScreenSubProcess(serveruid,startupcommand):
    subprocess.run(["screen", "-S", serveruid , startupcommand])