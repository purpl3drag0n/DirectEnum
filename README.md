# DirectEnum
A simple python script that sends GET requests to a domain from a list.
***********************************************************************

  ____                        ___
 (|   \ o                    / (_)
  |    |    ,_    _   __ _|_ \__   _  _           _  _  _
 _|    ||  /  |  |/  /    |  /    / |/ |  |   |  / |/ |/ |
(/\___/ |_/   |_/|__/\___/|_/\___/  |  |_/ \_/|_/  |  |  |_/


purpl3drag0n: Use the program at your own risk. I am not responsible for it's misuse.
usage: DirectEnum.py [-h] -f SHEETNAME -u BASEWEB [-d DELAY] [-https] [-s]

Quickly enumerate subdomains

optional arguments:
  -h, --help    show this help message and exit
  -f SHEETNAME  Excel file to read subdomains from (must have 'dirs' in row 1
                column A) Don't add .xlsx on command line. Must be a .xlsx file.
  -u BASEWEB    Website enumeration will be done on.
  -d DELAY      Delay in between requests in seconds. (default is 10)
  -https        Use https. (http by default)
  -s            Save subdomains and response codes. (saves in .xls file)
  
  Ex:
  python DirectEnum.py -u google.com -f subdomains -d 1 -https -s
  
  
  
  
  
