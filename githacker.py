#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports
import os
import threading
import requests
import random
import sys
import re

log = []

threadNumber = 50

def random_string(length):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join([random.choice(charset) for i in range(length)])

def dirlist(path, allfile):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        else:
            allfile.append(filepath)
    return allfile


def downloadFile(url, path):
    if url in log:
        print("[-] Downloaded!")
    else:
        log.append(url)
    index = path[::-1].find("/")
    folder = path[0:-index]
    try:
        print("[+] Make dir : {}".format(folder))
        os.makedirs(folder)
    except:
        print("[-] Folder already existed!")
    print("[!] Getting -> {}".format(url))
    response = requests.get(url)
    if response.status_code == 200:
        with open(path, "wb") as f:
            f.write(response.content)
            print("[+] Success!")
    else:
        print("[-] [{}]".format(response.status_code))