import shutil
import os
from os.path import basename
import sys
import glob

def moveIntoFolders():
    # Open each of the scripts and move to new folders
    sourcePath = "/Users/dchege711/Reddit_Daily_Programmer/Timeless_Discussions"

    for scriptPath in glob.glob(os.path.join(sourcePath, '*.md')):
        fileName = basename(scriptPath).split('.')[0]
        destination = sourcePath + "/" + fileName + "/"
        os.mkdir(destination)
        shutil.move(scriptPath, destination)

def updateReadme():
    readme = open('README.md', 'w')

    # Sample URL: https://github.com/dchege711/Reddit_Daily_Programmer/blob/master/Easy/135%20%5BEasy%5D%20Arithmetic%20Equations/135%20%5BEasy%5D%20Arithmetic%20Equations.md
    # Generated: https://github.com/dchege711/Reddit_Daily_Programmer/            /Easy/135%20%5BEasy%5D%20Arithmetic%20Equations/135%20%5BEasy%5D%20Arithmetic%20Equations.md
    baseURL = "https://github.com/dchege711/Reddit_Daily_Programmer/tree/master/"
    path = "/Users/dchege711/Reddit_Daily_Programmer/"
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith((".md")):
                filePath = os.path.join(root, name)
                filePath = filePath.replace('/Users/dchege711/Reddit_Daily_Programmer/', 'https://github.com/dchege711/Reddit_Daily_Programmer/blob/master/')
                filePath = filePath.replace(' ', '%20')
                filePath = filePath.replace('[', '%5B')
                filePath = filePath.replace(']', '%5D')
                readme.write("* [" + name.split('.md')[0] + "](" + filePath + ")\n")
