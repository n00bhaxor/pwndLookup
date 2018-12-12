#! /usr/bin/env python3

import requests
import os,sys
import time

myFile = sys.argv[1]
# truncated = sys.argv[2] will implement later

# AUP says no more than 1 lookup every 1500ms,
# and identify user agent

mySleep=.1500

user_agent = {'User-agent': 'n00bhaxor-pwnage-checker'}

def getPwnd(email, truncated):
    url = "https://haveibeenpwned.com/api/v2/breachedaccount/"
    if truncated == 'n':
        url = url + email
        response = requests.get(url, headers=user_agent)
        if response.status_code != '200':
            return 'Empty'
        else:
            response = response.json()
            return response
    if truncated == 'y':
        url = url + email + "?truncatedResponse=True"
        response = requests.get(url, headers=user_agent)
        if response.status_code != 200:
            return 'Empty'
        else:
            response = response.json()
            return response


f = open(myFile, 'r')

for email in f.readlines():
    email = email.rstrip()
    data = getPwnd(email, 'y')
    if data == 'Empty':
        print("No Data for " + email)
        print("\r\n")
        time.sleep(mySleep)
    else:
        for i in data:
            print("emailAddress: " + email)
            print("Name: " + i['Name'])
            for dataType in i['DataClasses']:
                print(dataType)
            print("\r\n")
        time.sleep(mySleep)
