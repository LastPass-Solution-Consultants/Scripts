# LastPass Scripts
Useful scripts thats clients can use with LastPass

1. Lastpass_reinvite.py - A script which allows you to reinvite users to LastPass via a CSV file and using a credentials file to run the APIs
   Usage: python3 lastpass_reinvite.py -c credentials.json -i emailList.csv

1. Lastpass_delete.py - A script which allows you to delete users in LastPass via a CSV file and using a credentials file to run the APIs. You have the option of soft and hard delete. Also you can disable users.
   Usage: python3 lastpass_delete.py -c credentials.json -i emailList.csv
   
