#  LastPass Delete Script
#
#  This is a demonstration script of the LastPass API capability, specifically removing users from business account and deleting users (soft and hard)
#
#  Usage
#  python3 lastpass_delete.py -c credentials.json -i emailList.csv
#
#
# Last update:  June 2022 by Nadeem Rasool
#
#
#
# THERE ARE NO EXPLICIT NOR IMPLICIT WARRANTIES OF THIS CODE.  THIS CODE IS PROVIDED ON AN AS-IS BASIS AND IS NOT SUPPORTED BY LASTPASS.
#
#
#

import requests
import json
import sys
import getopt
import csv
from csv import reader

credFile =""
inputFile =""
argv = sys.argv[1:]

try:
    options, args = getopt.getopt(argv, "c:i:",
                               ["cred =",
                                "input ="])
except:
    print("Usage: python3 lastpass_delete.py -c credentials.json -i emailList.csv")

 
for name, value in options:
    if name in ['-c', '--cred']:
        credFile = value
    elif name in ['-i', '--input']:
        inputFile = value
 
if credFile == "":
    print("Usage: python3 lastpass_delete.py -c credentials.json -i emailList.csv")
    quit()

# Opening JSON file
credFileObject = open(credFile)

 
# returns JSON object as a dictionary
creddata = json.load(credFileObject)

cidFile = creddata['cid']
print("Loaded cid")
provHashFile = creddata['provHash']
print("Loaded provHash")

url = "https://lastpass.com/enterpriseapi.php"
headers = {
  'Content-Type': 'application/json'
}

# open file in read mode
with open(inputFile, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        payload = json.dumps({
            "cid": cidFile,
            "provhash": provHashFile,
            "cmd": "deluser",
            "data": {
                "username": row[0],
                "deleteaction": row[1]
                }
            })
        response = requests.request("POST", url, headers=headers, data=payload)
       # print(row,response.text)
        print(", ".join(row),",",response.text)

#Close the file for safety
credFileObject.close()
read_obj.close()