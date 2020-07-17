#!/usr/bin/python

#CheckPoint SourceGuard Demo
#Joe Dillig - Check Point Software 2020

#Sensitive Information
username="myusername"
password="mypassword"

aws_access_key_id = "209ulksopslkmc08gb8ebnr2esf"
aws_secret_access_key = "xlkxj08slkw09u34pkj3.kmssdfsdff=="

#Malicious URLs
url='textspeier.de''
headers = {'Content-type': 'application/json', 'Accept': 'bla'}
data = {}
r = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
jsonreturn = json.loads(r.text)
