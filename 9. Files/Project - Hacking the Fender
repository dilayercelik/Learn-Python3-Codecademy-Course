#Module "Files" - Project (CSV, JSON)

#Question 1
import csv

#Question 2
compromised_users = []

#Question 3-4-5-6-7
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)

  for row in password_csv:
    password_row = row
    compromised_users.append(password_row['Username'])

#Question 8-9-10-11
with open('compromised_users.txt', 'w') as compromised_user_file:
  for compromised_user in compromised_users:
    compromised_user_file.write('Username')


#Question 12
import json

#Question 13-14
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {'recipient': 'The Boss', 'message': 'Mission Success'}
#Question 15 still indented within 'with':
  json.dump(boss_message_dict, boss_message)


#Question 16
with open('new_passwords.csv', 'w') as new_passwords_obj:
#Question 17-18
  slash_null_sig = "signature"
  new_passwords_obj.write(slash_null_sig)

