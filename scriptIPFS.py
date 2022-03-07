import requests
import json
import os
import csv

header = ['image', 'IPFS']

images = os.listdir("./images/")


with open('ipfs.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)

    for image in images:
        # write the data
        data=[]

        name=image.replace(".png","").replace(".jpg","")
        data.append(name)

        url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
        payload={}
        files=[
        ('file',('file',open("./images/"+image,'rb'),'application/octet-stream'))
        ]
        headers = {
        'pinata_api_key': 'APIKEY',
        'pinata_secret_api_key': 'SECRETAPIKEY'
        }
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        info=json.loads(response.text)
        data.append("ipfs://"+info['IpfsHash'])
        writer.writerow(data)
