import requests

from random import randint
from encode_image import ImageBase64

result = ImageBase64.encode('send_image.jpg')

# with open('image_base64', 'w', encoding='utf-8') as image_base64:
#     image_base64.write(result)
url = r'http://127.0.0.1:5000/api-external/add-visit-image-to-mediafile/'

data = {'dicom_uid': f'{randint(1, 999)}',
        'image': result,
        'image_uid': f'{randint(1, 999)}'}

headers = {'Content-type': 'application/json',
           'Authorization': 'Token LookInside'}

post_study = requests.post(url, verify=False, headers=headers, json=data)
print(f'STATUS_CODE: {post_study.status_code}')
print(f'RESPONSE: {post_study.text}')