#!/usr/bin/python3.5

### Pass operational commands to vrouter using REST API

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import socket

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

############################################################

username="vyatta"
password="vyatta"

hostname="vrouter-a"
command='show interface'

#############################################################


def http_post (req_url, headers):
	
	return requests.post(req_url, data="",auth=(username, password), verify=False, headers=headers)


def http_get (req_url, headers):

	return requests.get(req_url, auth=(username, password), headers=headers, verify=False)


hostip = socket.gethostbyname(hostname)

command=command.split()

req_url = "https://" + hostip + "/rest/op"
for word in command:
	req_url += "/"+word

headers={'Host': hostip,
	'Accept':'application/json' , 
	'Vyatta-Specification-Version': '0.1'
	}


r = http_post(req_url,headers)
url = 'https://' + hostip + '/' + (r.headers['Location'])
r2 = http_get(url, headers)


print( '\n==========================================\nREST call/answer status codes : {}/{}\n==========================================\n\n{}\n '\
	.format(r.status_code, r2.status_code, r2.content.decode()))




 