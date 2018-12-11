import winrm
import configparser
import ast

config = configparser.ConfigParser()
config.read('config.ini')
user = config['User']

username = user['username']
password = user['password']

qaList = ast.literal_eval(config.get('Servers', 'serverList'))

for i in range(len(qaList)):
    print("Connecting to - " + qaList[i])
    s = winrm.Session(qaList[i], auth=(username, password), transport='ntlm')
    print("Connected to - " + qaList[i])

# r = s.run_cmd("e:\\sms\\deploy\\update.py  12697")
#
# print(r.std_out)
