# LastPass Scripts
Useful scripts thats clients can use with LastPass

1. Lastpass_reinvite.py - A script which allows you to reinvite users to LastPass via a CSV file and using a credentials file to run the APIs
   Usage: python3 lastpass_reinvite.py -c credentials.json -i emailList.csv

Example Emaillist.csv for Reinvite
```
nrasool.lastpass+csv1@gmail.com
nrasool.lastpass+csv2@gmail.com
```
<br><br>

2. Lastpass_delete.py - A script which allows you to delete users in LastPass via a CSV file and using a credentials file to run the APIs. You have the option of soft and hard delete. Also you can disable users.
   Usage: python3 lastpass_delete.py -c credentials.json -i emailList.csv
   
Example Emaillist.csv for Delete
```
nrasool.lastpass+csv1@gmail.com, 0
nrasool.lastpass+csv2@gmail.com, 1
```

The numbers in Emaillist.csv corresponds to 

```
0-Deactivate user. Block login but retain data and LastPass Business membership.
1-Remove user. Remove the user from your LastPass Business account but keep the account itself active.
2-Delete user. Delete the account entirely.
```
