#!/usr/bin/python3
import requests
import json
messages="Tes Jumat"
url = 'https://webexapis.com/v1/messages'
file=open("email.txt","r")
data=[]
for i in file:
    try:
        access_token = 'YjRlY2Q1MjMtZjQ0Zi00OWI5LTgzNzAtNDc1Y2M3YWYwOTMzOTY0NGRiZTYtNDc3_P0A1_296842f3-00c1-4128-b47d-4e1e1fd7d576'
        i = i.replace("\n", "")
        data.append(i)
        headers={
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
        }   
        params = {'toPersonEmail': i, 'markdown':messages}
        res = requests.post(url, headers=headers, json=params)
        res.raise_for_status()
        print(json.dumps(res.json(), indent=4))
    except requests.exceptions.RequestException:
        print("Email tidak valid ! pada baris ke -",data.index(i)+1)
print("Daftar Email : ",data)
