from datetime import datetime
import os
import getpass
# import pyperclip
import xerox


# pswd = getpass.getpass('Password:')
USERNAME = "RAJ"
passcode = getpass.getpass('Password:')

if passcode != USERNAME:
  print("Incorrect passcode")
  os._exit(0)
# today = datetime.now()
# today_date = today.strftime("%Y%m%d")
date_input = input("Enter date(yyyy-mm-dd): ")
# date_list = date_input.split("-")
# print(date_list)
# print(today)
# today_date = ''.join(date_list)
# print(today_date)

date_format = '%Y-%m-%d'
try:
   # formatting the date using strptime() function
   dateObject = datetime.strptime(date_input, date_format)
   formated_date = dateObject.strftime("%Y%m%d")

# If the date validation goes wrong
except ValueError:
   # printing the appropriate text if ValueError occurs
   print("Incorrect data format, should be YYYY-MM-DD")
   os._exit(0)

print("Continue text")

print(formated_date)
graph_url = USERNAME
xerox.copy(graph_url)
print("Text copied")