#!/usr/bin/env python
import xlwt 
from xlwt import Workbook
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from datetime import datetime
from datetime import date
import argparse
import requests
import time
import sys



print("\n  ____                        ___                           ")
print(" (|   \ o                    / (_)                          ")
print("  |    |    ,_    _   __ _|_ \__   _  _           _  _  _   ")
print(" _|    ||  /  |  |/  /    |  /    / |/ |  |   |  / |/ |/ |  ")
print("(/\___/ |_/   |_/|__/\___/|_/\___/  |  |_/ \_/|_/  |  |  |_/\n\n")
print("purpl3drag0n: Use the program at your own risk. I am not responsible for it's misuse.")


parser = argparse.ArgumentParser(description="Quickly enumerate subdomains")
parser.add_argument("-f",help="Excel file to read subdomains from. (must have 'dirs' in row 1 column A) Don't add .xlsx on command line",dest="sheetname",type=str, required=True)
parser.add_argument("-u",help="Website enumeration will be done on.",dest="baseweb",type=str, required=True)
parser.add_argument("-d",help="Delay in between requests in seconds. (default is 10)",dest="delay",type=int, required=False)
parser.add_argument("-https",help="Use https. (http by default)", dest="https", action="store_true",required=False)
parser.add_argument("-s",help="Save subdomains and response codes. (saves in .xls file)",dest="save",action="store_true", required=False)
args=parser.parse_args()

if args.https == True:
    httporhttps = "https://"
else:
    httporhttps = "http://"

def getrequests():
    
    sheetname = args.sheetname + ".xlsx"
    var1 = pd.read_excel(sheetname)
    var2 = var1['dirs']

    delay = 10
    if args.delay != None:
        delay = args.delay

    if args.save == True:
        wb = Workbook() 
        sheet1 = wb.add_sheet('Sheet 1')

    print("-"*80)
    t1 = datetime.now()
    print('\nStarted at ', t1, "\n")
    print("-"*80)
    print("\n")

    i = 0 
    while i < len(var2):
        try:
            directory = var2[i]
            website1 = httporhttps + args.baseweb + directory 
            if args.save == True:
                sheet1.write(i, 0, website1)
            req = requests.get(website1)
            if args.save == True:
                sheet1.write(i, 1, req.status_code)
            print("\n" + str(website1) + "               " + str(req.status_code) + "\n")
            time.sleep(delay)
            i += 1
            if args.save == True:
                wb.save(((str(args.sheetname) + str(date.today())) + ".xls"))
        except KeyboardInterrupt:
            print("^C")
            break
        except:
            print("\nError sending request\n")
            i += 1
            time.sleep(delay)
            if args.save == True:
                sheet1.write(i, 0, directory)
                wb.save(((str(args.sheetname) + str(date.today())) + ".xls"))

    if args.save == True:
        wb.save(((str(args.sheetname) + str(date.today())) + ".xls"))
    t2 = datetime.now()
    total =  t2 - t1
    print('Completed in: ', total," \n\n")
    

if args.baseweb !=None:
    getrequests()


