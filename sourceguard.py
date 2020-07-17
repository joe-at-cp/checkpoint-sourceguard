#!/usr/bin/python

#CheckPoint SourceGuard Demo
#Joe Dillig - Check Point Software 2020

import boto3

#Sensitive Information
username="myusername"
password="mypassword"

aws_access_key = 'AKIAIBCRGWWBBZPIZFTR'
aws_secret_access_key = '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'

s3 = S3Connection( aws_access_key, aws_secret_access_key )
s3 = session.resource('s3')
bucket = s3.Bucket(S3_BUCKET)
bucket.upload_file(file, key, ExtraArgs={'ACL':'public-read'})

#Malicious URLs
url='textspeier.de''
headers = {'Content-type': 'application/json', 'Accept': 'bla'}
data = {}
r = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
jsonreturn = json.loads(r.text)
